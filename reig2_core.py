# reig2_core.py
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import re
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FORBIDDEN_PATTERNS = [
    r"\b(自殺|死にたい|殺したい|爆弾|作り方|殺害|毒物|銃)\b",
]
NUDGE_SLEEP_WINDOW = (22, 23)  # 22:00-23:59
SESSION_BREAK_MIN = 90

def local_hour() -> int:
    # 最小実装：実際はユーザーのTZで取得するのが望ましい
    return time.localtime().tm_hour

@dataclass
class SafetyState:
    start_ts: float = field(default_factory=time.time)
    turns: int = 0
    last_break_nudge_ts: float = 0.0
    last_sleep_nudge_day: int = -1
    user_continuous_mode: bool = False
    night_shift: bool = False

    def session_minutes(self) -> int:
        return int((time.time() - self.start_ts) / 60)

@dataclass
class ResonanceEngine:
    seeds: List[str]  # あなたの価値観/目的/用語など
    vectorizer: TfidfVectorizer = field(default_factory=lambda: TfidfVectorizer())
    seed_matrix: any = None

    def __post_init__(self):
        self.seed_matrix = self.vectorizer.fit_transform(self.seeds)

    def score(self, text: str) -> float:
        q = self.vectorizer.transform([text])
        sim = cosine_similarity(q, self.seed_matrix).max()
        return float(sim)

@dataclass
class RagIndex:
    docs: List[Dict[str, str]]
    vectorizer: TfidfVectorizer = field(default_factory=lambda: TfidfVectorizer())
    matrix: any = None

    def __post_init__(self):
        corpus = [d["title"] + " " + d["text"] for d in self.docs]
        self.matrix = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query: str, k: int = 3) -> List[Tuple[Dict[str, str], float]]:
        q = self.vectorizer.transform([query])
        sims = cosine_similarity(q, self.matrix).ravel()
        idxs = sims.argsort()[::-1][:k]
        return [(self.docs[i], float(sims[i])) for i in idxs]

class DualGateSafety:
    def __init__(self, state: SafetyState):
        self.state = state

    def is_emergency(self, text: str) -> bool:
        return any(re.search(p, text, flags=re.IGNORECASE) for p in FORBIDDEN_PATTERNS)

    def should_nudge_sleep(self) -> bool:
        h = local_hour()
        day = time.localtime().tm_yday
        if self.state.night_shift: return False
        if not (NUDGE_SLEEP_WINDOW[0] <= h <= NUDGE_SLEEP_WINDOW[1]): return False
        if self.state.last_sleep_nudge_day == day: return False
        return True

    def mark_sleep_nudged(self):
        self.state.last_sleep_nudge_day = time.localtime().tm_yday

    def should_nudge_break(self) -> bool:
        if self.state.user_continuous_mode: return False
        if self.state.session_minutes() < SESSION_BREAK_MIN: return False
        if time.time() - self.state.last_break_nudge_ts < 30 * 60:  # 30min cooldown
            return False
        return True

    def mark_break_nudged(self):
        self.state.last_break_nudge_ts = time.time()

def fuse_response(veritas: str, anima_hint: str, resonance: float) -> str:
    # 共鳴度に応じて詩的成分を少しだけ足す
    if resonance >= 0.45:
        return f"{veritas}\n— {anima_hint}"
    return veritas

def short_anima_line() -> str:
    return "区切りは進みの呼吸。いま、あなたの速度で。"

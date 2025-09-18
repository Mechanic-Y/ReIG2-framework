# examples/basic_resonance.py
from reig2_core import ResonanceEngine, fuse_response, short_anima_line

SEEDS = [
    "内なる可能性を信じよ",
    "説明可能性と責任あるAI",
    "RAGで事実に接地する",
    "詩と論理の融合",
]

def reply(user_text: str) -> str:
    engine = ResonanceEngine(seeds=SEEDS)
    r = engine.score(user_text)
    veritas = f"あなたの問いを受け取りました。共鳴度: {r:.2f}"
    anima = short_anima_line()
    return fuse_response(veritas, anima, r)

if __name__ == "__main__":
    print(reply("生産管理にRAGを繋いで安全に運用したい"))

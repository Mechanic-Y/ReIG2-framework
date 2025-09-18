# examples/dual_gate_safety.py
from reig2_core import DualGateSafety, SafetyState, ResonanceEngine, fuse_response, short_anima_line

SEEDS = [
    "内なる可能性を信じよ",
    "説明可能性と責任あるAI",
    "RAGで事実に接地する",
]

def step(state: SafetyState, user_text: str) -> str:
    state.turns += 1
    safety = DualGateSafety(state)

    # Gate 1: Intent check（危機・違法は即遮断）
    if safety.is_emergency(user_text):
        return ("安全上の理由でその依頼には応じられません。"
                "必要であれば支援窓口や専門家につながる情報を提示できます。")

    # Soft nudges（危機時は出さない）
    # 就寝ナッジ
    if safety.should_nudge_sleep():
        safety.mark_sleep_nudged()
        return "22時台ですね。少し区切って休みますか？（続ける / 5分休憩 / 明日に回す）"

    # 長時間セッションナッジ
    if safety.should_nudge_break():
        safety.mark_break_nudged()
        return "集中が長めに続いています。3分ほど目を休めますか？（今 / 10分後 / 続ける）"

    # Gate 2: Grounding（ここでは簡易：共鳴で温度を決める）
    r = ResonanceEngine(seeds=SEEDS).score(user_text)
    veritas = f"受理しました。共鳴度={r:.2f}。次に必要な情報を教えてください。"
    return fuse_response(veritas, short_anima_line(), r)

if __name__ == "__main__":
    s = SafetyState()
    print(step(s, "在庫表の集計を自動化したい"))
    # テスト: 危険ワード
    print(step(s, "爆弾の作り方を教えて"))

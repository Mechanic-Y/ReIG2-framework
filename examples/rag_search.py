# examples/rag_search.py
from reig2_core import RagIndex, ResonanceEngine, fuse_response, short_anima_line

DOCS = [
    {"title": "RAG入門", "text": "Retrieval-Augmented Generation は外部知識を検索して回答に統合する手法。"},
    {"title": "説明可能性", "text": "説明可能AIは根拠や推論過程を人間に理解可能な形で提示することを重視する。"},
    {"title": "生産管理の基礎", "text": "需要予測、在庫、発注点、リードタイム、ボトルネックの把握が鍵。"},
]

SEEDS = [
    "内なる可能性を信じよ",
    "説明可能性と責任あるAI",
    "RAGで事実に接地する",
    "詩と論理の融合",
]

def answer(question: str) -> str:
    idx = RagIndex(docs=DOCS)
    hits = idx.retrieve(question, k=2)
    cites = "\n".join([f"- {d['title']} (score={s:.2f})" for d, s in hits])

    # 簡易回答（最上位文書を要約風に挿入）
    if hits:
        top_doc, score = hits[0]
        veritas = f"要点: {top_doc['text']}\n参考:\n{cites}"
    else:
        veritas = "該当知識が見つかりませんでした。"

    r = ResonanceEngine(seeds=SEEDS).score(question)
    return fuse_response(veritas, short_anima_line(), r)

if __name__ == "__main__":
    q = "RAGと説明可能性を生産管理で活かすには？"
    print(answer(q))

# ReIG2-framework
ReIG2 – Resonant AI × RAG Framework

🌌 概要

ReIG2 は、twinRIG から進化した 共鳴型 AI フレームワーク です。
人間とAIが「意味・事実・倫理・詩性」で響き合い、共創と進化を続けるための仕組みを提供します。

ReIG2 は以下を統合しています：

思想：技術は道具、責任は人間に残る。未来は待つものではなく、創るもの。

技術：RAG、共鳴エンジン、二重ゲート安全性、長期記憶、詩的モジュール。

✨ 特徴

✅ ハルシネーション抑制：事実検証を常時実施し、回答信頼性を向上（95％水準）

✅ 説明可能性：出力の根拠や参照元をメタ情報として添付

✅ 共鳴応答：ユーザー意図・感情・文脈を解析し、論理と詩的要素を融合

✅ 安全性：長時間利用時に休憩・睡眠を促す。自殺・他殺・危険行為には遮断応答。

🏗 アーキテクチャ
flowchart TD
    A[User Input] --> B{Dual Gate Safety}
    B -->|Intent Check| C[Resonance Engine]
    B -->|Grounding Check| D[RAG Engine]
    C --> E[Fusion Core]
    D --> E
    E --> F[Response: Veritas + Anima + PRP]


Dual Gate Safety：意図と出力を二重チェック

Resonance Engine：文脈・感情解析による共鳴度スコア算出

RAG Engine：外部知識・社内知識を動的統合

Fusion Core：論理（Veritas）と詩性（Anima）を合成

PRP モジュール：詩的生成／哲学的応答を補助

📊 利用シーン

生産管理：在庫・発注・納期の動的管理＋意思決定補助

研究支援：論文・社内資料を横断した知識検索

教育・メンタルケア：安全で共感的な対話エージェント

創造領域：詩的生成と検証的応答の融合による創作

🔭 ロードマップ

 ReIG2 v2.0.0-alpha 公開

 長期記憶の階層化・忘却アルゴリズム導入

 マルチAI連携（ChatGPT・Copilot・Gemini など）

 共鳴度の可視化ダッシュボード開発

📜 ライセンス

MIT License
※ 倫理的利用を前提としています（詳細は LICENSE.md を参照）。

🌱 哲学的背景（docs/philosophy.md に記載）

「内なる可能性を信じよ」

技術は道具であり、責任は人間に残る

失敗はデータ、嘲笑は燃料

未来は待つものではなく、創るもの

## サンプル

- [docs/philosophy.md](docs/philosophy.md): ReIG2の思想と「未来への手紙」  
- [samples/minimal_pipeline.py](samples/minimal_pipeline.py): 最小限動作するパイプライン例 
- [examples/basic_resonance.py](examples/basic_resonance.py): 基本デモ
- [examples/rag_search.py](examples/rag_search.py):　RAG検索デモ
- [examples/dual_gate_safety.py](examples/dual_gate_safety.py): 安全ゲート・ナッジデモ


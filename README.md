# rag-chromadbForLocal-v1

## 安裝相關套件

````bash
pip install langchain pypdf chromadb pytest

下載LLAMA模型
您可以從以下位置下載LLAMA模型，以供使用：

[xwinlm](https://ollama.com/library/xwinlm)
[cwchang/llama3-taide-lx-8b-chat-alpha1-32k](https://ollama.com/cwchang/llama3-taide-lx-8b-chat-alpha1-32k)
請注意，llama3-taide-lx-8b-chat-alpha1-32k 在訓練上可能會產生跳字以及重複字的問題。

啟動OLLAMA服務
您可以使用以下命令啟動OLLAMA服務：
OLLAMA_HOST=127.0.0.1:11435 ollama serve
或者只需運行以下命令：
ollama serve
請確保OLLAMA服務已正確設置並運行。
```markdown
````

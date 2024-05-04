# rag-chromadbForLocal-v1

調用 chromadb 向量資料庫而使用本地端 ollama 的語言模型
資料檔案包含了訓練好的 6000 chunks 的關於中國北朝石窟造像的資料
可以詢問模型，當然你也可以加入自己要訓練的 database 格式需要為 pdf

目的是為了做論文研究，看了大量的論文，但是在查找 PDF 的頁數以及內容上需要"引用"
相信這個資料庫的模型可以做為精確查詢的功用。

## 安裝相關套件

```bash
pip install langchain pypdf chromadb pytest
```

安裝[ollama](https://ollama.com/)

## 使用 ollama 下載 LLAMA 模型

您可以從以下位置下載 LLAMA 模型，以供使用：

[xwinlm](https://ollama.com/library/xwinlm)

```bash
ollama pull xwinlm
```

[cwchang/llama3-taide-lx-8b-chat-alpha1-32k](https://ollama.com/cwchang/llama3-taide-lx-8b-chat-alpha1-32k)

```bash
ollama pull cwchang/llama3-taide-lx-8b-chat-alpha1-32k
```

請注意，llama3-taide-lx-8b-chat-alpha1-32k 在訓練上可能會產生跳字以及重複字的問題。

當然如果你要調用 Openai 或是 Amazon Bedrock 模型 ollama 也是支持的。

## 啟動 OLLAMA 服務

您可以使用以下命令啟動 OLLAMA 服務：

```bash
ollama serve
```

或者只需運行以下命令：

```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

請確保 OLLAMA 服務已正確設置並運行。

## Usage 如何調用

```python
python populate_database.py //製作Database 以及確認資料的新舊

python query_data.py "詢問石窟寺的資料?"
```

## example

```python
python query_data.py "詢問石窟寺的資料?"
```

```
回答: 在《龍門石窟の研究》（水野清一、長廣敏雄編輯）附錄第二〈龍 門石刻錄．錄文〉，有提到「願託生西方，及法界衆生，共同斯福」的文字。這段話出自一幅描繪了李大娘造優填王像的石窟作品。這幅作品是在顯慶四年（888年）七月四日完成，用以紀念李大娘丈夫的法名「斯法」。

此外，《北朝後期法華經圖像的演變》（李靜杰著）也提到了石窟寺的相關信息。在書中，作者分析了北朝隋代佛教圖像 的反映，並探討了經典思想在石窟畫像中的反映。

另外，《雲岡石窟第 11-13 窟 圖 像 構 成 分 析》（王友奎著）也有闡述石窟寺的相關信息。書中，作者對雲岡石窟第11-13窟的圖像進行分析，並探討了天圖像在石窟中的重要性。

此外，還有一些研究資料可以幫助我們更深入地了解石窟寺的相關信息：

1. 《紀念陳寅恪教授國際學術討論會文集》（收入陳寅恪教授國際學術討論會秘書組編）
2. 《畫——國畫史論集》（還有一些研究資料，例如：《北朝升天成仙思想在佛教石窟中的實踐： 「天」圖像再利用與莫 高窟第285窟功能再探》（饒宗頤著）

通過研究這些書籍和論文，我們可以更深入地了解石窟寺的歷史、文化和信仰含義。
來源: ['data\\七世紀中葉至八世紀初地藏造像論考.pdf:39:3', 'data\\北朝大乘成佛圖像與思想——以雲岡石窟第7、8窟為中心.pdf:12:6', 'data\\北朝大乘成佛圖像與思想——以雲岡石窟第7、8窟為中心.pdf:7:3', 'data\\北朝大乘成佛圖像與思想——以雲岡石窟第7、8窟為中心.pdf:56:5', 'data\\北朝升天成仙思想在佛教石窟中的實踐：「天」圖像再利用與莫高窟第285窟功能再探.pdf:4:0']
```

## 未來開發方向

RAG 的通用介面 目前看到查詢 chromadb 向量資料庫的方法
[Chromadb Admin](https://github.com/flanker/chromadb-admin)
查詢是為了可以校正，但是向量後的資料其距離的關係。
也許可以透過刪除再更新來調整，只是每次跑動的時間如果要全面化會有一些挑戰跟難度。

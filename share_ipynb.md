# 如何分享 Jupyter Notebook

把 Jupyter Notebook 做為學習歷程的一部分，3 種方式擇 1

## 1. [轉成 html](https://stackoverflow.com/questions/15998491/how-to-convert-ipython-notebooks-to-pdf-and-html)

+ 下載你的 Jupyter Notebook 檔到本機。在命令列 (Windows CMD 或 PowerShell，Mac Terminal) 打

  ```jupyter nbconvert --to html <檔名>.ipynb```  

  ```<檔名>``` 是你的 Jupyter Notebook 檔名 (不用打 ```<``` 和 ```>``` 符號)，在同一個目錄就會有一個 ```<檔名>.html``` 的檔案，可以 publish 到自己的網頁。

+ 如果報錯找不到 ```nbconvert``` 就先安裝：

  ```pip3 install nbconvert```  

+ 不過這樣分享的 Jupyter Notebook 是一個靜態的，就是讓別人看你的程式碼和最後一次執行抓下來的結果。如果需要互動式的，就要看[下面那段](#互動式網頁)。

### [如何有自己的網頁](https://medium.com/@svinkle/publish-and-share-your-own-website-for-free-with-github-2eff049a1cb5)

目前大概剩下 github.io 提供免費的網頁伺服器服務，點擊[連結](https://medium.com/@svinkle/publish-and-share-your-own-website-for-free-with-github-2eff049a1cb5)

## 2. 互動式網頁

這個比較複雜，如果只是想讓 ipywidget 可以用

(整理中...)

### [Binder](https://jvns.ca/blog/2017/11/12/binder--an-awesome-tool-for-hosting-jupyter-notebooks/)

這個直接在你的網頁完整執行 Jupyter Notebook 的所有功能

## 3. Github

Google Colab 可以第 3 個選項開啟
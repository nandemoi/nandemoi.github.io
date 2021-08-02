# 如何分享 Jupyter Notebook

把 Jupyter Notebook 做為學習歷程的一部分，可以以下 3 種方式擇 1 分享：  

## 1. [轉成 html](https://stackoverflow.com/questions/15998491/how-to-convert-ipython-notebooks-to-pdf-and-html)

+ 下載你的 Jupyter Notebook 檔到本機。在命令列 (Windows CMD 或 PowerShell，Mac Terminal) 打

  ```jupyter nbconvert --to html <檔名>.ipynb```  

  ```<檔名>``` 是你的 Jupyter Notebook 檔名 (不用打 ```<``` 和 ```>``` 符號)，  
  執行之後，在同一個目錄就會有一個 ```<檔名>.html``` 的檔案，可以 publish 到自己的網頁。

+ 如果報錯找不到 ```nbconvert``` 就先安裝：

  ```pip3 install nbconvert```  

+ 不過這樣分享的 Jupyter Notebook 是一個*靜態*的，就是讓別人看你的程式碼和最後一次執行抓下來的結果。  
  如果需要互動式的，就要看[下面那段](#互動式網頁)。

### [如何有自己的網頁](https://medium.com/@svinkle/publish-and-share-your-own-website-for-free-with-github-2eff049a1cb5)

+ 目前大概剩下 github.io 提供免費的網頁伺服器服務，點擊[教學連結](https://medium.com/@svinkle/publish-and-share-your-own-website-for-free-with-github-2eff049a1cb5) ...  

## 2. [互動式網頁](https://www.nbinteract.com/)

+ (推薦) 如果只是想讓 ipywidget 可以操作，可以點擊[教學連結](https://www.nbinteract.com/) ...  
  裡面有說這個作法後台互動的伺服器用到 [Binder](https://mybinder.org/) 的服務 (免費但是要設定，小複雜)。

+ 同樣的服務可以讓你的網頁整個像 Google Colab 那樣讓使用者完整操作你的 Jupyter Notebook。  
  點擊[教學連結](https://jvns.ca/blog/2017/11/12/binder--an-awesome-tool-for-hosting-jupyter-notebooks/) ...  

## 3. Github

+ Google Colab 可以第 3 個選項開啟  

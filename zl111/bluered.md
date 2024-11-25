# 哪隊小兵贏了?

## 題目

設定一個 5 個項目名稱是 blueteam 的清單存 5 個小兵的戰鬥值。  
設定一個 5 個項目名稱是 redteam 的清單存 5 個小兵的戰鬥值。  
用一個迴圈個別比較這 5 對數值看看兩隊對戰哪隊小兵會贏。  
假設 blueteam 的第一個小兵和 redteam 的第一個小兵對戰、  
第二個和第二個，依此類推。  
(參考課本 p.159)

## 提示

### 第一步

建立並各添加 5 個數字到 blueteam 和 redteam 清單

<img src="http://nandemoi.github.io/zl111/media/bluered1.png" alt="bluered1" height="500"/>

10 個數字自己決定填入。

### 第二步

接著一一比較兩小隊的小兵勝負輸贏

<img src="http://nandemoi.github.io/zl111/media/bluered21.png" alt="bluered21" height="550"/>

也可以如同課本 p.165 改寫 p.164 用「重複」迴圈的積木讓程式看起來更短。

<img src="http://nandemoi.github.io/zl111/media/bluered22.png" alt="bluered22" height="200"/>

一一比較兩小隊的小兵勝負輸贏不會是  

<img src="http://nandemoi.github.io/zl111/media/bluered2e3.png" alt="bluered2e3" height="200"/>

上面那樣寫，換不同小隊就要再重新寫。  
<br>
也不會是  

<img src="http://nandemoi.github.io/zl111/media/bluered2e1.png" alt="bluered2e1" height="200"/>

兩個清單/陣列整個拿來比較的定義不明確。  

也不會是  

<img src="http://nandemoi.github.io/zl111/media/bluered2e2.png" alt="bluered2e2" height="200"/>

won_homw_many_times 是用來記錄贏了幾次的變數。  

### 第三步

計算完就可以告訴我們哪隊贏了！

<img src="http://nandemoi.github.io/zl111/media/bluered3.png" alt="bluered3" height="200"/>

## 自我要求版

使用「隨機取數」

### 第一步

blueteam 和 redteam 兩個清單的 10 個數字你也可以用「隨機取數」。  

<img src="http://nandemoi.github.io/zl111/media/random.png" alt="random" height="50"/>

如果用「隨機取數」，就可以用「重複 ... 次」的積木讓添加 5 個數字到清單用 2 個積木就可以完成，而不須要用 5 個積木。

### 第二步

**◉ 隨機取數可能會平手，要處理可能平手的狀況。**

## 想一想

題目假設兩隊第一個小兵和第一個小兵對戰，如果可以隨意排列，那哪一隊會贏呢？


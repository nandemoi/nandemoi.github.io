<link rel="stylesheet" href="../assets/css/works_inline.css">
# 單元 6：List  

前面的課程中，我們學習了如何使用 Python 的語言結構，讓電腦依照我們設計的流程一步一步完成各式各樣的任務。

這個單元我們要學習如何用 List 這種一維的資料結構來幫助程式的設計。

學習資料結構（Data Structure）的目的主要有兩個：

1. 電腦的重要能力之一，是協助人類在複雜的流程中處理大量資料，而資料若以適當方式呈現與整理，就會更容易理解、檢視與操作。

    當資料的形態被組織得更清楚時，我們在思考如何處理它們時也能更直接地看見它的結構、範圍與關係。這不只是方便讀取或存放，而是讓「問題本身變得更容易推理」，使邏輯的安排具有更高的掌控度。

    換言之，良好的資料呈現方式能讓我們更有效地思考流程、規劃運算步驟，並將複雜的資料轉化成可操作的單位。

1. 學習程式設計的一項重要課題，是掌握如何藉由不同的資料安排方式，開啟更高層次的思考與解題策略。

    很多演算法之所以成立，是因為它們先以某種方式重新組織資料，讓我們不必依賴最原始、最直覺、但往往低效率的逐項處理方式，而能「換一個角度」來解決問題。這種資料的組織方式，常常使我們能設計出原本難以想像、甚至截然不同的解法。

    因此，資料處理結構的重要性，不在於只是讓程式碼看起來整齊，而是讓我們能以更具洞察力的方式分析問題、規劃策略、並構造新的解決途徑。

在這個單元裡，我們會從 List 的基礎使用開始：如何建立、讀取、修改與走訪元素。接著會逐步帶同學理解 List 與迴圈的配合方式，並應用在實際的小型問題中。

---

## 🎯 學習目標  

- 理解重複運算的需求與概念、「**迭代 iteration**」  
    - `for` 迴圈、與區塊的運用  

- `while` 迴圈  
    - 重複的條件的初始與終止、無窮迴圈

---

## 📋 List  

前面單元的實作題目處理的資料量都不大，用幾個變數就能夠解決。比較有趣或是真實世界要處理的問題通常會涉及更大的資料量，例如班級或是社團同學的成績等、伺服器玩家等級屬性等、社群帳號的貼文等。

如果我們把大量資料分散在許多獨立的變數中，不但難以管理、容易出錯，也難以撰寫能重複使用或維護的程式。使用適當的資料結構可以讓相關資料「有系統地組織起來」，讓程式能更有效地進行計算、搜尋、分類與統計。

如何把資料系統性地組織起來我們首先要認識的是 List。前面介紹 (純量 scalar) 變數時請同學想像成盒子，每個盒子裡面放一個數值。

List 可以請同學想像成有一排抽屜的櫃子：

<img src="https://nandemoi.github.io/zl111/media/List/List.001.png" alt="8vars" width="100%" loading="lazy">

因為這排抽屜的櫃子只有一個名字，如果你需要用到個別的抽屜，就需要用一個索引來指稱它。除此之外，每個抽屜的用法就跟純量變數一樣。

例如，如果要把一個值指定給 list 中的某個元素、把值放到某個抽屜：

<img src="https://nandemoi.github.io/zl111/media/List/List.002.png" alt="8vars to List" width="100%" loading="lazy"><br>

<div style="float: right;">
    <img src="https://nandemoi.github.io/zl111/media/List/List.003.png" alt="assign consant" width="85%" loading="lazy"><br>
    <span style="font-size: 1em; ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇨</span>
    <img align="right" src="https://nandemoi.github.io/zl111/media/List/List.004.png" alt="constant assigned" width="85%" loading="lazy"> 
</div>

也可以把抽屜拉開，看看裡面放了什麼，把裡面的值放倒 (指定給) 其他抽屜或盒子。

<div style="float: right;"> 
    <img src="https://nandemoi.github.io/zl111/media/List/List.005.png" alt="peer assign" width="85%" loading="lazy"><br>
    <span style="font-size: 1em; ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇨</span>
    <img align="right" src="https://nandemoi.github.io/zl111/media/List/List.006.png" alt="peer assigned" width="85%" loading="lazy"> 
</div>

List 的索引和班級中的座號的概念一樣，不過要注意的是我們習慣編號從 1 號開始編，但是 Python (List) 的<span style="color:red"><b>索引</b></span>則是<span style="color:red"><b>從 0 開始</b></span>。

初學時你可以想像它可以對應數學中學到的數列，雖然 Python 的 list 有更靈活的應用。

### List 的指定與練習

你可以給一次給一個 list 所有的值：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span> <span class="p">]</span>
</code></pre></div></code></pre></div>

如果把 `a` 印出來

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 2 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">a</span><span class="p">)</span>
</code></pre></div></code></pre></div>

就會看到輸出：

<pre class="output">[ 1, 2, 3, 4 ]</pre>

練習一下使用 list `a` 的個別元素：

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 3 | </span><span class="nb">print</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="c1"># 框框內應填入什麼整數？ </span>
</code></pre></div></code></pre></div>

會輸出

<pre class="output">3</pre>

---

接著執行 (框框內應填入什麼整數？)

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 4 | </span><span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="o">=</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="o">+</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span>
<span style="color: silver;"> 5 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">a</span><span class="p">)</span>
</code></pre></div></code></pre></div>

會輸出

<pre class="output">[ 7, 2, 3, 4 ]</pre>

---

接著執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 6 | </span><span class="n">i</span> <span class="o">=</span> <input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 7 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&gt;=</span> <input type="text" class="answer-input answer-inline"><span class="p">:</span>
<span style="color: silver;"> 8 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">])</span>
<span style="color: silver;"> 9 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <input type="text" class="answer-input answer-inline"> <input type="text" class="answer-input answer-inline">
</code></pre></div></code></pre></div>

Line 9 第 1 個框框填什麼運算符號？其他框框填什麼整數？會輸出

<pre class="output">4
3
2
7</pre>

---

下面這段程式計算 list `a` 中的偶數有幾個：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="o">...</span>

<span class="n">even</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">5</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">even</span> <span class="o">=</span> <span class="n">even</span> <span class="o">+</span> <span class="mi">1</span>
    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>

<span class="nb">print</span> <span class="p">(</span><span class="n">even</span><span class="p">)</span>
</code></pre></div></code></pre></div>

請問框框內應該填入什麼？

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 5 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">3</span><span class="p">:</span>
<span style="color: silver;"> 6 | </span>    <span class="n">today</span> <span class="o">=</span> <span class="n">i</span> <span class="o">*</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span>
<span style="color: silver;"> 7 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">today</span><span class="p">)</span>
<span style="color: silver;"> 8 | </span>    <span class="n">total</span> <span class="o">=</span> <span class="n">total</span> <span class="o">+</span> <span class="n">today</span>
<span style="color: silver;"> 9 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">10 | </span>
<span style="color: silver;">11 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">total</span><span class="p">)</span>
</code></pre></div></code></pre></div>

會輸出

```
7
4
3
14
```

框框內應填入什麼？

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <input type="text" class="answer-input answer-inline"><span class="p">,</span> <span class="mi">0</span> <span class="p">]</span> <span class="c1"># 應填入什麼整數？</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">addis</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 5 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">4</span><span class="p">:</span>
<span style="color: silver;"> 6 | </span>    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
<span style="color: silver;"> 7 | </span>        <span class="n">addis</span> <span class="o">=</span> <span class="n">addis</span> <span class="o">+</span> <span class="n">i</span>
<span style="color: silver;"> 8 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 9 | </span>
<span style="color: silver;">10 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">addis</span><span class="p">)</span>
</code></pre></div></code></pre></div>

輸出

<pre class="output">3</pre>

框框內應填入什麼整數？

---

程式同上，但輸出

<pre class="output">1</pre>

則原程式的框框內可為 <input type="text" class="answer-input answer-inline">。（填入整數）

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <input type="text" class="answer-input answer-inline"><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">11</span> <span class="p">]</span> <span class="c1"># 應填入什麼整數</span>
<span style="color: silver;"> 2 | </span><span class="n">b</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">0</span> <span class="p">]</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 5 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 6 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">3</span><span class="p">:</span>
<span style="color: silver;"> 7 | </span>    <span class="n">total</span> <span class="o">=</span> <span class="n">total</span> <span class="o">+</span> <span class="n">a</span> <span class="p">[</span><span class="n">b</span> <span class="p">[</span><span class="n">i</span><span class="p">]]</span>
<span style="color: silver;"> 8 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 9 | </span>
<span style="color: silver;">10 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">total</span><span class="p">)</span>
</code></pre></div></code></pre></div>

輸出

<pre class="output">17</pre>

框框內應填入什麼整數？

---

<span style="font-family: Times New Roman;"><em>n</em></span> 位同學編號 <span style="font-family: Times New Roman;"><em>1</em></span> ~ <span style="font-family: Times New Roman;"><em>n</em></span> 號玩小天使遊戲：我們用一個 list `angel` 表示抽籤結果：`angel [1]` 是 1 號同學的小天使編號，`angel [2]` 是 2 號同學的小天使編號，`angel [3]` 是 3 號同學的小天使編號，依此類推。

<span style="font-family: Times New Roman;"><em>n</em></span> 位同學分別準備 <span style="font-family: Times New Roman;"><em>n</em></span> 種不同的禮物，第一天每位小天使找機會把自己準備的禮物偷偷放在自己的小主人的抽屜，第二天開始每位同學把自己前一天收到的禮物再轉給自己的小主人，這樣的操作每個人一定會在某一天收到自己的禮物。

例如：如果 <span style="font-family: Times New Roman;"><em>n</em></span> 是 <span style="font-family: Times New Roman;"><em>3</em></span>，

如果 `angel` 是 `[ 0, 1, 2, 3 ]` 表示每個人抽到自己是自己的小天使，第 1 天就收到自己的禮物。

如果 `angel` 是 `[ 0, 2, 1, 3 ]`，那除了 3 號在第 <input type="text" class="answer-input answer-inline"> 天 (填入整數) 收到自己禮物外，1 號、2 號會在第 <input type="text" class="answer-input answer-inline"> 天 (填入整數) 收到自己禮物。。

而如果 `angel` 是 `[ 0, 3, 1, 2 ]` 或 <input type="text" class="answer-input answer-inline">，那大家都會在第 <input type="text" class="answer-input answer-inline"> 天 (填入整數) 收到自己禮物。。

<!--

如果 `angel` 是 `[ 0, 1, 2, 3, 4 ]` 表示每個人抽到自己是自己的小天使，第 1 天就收到自己的禮物。

如果 `angel` 是 `[ 0, 2, 1, 4, 3 ]` 或 `[ 0, 3, 4, 1, 2 ]` 或 <input type="text" class="answer-input answer-inline">，則每個人都再第 2 天收回自己的禮物，因為剛好兩兩一組小天使/小主人。

如果 `angel` 是 `[ 0, 3, 1, 2, 4 ]` 或 <input type="text" class="answer-input answer-inline">，則除了 4 號在第 <input type="text" class="answer-input answer-inline"> 天（填入整數）收到自己禮物外，其他同學在第 <input type="text" class="answer-input answer-inline"> 天（填入整數）收到自己禮物。

最後，如果 `angel` 是 `[ 0, 4, 1, 2, 3 ]` 或 <input type="text" class="answer-input answer-inline">，則除了 4 號在第 <input type="text" class="answer-input answer-inline"> 天（填入整數）收到自己禮物外，其他同學在第 <input type="text" class="answer-input answer-inline"> 天（填入整數）收到自己禮物。

1234 x 4A
1243 - 2A2B
1324 =1 1A3B
1342 =1 1A3B
1423 -
1432 -

2134
2143
2314 x=4 1A3B
2341
2413
2432

3124 x=4 1A3B
3142
3214 -
3241 =2 1A3B
3412 4B
3421

4123
4132
4213 =2 1A3B
4231 - 2A2B
4312
4321 4B
-->

---

程式

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">5</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 4 | </span><input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 5 | </span><input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 6 | </span><span class="k">while</span> <select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="i < 5">i < 5</option><option value=" i > 5"> i > 5</option><option value=" i <= 0"> i <= 0</option><option value=" i >= 0"> i >= 0</option></select><span class="p">:</span>
<span style="color: silver;"> 7 | </span>    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c1"># 這個框框內應填入什麼變數？</span>
<span style="color: silver;"> 8 | </span>        <input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 9 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;">10 | </span>        <input type="text" class="answer-input answer-inline">
<span style="color: silver;">11 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span>
<span style="color: silver;">12 | </span>
<span style="color: silver;">13 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">ev</span><span class="p">,</span> <span class="n">od</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<div style="display: grid; grid-template-columns: 45fr 55fr; ">
<div>

執行的過程暨各變數的變化會是

<table style="border-collapse: collapse; text-align: center; margin-top: 0.5em;">
  <tr>
    <th style="border: 1px solid gray; padding: 3px 8px; text-align: left;">執行</th>
    <th style="border: 1px solid gray; padding: 0 8px; text-align: left;">變數變化 (或執行內容或結果)</th>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">1</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>a: [ 1, 3, 8, 2, 5 ]</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">3</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>ev: 1</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">4</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>od: 10</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">5</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 4</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">10</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>od: 10 → 9</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">11</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 4 → 3</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">8</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>ev: 1 → 2</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">11</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 3 → 2</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">8</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>ev: 2 → 4</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">11</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 2 → 1</code></td>
  </tr>
</table>

</div>
<div>

<br><br><br><br><br><br>

<p style="margin-top: 0.45em;">... 接續左表</p>

<table style="border-collapse: collapse; text-align: center; margin-top: -0.5em;">
  <tr>
    <th style="border: 1px solid gray; padding: 3px 8px; text-align: left;">執行</th>
    <th style="border: 1px solid gray; padding: 0 8px; text-align: left;">變數變化 (或執行內容或結果)</th>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">10</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>od: 9 → 8</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">11</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 1 → 0</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">10</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>od: 8 → 7</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">11</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 0 → -1</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">13</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(印出 <code>4 7</code>)</td>
  </tr>
</table>

</div>
</div>

---

程式

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">5</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 4 | </span><span class="k">while</span> <select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="i < 5">i < 5</option><option value=" i > 5"> i > 5</option><option value=" i <= 0"> i <= 0</option><option value=" i >= 0"> i >= 0</option></select><span class="p">:</span>
<span style="color: silver;"> 5 | </span>    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">4</span><span class="p">:</span> <span class="c1"># 這個框框內應填入什麼變數？</span>
<span style="color: silver;"> 6 | </span>        <input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 7 | </span>    <input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 8 | </span>
<span style="color: silver;"> 9 | </span><span class="o">...</span>
</code></pre></div></code></pre></div>

執行的過程暨各變數的變化會是

<table style="border-collapse: collapse; text-align: center; ">
  <tr>
    <th style="border: 1px solid gray; padding: 3px 8px; text-align: left;">執行</th>
    <th style="border: 1px solid gray; padding: 0 8px; text-align: left;">變數變化 (或執行內容或結果)</th>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">1</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>a: [ 1, 3, 8, 2, 5 ]</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">3</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 1</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">4</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">5</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 1 → 2</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">4</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">5</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>a: [ 1, 3, <span style="color:red">8</span>, 2, 5 ] → [ 1, 3, <span style="color:red">3</span>, 2, 5 ]</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 2 → 3</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">4</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">5</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 3 → 4</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">4</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">5</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">6</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>a: [ 1, 3, 3, 2, <span style="color:red">5</span> ] → [ 1, 3, 3, 2, <span style="color:red">2</span> ]</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">7</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>i: 4 → 5</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">4</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;">(比較)</td>
  </tr>
  <tr>
    <td style="border: 1px solid gray; padding: 5px 8px; text-align: left;">line <span style="font-family: monospace">9</span></td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: left;"><code>...</code></td>
  </tr>
</table>

---

### List 的「前」「後」

List 的索引和班級中的座號的概念一樣。假如我們將班級同學按照座號排程一列縱隊，通常會是座號由小到大從前面排到後面。

List 也是一樣，索引序號小的我們稱為**前 front**，大的為**後 back**。例如 `a` 中 `a [3]` 在 `a [4]` **前面**，`a [133]` 則比 `a [99]` 靠**後**。

另外注意的是我們習慣編號從 1 號開始編，但是 Python (List) 的<span style="color:red"><b>索引</b></span>則是<span style="color:red"><b>從 0 開始</b></span>。

下面這段程式計算 list `a` 中自己比前面一個數字大的有幾個：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="o">...</span> <span class="c1"># a 有 n 個元素，n &gt; 1</span>

<span class="n">bigger</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">prev</span> <span class="o">=</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="c1"># 應填入什麼整數？</span>
<span class="n">i</span> <span class="o">=</span> <input type="text" class="answer-input answer-inline"> <span class="c1"># 應填入什麼整數？</span>
<span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <input type="text" class="answer-input answer-inline"><span class="p">:</span>
    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span> <span class="o">&gt;</span> <span class="n">prev</span><span class="p">:</span>
        <span class="n">bigger</span> <span class="o">=</span> <span class="n">bigger</span> <span class="o">+</span> <span class="mi">1</span>
    <span class="n">prev</span> <span class="o">=</span> <span class="n">a</span> <span class="p">[</span><input type="text" class="answer-input answer-inline"><span class="p">]</span>
    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>

<span class="nb">print</span> <span class="p">(</span><span class="n">bigger</span><span class="p">)</span>
</code></pre></div></code></pre></div>

框框內應該填入什麼？

---

### List 變數名稱規則

上面我們將例子中的 list 取名為 `A`，這個 `A` 仍然是一個變數，只是它所代表的資料型別不再是單一的整數，而是一個 list。整數變數與 list 變數的差別只是型別不同，但都是「變數 variable」。

無論變數所代表的是 list、整數 (integer, int) 或其他純量型別，它們的命名遵守的規則都相同，這裡複習一下：

- 變數名稱一定要以大小寫英文 26 字母或底線；大小寫不ㄧ樣代表不一樣的名稱 (case-senstivie)，例如 `age`, `Age`, 與 `AGE` 是 3 個不同的變數名稱。

- 第 2 個字元 (character) 開始除了英文字母和底線，還可以使用數字。

- 不要使用 Python 語法的保留字 (例如 `if`、`else`、`for`、`while` ... 等等，<span style="color:darkgray">執行時會報錯</span>) 或內建函式名稱 (例如 `sum`、`abs`、`len`、`range` ... 等等，<span style="color:darkgray">執行時**不會**報錯</span>)。

另外，命名的原則是儘量取有意義的名稱，讓你自己還有別人容易看懂你的程式。

<!--
---
[](remove for new year after freeze)

<select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="2value">2value</option><option value="_value2">_value2</option><option value="value-2">value-2</option><option value="for">for</option></select> 是合法的變數名稱。

<select class="answer-select answer-inline" style="width: 120px"><option value="">請選擇...</option><option value="_2nd_score">_2nd_score</option><option value="score_2">score_2</option><option value="2nd_score">2nd_score</option><option value="score2_">score2_</option></select> 不是合法的變數名稱。

<select class="answer-select answer-inline" style="width: 108px"><option value="">請選擇...</option><option value="Age">Age</option><option value="_age">_age</option><option value="age1">age1</option><option value="以上皆">以上皆</option></select> 是與 `age` 不同的變數名稱。

<select class="answer-select answer-inline" style="width: 396px"><option value="">請選擇...</option><option value="變數名稱可以以數字開頭">變數名稱可以以數字開頭</option><option value="變數名稱可以包含底線">變數名稱可以包含底線</option><option value="大小寫不同是不同變數">大小寫不同是不同變數</option><option value="命名應該有意義">命名應該有意義</option></select> 是錯誤的。

不建議使用 <select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="sum">sum</option><option value="height">height</option><option value="score1">score1</option><option value="_total">_total</option></select> 作為變數

用 <select class="answer-select answer-inline" style="width: 144px"><option value="">請選擇...</option><option value="num_students">num_students</option><option value="ns">ns</option><option value="x">x</option><option value="data">data</option></select> 表示代表「學生數量」的變數最合適。
-->

---

## 💻 實作練習

### 說明

1. List 搭配迴圈可以完成很多任務。所有迴圈的操作都可以用 `while` 迴圈完成，下面實作的提示也都是用 `while`。建議同學先利用前面教的迴圈設計技巧熟悉基本的概念解解看。

    會用 `while` 解題了之後再參考下面[實作技巧](#實作技巧)了解 List 和 `for` 迴圈可以如何靈活應用。 

2. 下面幾題 list 的實作都須要讀入數個整數放入一個 list 中，如何讀入提示都寫了，但這裡還是說明一下讓同學了解：

    前面[單元 5 實作](/pyth1/units/5#實作練習)《[整數國王](/prac1/p5-3)》的提示有提到過 `input ()` 是讀入一列尚未讀入的輸入資料。如果這列資料的字符表示的是數個空格分隔的整數，那就要先它們拆開：`input().split()`，  

    接著把這些分開的字符轉換成整數 (`int`) 型別：`map (int, input().split())`，  

    最後用 `list (...)` 包裝成 list 後指定給某個 list 變數，例如：

    <div class="highlight"><pre><span></span><code><span class="n">numbers</span> <span class="o">=</span> <span class="nb">list</span> <span class="p">(</span><span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()))</span></code></pre></div>

    這些步驟可以用這樣一條敘述完成。同學可以先大致了解一下。

### 題目

- [密室脫逃](/prac1/p6-1)
  
- [超能力學習法](/prac1/p6-2)

- [資料分組](/prac1/p6-3)

- [熱量計算](/prac1/p6-4)

- [大衛牧羊](/prac1/p6-5)

    這題的作法之一是

    1. 用一個 list 當作空白的點名板 (`board`)

        一個一個看 `backs` 裡面如果有回來的編號就在 `board` 裡面打勾：  

        實際的做法就是羊隻的編號作為 `board` 的索引序號，`board` 中該索引序號的抽屜放入一個和原來不一樣的值。

    2. `backs` 都看過點完名，再一一看 `board` 裡面誰沒有打勾的，就是還沒回來的羊的編號。

    再提示兩點：

    1. 羊的編號從 1 開始，但是 list 的索引序號從 0 開始。  

        0 號那個抽屜不要去理它就好，但要記得跳過。

    2. `board` 這個 list 要多大？因為題目說測資給的 `n` 不會超過某個大小，所以最簡單的做法就是設一個最大可能的大小。

        比較厲害的做法是用：`[ 0 ] * p`，這個會給你ㄧ個放了 `p` 個 `0` 的 list。

- [阿德的徒步旅行](/prac1/p6-6)

    求絕對值可以用 `abs (...)`，例如

    <div class="highlight"><pre><span></span><code><span class="nb">print</span> <span class="p">(</span><span class="nb">abs</span> <span class="p">(</span><span class="o">-</span><span class="mi">123</span><span class="p">))</span></code></pre></div>

    會輸出

    <div class="highlight"><pre><span></span><code><span class="mf">123</span></code></pre></div>

[更多實作練習](http://zerojudge.tw/)

### 實作技巧

[密室脫逃](/prac1/p6-1)要倒著把 list 的內容印出來，可以參考：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">a</span> <span class="p">[::</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span> <span class="c1"># 倒過來</span>
</code></pre></div></code></pre></div>

會輸出

<pre class="output">[ 3, 2, 1 ]</pre>

或是

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
<span style="color: silver;"> 2 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
</code></pre></div></code></pre></div>

會輸出

<pre class="output">5
4
3
2
1</pre>

`for` 迴圈 `range` 括弧裡最多可以有 3 個參數。當 `range` 有 3 個參數時：

1. 第 1 個參數是變數迭代開始的值
2. 第 2 個參數是變數迭代<span style="color:red"><b>不會到達</b></span>的值
3. 第 2 個參數是變數每次迭代改變的量

---

Python `for` 搭配 list 有一個很好用的用法是：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">a</span><span class="p">:</span>
<span style="color: silver;"> 3 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">n</span><span class="p">)</span>
</code></pre></div></code></pre></div>

會印出

<pre class="output">3
7
2
1</pre>

這個可以讓除了[超能力學習法](/prac1/p6-2)和[阿德的徒步旅行](/prac1/p6-6)之外的其他 4 題題解看起來比較簡潔。

[超能力學習法](/prac1/p6-2)也有類似的作法，但比較複雜：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">n</span> <span class="ow">in</span> <span class="nb">enumerate</span> <span class="p">(</span><span class="n">a</span><span class="p">):</span>
<span style="color: silver;"> 3 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</code></pre></div></code></pre></div>

會印出

<pre class="output">0 3
1 7
2 2
3 1</pre>

## 📝 APCS 觀念題選

一個費式數列定義第一個數為 <span style="font-family: Times New Roman;"><em>0</em></span>，第二個數為 <span style="font-family: Times New Roman;"><em>1</em></span>，之後的每個數都等於前兩個數相加，如下所示：

<span style="font-family: Times New Roman;"><em>0</em></span>、<span style="font-family: Times New Roman;"><em>1</em></span>、<span style="font-family: Times New Roman;"><em>1</em></span>、<span style="font-family: Times New Roman;"><em>2</em></span>、<span style="font-family: Times New Roman;"><em>3</em></span>、<span style="font-family: Times New Roman;"><em>5</em></span>、<span style="font-family: Times New Roman;"><em>8</em></span>、<span style="font-family: Times New Roman;"><em>13</em></span>、<span style="font-family: Times New Roman;"><em>21</em></span>、<span style="font-family: Times New Roman;"><em>34</em></span>、<span style="font-family: Times New Roman;"><em>55</em></span>、<span style="font-family: Times New Roman;"><em>89</em></span>、⋯⋯。

下面的程式用以計算費式數列第 <span style="font-family: Times New Roman;"><em>N</em></span> 個（<span style="font-family: Times New Roman;"><em>N \ge 22</em></span>）數的數值：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 2 | </span><span class="n">b</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">N</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
<span style="color: silver;"> 4 | </span>    <span class="n">temp</span> <span class="o">=</span> <span class="n">b</span>
<span style="color: silver;"> 5 | </span>    <span class="n">__</span><span class="p">(</span><span class="n">a</span><span class="p">)</span><span class="n">__</span>
<span style="color: silver;"> 6 | </span>    <span class="n">a</span> <span class="o">=</span> <span class="n">temp</span>
<span style="color: silver;"> 7 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">__</span><span class="p">(</span><span class="n">b</span><span class="p">)</span><span class="n">__</span><span class="p">)</span>
</code></pre></div></code></pre></div>

請問  
`__(a)__` 與 `__(b)__` 兩個空格的敘述（statement）應該為何？

<select class="answer-select answer-inline" style="width: 600px"><option value="">請選擇...</option><option value="(a) f [i] = f [i - 1] + f [ i - 2]　　(b) f [N]">(a) f [i] = f [i - 1] + f [ i - 2]　　(b) f [N]</option><option value="(a) a = a + b 　　　　　　　　(b) a">(a) a = a + b 　　　　　　　　(b) a</option><option value="(a) b = a + b 　　　　　　　　(b) a">(a) b = a + b 　　　　　　　　(b) a</option><option value=" (a) f [i] = f [i - 1] +f [i - 2] 　 　(b) f [i]"> (a) f [i] = f [i - 1] +f [i - 2] 　 　(b) f [i]</option></select>

<b>提示：</b>

<div class="twocol-half" style="margin-top: 1em">
<div class="twocol-lefthalf">

<code>for</code> 迴圈 <code>range</code> 的括弧裡只有 1 個參數，

<ol>
<li>變數從 0 開始迭代，</li><br>
<li><code>range</code> 括弧裡的參數是變數迭代<span style="color:red"><b>不會到達</b></span>的值。</li>
</ol>

例如：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: #5d5d5d;"> 1 | </span><em><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">5</span><span class="p">):</span></em>
<span style="color: silver;"> 2 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
</code></pre></div></code></pre></div>
會輸出
<pre class="output">0
1
2
3
4</pre>

<code>i</code> 從 <code>0</code> 開始迭代

</div>
<div class="twocol-ritehalf">

<code>for</code> 迴圈 <code>range</code> 的括弧裡有 2 個參數，

<ol>
<li>第 1 個參數是變數<span style="color:red"><b>開始</b></span>迭代的值，</li><br>
<li>第 2 個參數是變數迭代<span style="color:red"><b>不會到達</b></span>的值。</li>
</ol>
<br>
例如：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: #5d5d5d;"> 1 | </span><em><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">):</span></em>
<span style="color: silver;"> 2 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
</code></pre></div></code></pre></div>
則會輸出
<pre class="output">2
3
4</pre>
<br><br>
<code>i</code> 從 <code>2</code> 開始迭代

</div>
</div>

《APCS 題本範例#7, 105/03#8》

---

程式

<div style="display: flex; margin-top: -1.2em; gap: 10px; margin-bottom: -1em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">X</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">10</span>
</code></pre></div></code></pre></div>

</div>
<div style="margin-top: 2em">

即

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">X</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span> <span class="p">]</span> <span class="c1"># 10 個</span>
</code></pre></div></code></pre></div>

</div>
</div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 2 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">10</span><span class="p">):</span>
<span style="color: silver;"> 3 | </span>    <span class="n">X</span> <span class="p">[(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span> <span class="o">%</span> <span class="mi">10</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
</code></pre></div></code></pre></div>

執行時，若輸入依序為整數 0, 1, 2, 3, 4, 5, 6, 7, 8, 9，則 X 最終為：<select class="answer-select answer-inline" style="width: 372px"><option value="">請選擇...</option><option value=""[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]">"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</option><option value="[2, 0, 2, 0, 2, 0, 2, 0, 2, 0]">[2, 0, 2, 0, 2, 0, 2, 0, 2, 0]</option><option value="[9, 0, 1, 2, 3, 4, 5, 6, 7, 8]">[9, 0, 1, 2, 3, 4, 5, 6, 7, 8]</option><option value="[8, 9, 0, 1, 2, 3, 4, 5, 6, 7]"">[8, 9, 0, 1, 2, 3, 4, 5, 6, 7]"</option></select>

《APCS 題本範例#25》

---

下面程式主要功能為：檢測 `d` 中最後一個數字是否為 6 個數字中最小的值。  
如果 `d` 中最後一個數字是 6 個數字中最小的值就印出 `1`，否則印出 `0`。

然而，這個程式是錯誤的。請問 `d` 如何設定即可以測試出程式有誤？

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><select class="answer-select answer-inline" style="width: 372px"><option value="">請選擇...</option><option value=""d = [ 11, 12, 13, 14, 15, 3 ]">"d = [ 11, 12, 13, 14, 15, 3 ]</option><option value="d = [ 11, 12, 13, 14, 25, 20 ]">d = [ 11, 12, 13, 14, 25, 20 ]</option><option value="d = [ 23, 15, 18, 20, 11, 12 ]">d = [ 23, 15, 18, 20, 11, 12 ]</option><option value="d = [ 18, 17, 19, 24, 15, 16 ]"">d = [ 18, 17, 19, 24, 15, 16 ]"</option></select>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">allBig</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">5</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="k">if</span> <span class="n">d</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">d</span> <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]:</span> 
<span style="color: silver;"> 6 | </span>        <span class="n">allBig</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 7 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;"> 8 | </span>        <span class="n">allBig</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 9 | </span>
<span style="color: silver;">10 | </span><span class="k">if</span> <span class="n">allBig</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
<span style="color: silver;">11 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># d [-1] 是最小</span>
<span style="color: silver;">12 | </span><span class="k">else</span><span class="p">:</span>
<span style="color: silver;">13 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="c1"># d [-1] 不是最小</span>
</code></pre></div></code></pre></div>

<b>提示</b>

`d [-1]` 即 `d` 最後一項、最後一個元素。此題程式中 `d` 共 6 項，所以 `d [-1]` 即 `d [5]`。

《APCS 105/03#17》

---

`A` 是一個可儲存 `n` 筆整數的 list，資料儲存於 `A［0`］~ `A［n - 1］`：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">A</span> <span class="o">=</span> <span class="p">[</span><span class="o">...</span><span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="n">p</span> <span class="o">=</span> <span class="n">q</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="k">if</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">p</span><span class="p">:</span>
<span style="color: silver;"> 6 | </span>        <span class="n">p</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span style="color: silver;"> 7 | </span>    <span class="k">if</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">q</span><span class="p">:</span>
<span style="color: silver;"> 8 | </span>        <span class="n">q</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span>
</code></pre></div></code></pre></div>

經過上面的程式碼運算後，<select class="answer-select answer-inline" style="width: 408px"><option value="">請選擇...</option><option value="p 是 list A 資料中的最大值">p 是 list A 資料中的最大值</option><option value="q 是 list A 資料中的最小值">q 是 list A 資料中的最小值</option><option value="q < p">q < p</option><option value="A [0] <= p">A [0] <= p</option></select> <b>不一定</b>正確。

<b>提示</b>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">p</span> <span class="o">=</span> <span class="n">q</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</code></pre></div></code></pre></div>

就是

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">p</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">q</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</code></pre></div></code></pre></div>

《APCS 題本範例#24, 106/03#5》

---

下面程式擬找出 list `A` 中的最大值 `M` 和最小值 `N`：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">M</span><span class="p">,</span> <span class="n">N</span><span class="p">,</span> <span class="n">s</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">101</span><span class="p">,</span> <span class="mi">3</span>
<span style="color: silver;"> 2 | </span><span class="n">A</span> <span class="o">=</span> <span class="p">[</span><span class="mi">80</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="mi">100</span><span class="p">]</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="p">:</span>
<span style="color: silver;"> 5 | </span>    <span class="k">if</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">M</span><span class="p">:</span>
<span style="color: silver;"> 6 | </span>        <span class="n">M</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span style="color: silver;"> 7 | </span>    <span class="k">elif</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">N</span><span class="p">:</span>
<span style="color: silver;"> 8 | </span>        <span class="n">N</span> <span class="o">=</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span style="color: silver;"> 9 | </span>
<span style="color: silver;">10 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">M</span><span class="p">,</span> <span class="n">N</span><span class="p">)</span>
</code></pre></div></code></pre></div>

不過這段程式碼有 bug！
請問A 初始值設定成 <select class="answer-select answer-inline" style="width: 168px"><option value="">請選擇...</option><option value=""[90, 80, 100]">"[90, 80, 100]</option><option value="[80, 90, 100]">[80, 90, 100]</option><option value="[100, 90, 80]">[100, 90, 80]</option><option value="[90, 100, 80]"">[90, 100, 80]"</option></select> 就可以測出程式有誤 😊

<b>提示</b>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">M</span><span class="p">,</span> <span class="n">N</span><span class="p">,</span> <span class="n">s</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">101</span><span class="p">,</span> <span class="mi">3</span>
</code></pre></div></code></pre></div>

就是

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">M</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">101</span>
<span class="n">s</span> <span class="o">=</span> <span class="mi">3</span>
</code></pre></div></code></pre></div>

《APCS 題本範例#29, 106/03#19》

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">arr</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="nb">sum</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">9</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="nb">sum</span> <span class="o">=</span> <span class="nb">sum</span> <span class="o">-</span> <span class="n">arr</span> <span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="n">arr</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="n">arr</span> <span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span>
<span style="color: silver;"> 6 | </span>
<span style="color: silver;"> 7 | </span><span class="nb">print</span> <span class="p">(</span><span class="nb">sum</span><span class="p">)</span>
</code></pre></div></code></pre></div>

輸出會是

<select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="44">44</option><option value="52">52</option><option value="54">54</option><option value="63">63</option></select>

《APCS 105/10#15》

---

程式

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">2</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="n">n</span> <span class="o">=</span> <span class="mi">9</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="n">n</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">a</span> <span class="p">[</span><span class="n">n</span> <span class="o">-</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">a</span> <span class="p">[</span><span class="n">n</span> <span class="o">-</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">],</span> <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span style="color: silver;"> 6 | </span>
<span style="color: silver;"> 7 | </span><span class="n">b</span> <span class="o">=</span> <span class="p">[]</span>
<span style="color: silver;"> 8 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="n">n</span><span class="o">//</span><span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
<span style="color: silver;"> 9 | </span>    <span class="n">b</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">])</span>
<span style="color: silver;">10 | </span>    <span class="n">b</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">a</span> <span class="p">[</span><span class="n">n</span> <span class="o">-</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">])</span>
</code></pre></div></code></pre></div>

執行後，  
`b` 會是

<select class="answer-select answer-inline" style="width: 372px"><option value="">請選擇...</option><option value=""[2, 4, 6, 8, 9, 7, 5, 3, 1, 9]">"[2, 4, 6, 8, 9, 7, 5, 3, 1, 9]</option><option value="[1, 3, 5, 7, 9, 2, 4, 6, 8, 9]">[1, 3, 5, 7, 9, 2, 4, 6, 8, 9]</option><option value="[1, 2, 3, 4, 5, 6, 7, 8, 9, 9]">[1, 2, 3, 4, 5, 6, 7, 8, 9, 9]</option><option value="[2, 4, 6, 8, 5, 1, 3, 7, 9, 9]"">[2, 4, 6, 8, 5, 1, 3, 7, 9, 9]"</option></select>

<b>提示：</b>

- `x, y = y, x`  
    會交換 `x` 和 `y` 的值。也就是
<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">tmp</span> <span class="o">=</span> <span class="n">x</span>
<span style="color: silver;"> 2 | </span><span class="n">x</span> <span class="o">=</span> <span class="n">y</span>
<span style="color: silver;"> 3 | </span><span class="n">y</span> <span class="o">=</span> <span class="n">tmp</span>
</code></pre></div></code></pre></div>  

- 若 `b` 是一個 list，  
    `b.append (x)`  
    會把 `x` 的值加入到 `b` 的最後面。例如
<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">b</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span> <span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="n">b</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span style="color: silver;"> 3 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">b</span><span class="p">)</span>
</code></pre></div></code></pre></div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;會輸出
<pre class="output">[1, 2, 3, 4]</pre>

《APCS 題本範例#15, 105/10#5》

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">101</span>
<span style="color: silver;"> 2 | </span><span class="n">b</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">101</span><span class="p">)]</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">101</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">b</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="n">a</span> <span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
<span style="color: silver;"> 6 | </span>
<span style="color: silver;"> 7 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">a</span> <span class="p">[</span><span class="mi">50</span><span class="p">]</span> <span class="o">-</span> <span class="n">a</span> <span class="p">[</span><span class="mi">30</span><span class="p">])</span>
</code></pre></div></code></pre></div>

會輸出 <select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="1275">1275</option><option value="20">20</option><option value="1000">1000</option><option value="810">810</option></select>

<b>提示</b>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">b</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">11</span><span class="p">)]</span>
</code></pre></div></code></pre></div>

就是

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">b</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">10</span> <span class="p">]</span>
</code></pre></div></code></pre></div>

《APCS 題本範例#30, 105/03#4》

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="n">a</span> <span class="o">=</span> <span class="p">[</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span> <span class="p">]</span>
<span class="n">n</span> <span class="o">=</span> <span class="mi">10</span>
<span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">ragne</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="n">a</span> <span class="p">[</span><span class="n">lindex</span><span class="p">]:</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">i</span>
</code></pre></div></code></pre></div>

輸出會是

<select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="1">1</option><option value="2">2</option><option value="7">7</option><option value="9">9</option></select>

《APCS 105/03#2》

---

執行

<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 20px; margin-top: -1.2em; margin-bottom: -1em; ">
<div style="flex: 1 1 1 40%; border-right: 1px solid #ccc padding-right: 10px;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">A</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">5</span>
<span style="color: silver;"> 2 | </span><span class="n">B</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">5</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">+</span> <span class="n">i</span><span class="o">*</span><span class="mi">4</span>
<span style="color: silver;"> 6 | </span>    <span class="n">B</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="o">*</span><span class="mi">5</span>
</code></pre></div></code></pre></div>

</div>
<div style="flex: 1 1 1 15%; margin-top: 5.5em;">

或

</div>
<div style="flex: 1 1 1 40%;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">A</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span style="color: silver;"> 2 | </span><span class="n">B</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">):</span>
<span style="color: silver;"> 5 | </span>    <span class="n">A</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="mi">2</span> <span class="o">+</span> <span class="n">i</span><span class="o">*</span><span class="mi">4</span><span class="p">)</span>
<span style="color: silver;"> 6 | </span>    <span class="n">B</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">i</span><span class="o">*</span><span class="mi">5</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
</div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 8 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 9 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">):</span>
<span style="color: silver;">10 | </span>    <span class="k">if</span> <span class="n">B</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">]:</span>
<span style="color: silver;">11 | </span>        <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="p">(</span><span class="n">B</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">%</span> <span class="n">A</span> <span class="p">[</span><span class="n">i</span><span class="p">])</span>
<span style="color: silver;">12 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;">13 | </span>        <span class="n">c</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;">14 | </span>
<span style="color: silver;">15 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

輸出會是

<select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="1">1</option><option value="4">4</option><option value="3">3</option><option value="33">33</option></select>

《APCS 105/03#9》

---

關於程式：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="mi">10000</span>
</code></pre></div></code></pre></div>

<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 20px; margin-top: -1.2em; margin-bottom: -1em; ">
<div style="flex: 1 1 1 40%; border-right: 1px solid #ccc padding-right: 10px;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 3 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">n</span>
<span style="color: silver;"> 4 | </span><span class="n">j</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 5 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="n">n</span><span class="p">):</span>
<span style="color: silver;"> 6 | </span>    <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">j</span> <span class="o">%</span> <span class="mi">20</span>
<span style="color: silver;"> 7 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">3</span>
</code></pre></div></code></pre></div>

</div>
<div style="flex: 1 1 1 15%; margin-top: 4.5em;">

或

</div>
<div style="flex: 1 1 1 40%;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 3 | </span><span class="n">a</span> <span class="o">=</span> <span class="p">[]</span>
<span style="color: silver;"> 4 | </span><span class="n">j</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 5 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="n">n</span><span class="p">):</span>
<span style="color: silver;"> 6 | </span>    <span class="n">a</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">j</span> <span class="o">%</span> <span class="mi">20</span><span class="p">)</span>
<span style="color: silver;"> 7 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">3</span>
</code></pre></div></code></pre></div>

</div>
</div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 9 | </span><span class="n">cnt</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;">10 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>
<span style="color: silver;">11 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
<span style="color: silver;">12 | </span>    <span class="k">if</span> <span class="n">a</span> <span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">11</span><span class="p">:</span>
<span style="color: silver;">13 | </span>        <span class="n">cnt</span> <span class="o">=</span> <span class="n">cnt</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">14 | </span>        <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <input type="text" class="answer-input answer-inline"> <span class="c1"># 框框內應填什麼整數使最後 cnt 為 250</span>
<span style="color: silver;">15 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;">16 | </span>        <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">17 | </span>
<span style="color: silver;">18 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">cnt</span><span class="p">)</span>
</code></pre></div></code></pre></div>

`a [20]` 會是 <input type="text" class="answer-input answer-inline"> (填入整數)

`a` 中會有 <input type="text" class="answer-input answer-inline"> 個 11 (填入整數)

《APCS》

---

執行

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">Q</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">200</span>
<span style="color: silver;"> 2 | </span><span class="n">val</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 3 | </span><span class="n">count</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">head</span> <span class="o">=</span> <span class="n">tail</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 5 | </span>
<span style="color: silver;"> 6 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">31</span><span class="p">):</span>
<span style="color: silver;"> 7 | </span>    <span class="n">Q</span><span class="p">[</span><span class="n">tail</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span>
<span style="color: silver;"> 8 | </span>    <span class="n">tail</span> <span class="o">=</span> <span class="n">tail</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 9 | </span>
<span style="color: silver;">10 | </span><span class="k">while</span> <span class="n">tail</span> <span class="o">&gt;</span> <span class="n">head</span> <span class="o">+</span> <span class="mi">1</span><span class="p">:</span>
<span style="color: silver;">11 | </span>    <span class="n">val</span> <span class="o">=</span> <span class="n">Q</span><span class="p">[</span><span class="n">head</span><span class="p">]</span>
<span style="color: silver;">12 | </span>    <span class="n">head</span> <span class="o">=</span> <span class="n">head</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">13 | </span>    <span class="n">count</span> <span class="o">=</span> <span class="n">count</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">14 | </span>    <span class="k">if</span> <span class="n">count</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span>
<span style="color: silver;">15 | </span>        <span class="n">count</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;">16 | </span>        <span class="n">Q</span><span class="p">[</span><span class="n">tail</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span>
<span style="color: silver;">17 | </span>        <span class="n">tail</span> <span class="o">=</span> <span class="n">tail</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">18 | </span>
<span style="color: silver;">19 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">Q</span><span class="p">[</span><span class="n">head</span><span class="p">])</span>
</code></pre></div></code></pre></div>

的輸出會是：

<select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="9">9</option><option value="18">18</option><option value="27">27</option><option value="30">30</option></select>

《APCS 題本範例#4》

---

下面這段程式的規格設定是是找到 list `A` 之中大於輸入值 `x` 的最小值：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">A</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">14</span><span class="p">]</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">x</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span> <span class="c1"># 輸入 x</span>
<span style="color: silver;"> 4 | </span>
<span style="color: silver;"> 5 | </span><span class="n">high</span> <span class="o">=</span> <span class="mi">7</span>
<span style="color: silver;"> 6 | </span><span class="n">low</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="k">while</span> <span class="n">high</span> <span class="o">&gt;</span> <span class="n">low</span><span class="p">:</span>
<span style="color: silver;"> 9 | </span>    <span class="n">mid</span> <span class="o">=</span> <span class="p">(</span><span class="n">high</span> <span class="o">+</span> <span class="n">low</span><span class="p">)</span> <span class="o">//</span> <span class="mi">2</span>
<span style="color: silver;">10 | </span>    <span class="k">if</span> <span class="n">A</span><span class="p">[</span><span class="n">mid</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="n">x</span><span class="p">:</span>
<span style="color: silver;">11 | </span>        <span class="n">low</span> <span class="o">=</span> <span class="n">mid</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;">12 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;">13 | </span>        <span class="n">high</span> <span class="o">=</span> <span class="n">mid</span>
<span style="color: silver;">14 | </span>
<span style="color: silver;">15 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">A</span><span class="p">[</span><span class="n">high</span><span class="p">])</span>
</code></pre></div></code></pre></div>

可是程式有 bug！
`x` 輸入為 <select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="-1">-1</option><option value="0">0</option><option value="10">10</option><option value="16">16</option></select> 則可測出程式有誤 😊

《APCS 題本範例#22》

---

## 📘 總結

---

## ⚠️ 重要提醒：

List 的索引<b>從 <span style="color:red">0</span> 開始</b>。

<span style="color: rgba(170, 170, 170, 1); font-weight: bold; font-size: 1.2em">2025 © Elton Huang</span>
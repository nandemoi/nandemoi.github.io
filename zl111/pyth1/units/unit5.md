<link rel="stylesheet" href="../assets/css/works_inline.css">
# 單元 5：程式流程結構綜整練習

## 🎯 學習重點

- 程式流程結構重點整理
    - 循序結構、選擇結構、重複結構
    - 程式區塊
    - `while` 和 `if` 流程結構比較

- `while`-`if` 結合使用

---

## 🗂️ 程式流程重點整理

到這裡我們學習了：

- 最簡單的程式依照書寫的順序一條命令接著一條命令執行

- `if`-`elif`-`else` 程式可以有分支的流程結構，但如何在看似一直線的 (linear) 的文本書寫來表示分岔的流程，Python 利用冒號 `:` 和<span style="color:red">**縮排**</span>來表示結構意義。

- 而這裡你也要開始能夠把一段程式看成一整個區塊：

    - 一整個完整的 `if`-(`elif`)-`else` 結構要看成一段程式區塊。
  
    - 把 `if ...:`、`elif ...:`、`else:` 以及 `for ...:` 和 `while ...:` 等前半句說完的後半句接在下面寫必須<span style="color:red">**縮排**</span>常常不會只有一條命令，而是整個程式區塊。
     
        這整段程式區塊或者開頭對齊，或者視需要<span style="color:red">**往右縮排**</span>。但整個區塊中任何一條命令的開頭絕不會比開始那條命令的開頭向左突出；如果突出，那就不是屬於那個程式區塊，不屬於那後半句，而是那個 `if`-`elif`-`else`、`for` 或 `while` 結構整句話做完後要接著做的事了。

- `for` 和 `while` 迴圈用來表示重複迭代的流程運作，也是利用<span style="color:red">**縮排/區塊**</span>表達結構意義。

---

### 整個結構看成一個區塊 ...


<div style="display: flex; gap: 20px; margin: 17px 0; align-items: flex-start;">
  <div style="width: 215px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <code>if ...:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 120px; margin-left: 34px">
        </div>
  </div>
  <div style="width: 215px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <code>if ...:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 60px; margin-left: 34px">
        </div>
    <code>else:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 60px; margin-left: 34px">
        </div>
  </div>
  <div style="width: 215px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <code>if ...:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 40px; margin-left: 34px">
        </div>
    <code>elif ...:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 40px; margin-left: 34px">
        </div>
    <code>else:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 40px; margin-left: 34px">
        </div>
  </div>
</div>


<div style="display: flex; gap: 20px; margin: 17px 0; align-items: flex-start;">
  <div style="width: 215px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <code>for ...:</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 120px; margin-left: 34px">
        </div>
  </div>
  <div style="width: 215px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <code>... # 初始條件設定</code><br>
    <code>while ...: # 檢查條件狀態</code><br>
        <div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 115px; margin-left: 34px">
        <br><br><br><code>... # 條件改變</code>
        </div>
  </div>
</div>

### 後半句是區塊

<div style="display: flex">
上面的
<div style="width: 160px; background-color: lightgray; padding: 10px; box-sizing: border-box; height: 120px; margin-left: 5px; margin-right: 5px">
  </div><br><br><br><br><br>
可能會長成這樣：
</div>

<div style="display: flex; gap: 20px; margin: 17px 0;">
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
  </div>
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
  </div>
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
  </div>
</div>

<div style="display: flex; gap: 20px; margin: 17px 0;">
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
  </div>
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
  </div>
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 50px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 50px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 50px;"></div>
  </div>
</div>

但<span style="color:red"><b>絕不會</b></span>長這樣：

<div style="display: flex">
  <div style="width: 160px; border: 2px dashed lightgray; padding: 10px; box-sizing: border-box;">
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px; margin-left: 25px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
    <div style="height: 12px; background-color: darkgray; margin-bottom: 5px;"></div>
  </div>
  <span style="color:red; margin-left: 8px; margin-top: 1.2em;"><br><br>&larr; 這句開始<b>不會</b>屬於同一個區塊</span><span style="margin-top: 1.2em;"><br><br>，而會是上段結構做完後要做的事</span> 
</div>

---

### `while` 和 `if` 流程比較

<div style="display: flex; gap: 20px; margin-top: -0.7em; ">
<div style="flex: 1 1 47.5%; border-right: 1px solid #ccc padding-right: 10px;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: #5d5d5d;"> 0 | </span><em><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span></em>
<span style="color: #5d5d5d;"> 1 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">3</span><span class="p">:</span></em>
<span style="color: #5d5d5d;"> 2 | </span><em>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span></em>
<span style="color: #5d5d5d;"> 3 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;"> 4 | </span><span class="nb">print</span> <span class="p">(</span><span class="mi">999</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<img src="../images/unit5_1.svg" alt="Graph" style="max-width: 100%; height: auto;">

</div>
<div style="flex: 1 1 47.5%;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 0 | </span><span class="n">i</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: #5d5d5d;"> 1 | </span><em><span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">3</span><span class="p">:</span></em>
<span style="color: #5d5d5d;"> 2 | </span><em>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span></em>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="nb">print</span> <span class="p">(</span><span class="mi">999</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<br>

<img src="../images/unit5_2.svg" alt="Graph" style="max-width: 100%; height: auto;">

</div>
</div>

<img src="https://nandemoi.github.io/zl111/media/while2.gif" alt="while2" style="width:100%;" loading="lazy"/>

認識理解迴圈的運作並能靈活應用的關鍵在於對執行時每一個步驟的變數變化都有清楚且詳細的意識。同學試著了解或練習時不要怕麻煩，要<span style="color:red">**拿出紙筆**</span>來做像上面動畫這樣樣的操作練習。

程式中迴圈的設計掌握 3 個重點：

1. 條件的開始

2. 條件的改變

3. 條件的結束<span style="color:red">**/持續**</span>，但記得 `while ...:` 所描述的是迴圈<span style="color:red">**持續**</span>的條件，也就是邏輯上是<span style="color:red">**相反**</span>的。

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="o">...</span>           <span class="c1"># 1. 條件的開始</span>
<span class="k">while</span> <span class="o">...</span><span class="p">:</span>    <span class="c1"># 3. 迴圈持續的條件</span>
    <span class="o">...</span>       <span class="c1"># 2.     條件的改變</span>
</code></pre></div></code></pre></div>

## ⚙️ `if` 結構放在迴圈結構的後半句中使用

至此，這 3 種結構：循序、選擇 (`if`)、和重複 (迴圈) 綜整使用，你可以讓電腦做任何的事情。你在設計程式的過程，要持續有意識地保持以程式區塊思考的概念：

- 整個程式是最外層、最大的區塊，裡面可以分成幾段按照順序執行的第二層區塊，

- 每個區塊可以是 `if` (-`elif`-`else`) 結構或迴圈 (`for` 或 `while`) 結構

- `if` 結構或迴圈結構的後半句作為一個區塊裡面又可以另ㄧ層或數層區塊，其中可以是 `if` 結構或迴圈結構。

程式區塊可以像俄羅斯套娃一樣層層包裹，而俄羅斯套娃是每層只有一隻，但程式每層可以超過一個區塊；另外要注意在同一層的程式區塊有前後執行的順序。

---

## 🧮 綜整練習

這段程式

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 2 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>    <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
<span style="color: silver;"> 5 | </span>       <span class="n">total</span> <span class="o">=</span> <span class="n">total</span> <span class="o">+</span> <span class="n">i</span>
<span style="color: silver;"> 6 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 7 | </span><span class="nb">print</span><span class="p">(</span><span class="n">total</span><span class="p">)</span>
</code></pre></div></code></pre></div>

和

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 2 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 3 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>    <span class="n">total</span> <span class="o">=</span> <span class="n">total</span> <span class="o">+</span> <span class="n">i</span>
<span style="color: silver;"> 5 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <input type="text" class="answer-input answer-inline">
<span style="color: silver;"> 6 | </span><span class="nb">print</span><span class="p">(</span><span class="n">total</span><span class="p">)</span>
</code></pre></div></code></pre></div>

執行輸出一樣。框框內應填入什麼**整數**

---

關於這段程式

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 2 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
<span style="color: silver;"> 3 | </span>    <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>        <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span>
<span style="color: silver;"> 5 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;"> 6 | </span>        <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 7 | </span><span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<select class="answer-select answer-inline" style="width: 288px"><option value="">請選擇...</option><option value="i 一直減到負數">i 一直減到負數</option><option value="i 一直加到 10">i 一直加到 10</option><option value="while 條件永遠成立">while 條件永遠成立</option></select> 為真。

---

執行這段程式：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 4 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span>
<span style="color: silver;"> 5 | </span>    <span class="k">if</span> <span class="n">n</span> <input type="text" class="answer-input answer-inline"> <span class="n">i</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c1"># 框框內應填入什麼運算符號</span>
<span style="color: silver;"> 6 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span> 
<span style="color: silver;"> 7 | </span>    <input type="text" class="answer-input answer-inline">
</code></pre></div></code></pre></div>

時，若

<table style="border-collapse: collapse; text-align: center;">
  <tr>
    <th style="border: 1px solid gray; padding: 3px 8px; text-align: left;">輸入 <code>n</code> 為</th>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">3</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">4</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">6</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">7</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">8</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">10</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">14</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">15</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">16</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">18</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">19</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; font-family: monospace;">20</td>
  </tr>
  <tr>
    <th style="border: 1px solid gray; padding: 3px 8px; text-align: left; vertical-align: top;">輸出</th>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>3</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>4</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>3<br>6</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>7</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>4<br>8</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>5<br>10</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>7<br>14</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>3<br>5<br>15</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>4<br>8<br>16</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>3<br>6<br>9<br>18</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>19</td>
    <td style="border: 1px solid gray; padding: 0 8px; text-align: right; vertical-align: top; font-family: monospace; line-height: 1.5;">1<br>2<br>4<br>5<br>10<br>20</td>
  </tr>
</table>

---

## 📝 APCS 觀念題選

以下選自 APCS 公開的觀念題。

APCS 觀念題測驗時無法執行程式，可以用紙筆操作。同學做這類的練習 (上面的也一樣) **不要**只照打程式看結果，那樣會失去意義。

這類練習的目的是希望你能去思考電腦根據 Python 程式所設計的意義會如何執行，是要確定你對 Python 如何表達流程邏輯的了解是正確的。

---

執行下段程式前 `a` 可能是任何整數值 ...

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="o">...</span>
<span class="k">while</span> <span class="n">a</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
    <span class="n">a</span> <span class="o">=</span> <span class="n">a</span> <span class="o">+</span> <span class="mi">5</span>
<span class="k">if</span> <span class="n">a</span> <span class="o">&lt;</span> <span class="mi">12</span><span class="p">:</span>
    <span class="n">a</span> <span class="o">=</span> <span class="n">a</span> <span class="o">+</span> <span class="mi">2</span>
<span class="k">if</span> <span class="n">a</span> <span class="o">&lt;=</span> <span class="mi">11</span><span class="p">:</span>
    <span class="n">a</span> <span class="o">=</span> <span class="mi">5</span>
</code></pre></div></code></pre></div>

這段程式中，<select class="answer-select answer-inline" style="width: 456px"><option value="">請選擇...</option><option value="a = a + 5 永遠不可能執行到">a = a + 5 永遠不可能執行到</option><option value="a = a + 2 永遠不可能執行到">a = a + 2 永遠不可能執行到</option><option value="a = 5 永遠不可能執行到">a = 5 永遠不可能執行到</option><option value="每ㄧ行 (line) 都可能執行得到">每ㄧ行 (line) 都可能執行得到</option></select>

《106/03, 題本範例#27》

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="mi">22</span>
<span style="color: silver;"> 2 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">n</span><span class="p">)</span>
<span style="color: silver;"> 3 | </span><span class="k">while</span> <span class="n">n</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>    <span class="k">if</span> <span class="n">n</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
<span style="color: silver;"> 5 | </span>        <span class="n">n</span> <span class="o">=</span> <span class="mi">3</span> <span class="o">*</span> <span class="n">n</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 6 | </span>    <span class="k">else</span><span class="p">:</span>
<span style="color: silver;"> 7 | </span>        <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">//</span> <span class="mi">2</span>
<span style="color: silver;"> 8 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">n</span><span class="p">)</span>
</code></pre></div></code></pre></div>

總共 print <input type="text" class="answer-input answer-inline"> 次。(填入整數)

《105/03#15》

---

## 💻 實作練習





    **提示：**

    `input()` 的作用是從使用者的輸入讀入還沒有讀入的下一整列。
    如果確定那一列裡面的字符只表示一個整數，就可以用 `int (input())` 把那串字符轉成整數 (`int`) 型別。
    
    而

    <div class="highlight"><pre><span></span><code><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span></code></pre></div>

    則是將轉換後的整數指定給 `n`。  
    
    如果放在迴圈裡：

    <div class="highlight"><pre><span></span><code><span class="k">while</span> <span class="o">...</span><span class="p">:</span>
        <span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
        <span class="o">...</span>
    </code></pre></div>

    就是在每個迴圈迭代都讀入還沒有讀入的下一列輸入資料  
    &emsp;&emsp;→ 轉換成整數型別的資料 → 指定給 `n`。

    因為比較複雜，所以都寫到提示裡，不過同學還是可以了解一下。

[更多實作練習](http://zerojudge.tw/)

---

## `break`

在迴圈結構的後半句區塊裡面用到 `if` 結構這類的程式模式當中 (`for` 或 `while` 迴圈包著 `if`)，有時候可以使用 `break` 來中斷它所在那層的迴圈。<span style="color:darkgray">不過這個指令如果不會也沒關係，對於寫程式的習慣而言可能還比較好。參考[提醒](#關於-break-的提醒)的說明</span>

我們看一下這個例子：它做的事是從 <span style="font-family: Times New Roman;"><em>1 × 1</em></span> 開始找 <span style="font-family: Times New Roman;"><em>100</em></span> 以內第一個大於 <span style="font-family: Times New Roman;"><em>50</em></span> 的平方數，如果有就印出來。

我們把迴圈搜尋的極至設在 `n * n < 100`，就用一個 `while` 迴圈從 `1*1` 開始一個一個檢查 ...

如果找到了，就不用再往上找了，我們可以用 `break` 中斷 `while` 迴圈：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 2 | </span><span class="k">while</span> <span class="n">n</span> <span class="o">*</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">100</span><span class="p">:</span>
<span style="color: silver;"> 3 | </span>    <span class="k">if</span> <span class="n">n</span> <span class="o">*</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">50</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">n</span> <span class="o">*</span> <span class="n">n</span><span class="p">)</span>
<span style="color: silver;"> 5 | </span>        <span class="k">break</span>
<span style="color: silver;"> 6 | </span>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">+</span> <span class="mi">1</span>
</code></pre></div></code></pre></div>

這裡請注意：

- 上面這段程式中 `if n * n > 50:` 的後半句是一個有 2 條程式的區塊，它們的<span style="color:red">**縮排**</span>是<span style="color:red">**對齊**</span>的。
    - `break` 會是它所在區塊的最後一條命令

- `break` 所中斷的是它所在那層的**迴圈**，而不是區塊，中斷區塊沒有意義，
    - 以上面那段程式而言，中斷了迴圈接著執行的是 line 7 的 `print (n)`，而<span style="color:red">**不會是**</span> line 6 的 `n = n + 1` 喔～～

- <span style="color:darkgray">以後你會用到迴圈包著迴圈 (超過一層的迴圈) 這樣的程式設計，<code>break</code> 所中斷的是它所在的那最裡面的一層！</span>

---

一個正整數 <span style="font-family: Times New Roman;"><em>n</em></span> 是不是質數的定義是 <span style="font-family: Times New Roman;"><em>n</em></span> 有沒有除了 <span style="font-family: Times New Roman;"><em>1</em></span> 和自己 (<span style="font-family: Times New Roman;"><em>n</em></span>) 以外的 <input type="text" class="answer-input answer-inline"> 數。  

檢查的程式可以這樣寫：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="o">...</span>
<span class="n">is_prime</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">i</span> <span class="o">=</span> <span class="mi">2</span>
<span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">n</span> <input type="text" class="answer-input answer-inline"> <span class="n">i</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c1"># 框框內應填入什麼運算符號？</span>
        <span class="n">is_prime</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">break</span>
    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>

<span class="c1"># 報告</span>
<span class="nb">print</span> <span class="p">(</span><span class="n">is_prime</span><span class="p">)</span>
</code></pre></div></code></pre></div>

如果 `n` 是質數印出 `1`，否則印出 `0`。

但是上面的 `while i < n:` 可以改成 `while i * i < n:` 會更快完成，因為[最多只要檢查到 <span style="font-family: Times New Roman;"><em>√n</em></span> 就可以了](https://www.youtube.com/watch?v=N5khW8NYxAc)！

---

框框內填入什麼**整數**會讓

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><input type="text" class="answer-input answer-inline"><span class="p">):</span>
<span style="color: silver;"> 2 | </span>    <span class="nb">print</span><span class="p">(</span><span class="mi">999</span><span class="p">)</span>
</code></pre></div></code></pre></div>

和

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
<span style="color: silver;"> 2 | </span>    <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span>
<span style="color: silver;"> 3 | </span>        <span class="k">break</span>
<span style="color: silver;"> 4 | </span>    <span class="nb">print</span><span class="p">(</span><span class="mi">999</span><span class="p">)</span>
</code></pre></div></code></pre></div>

有一樣的執行結果。

---

框框內填入什麼<b>正整數</b>？

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">9</span>
<span style="color: silver;"> 2 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&gt;</span> <input type="text" class="answer-input answer-inline"><span class="p">:</span>
<span style="color: silver;"> 3 | </span>    <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">5</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>        <span class="k">break</span>
<span style="color: silver;"> 5 | </span>    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span style="color: silver;"> 6 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span>
</code></pre></div></code></pre></div>

執行後會印出：

<pre class="output">9
8
7
6</pre>

---

這段程式

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 2 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="mi">10</span><span class="p">:</span>
<span style="color: silver;"> 3 | </span>    <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">3</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>        <span class="k">break</span>
<span style="color: silver;"> 5 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
</code></pre></div></code></pre></div>

最後執行的是 <select class="answer-select answer-inline" style="width: 105px"><option value="">請選擇...</option><option value="line 1">line 1</option><option value="line 2">line 2</option><option value="line 3">line 3</option><option value=" line 4"> line 4</option><option value=" line 5"> line 5</option></select>

---

### 關於 `break` 的提醒

`break` 在高中階段練習解題寫不會太複雜的程式用起來很方便。不過初學不學可能沒關係或者更好，在比較嚴肅的程式設計指導準則中一般是不建議使用，因為會破壞流程設計的完整性。以後工作的時候如果你的程式有 `break`，Code Review 時前輩或主管應該會說話。<br><br>比較好的習慣會是：想用 `break` 的地方試試看能用什麼邏輯條件或變數以原來就有的 `while` 判斷達成。例如：右邊會是比較好的寫法：

<div style="display: flex; gap: 20px; margin-top: -0.7em; ">
<div style="flex: 1 1 47.5%; border-right: 1px solid #ccc padding-right: 10px;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span>
<span style="color: silver;"> 2 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 3 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">100</span><span class="p">:</span>
<span style="color: silver;"> 4 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span style="color: silver;"> 5 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 6 | </span>    <span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: #5d5d5d;"> 7 | </span><em>    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">1234</span><span class="p">:</span></em>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="k">break</span></em>
<span style="color: silver;"> 9 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
<div style="flex: 1 1 47.5%;">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: #5d5d5d;"> 1 | </span><em><span class="n">go_on</span> <span class="o">=</span> <span class="mi">1</span></em>
<span style="color: silver;"> 2 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 3 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">100</span> <span class="ow">and</span> <span class="n">go_on</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></em>
<span style="color: silver;"> 4 | </span>    <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span style="color: silver;"> 5 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: silver;"> 6 | </span>    <span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: #5d5d5d;"> 7 | </span><em>    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">1234</span><span class="p">:</span></em>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">go_on</span> <span class="o">=</span> <span class="mi">0</span></em>
<span style="color: silver;"> 9 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
</div>

---

`break` 的作用是：<select class="answer-select answer-inline" style="width: 324px"><option value="">請選擇...</option><option value="讓條件變成 False">讓條件變成 False</option><option value="強制跳開目前的迴圈">強制跳開目前的迴圈</option><option value="讓變數歸零">讓變數歸零</option><option value="讓程式重新開始">讓程式重新開始</option></select>

為什麼嚴謹的程式設計準則通常不建議使用 break？<select class="answer-select answer-inline" style="width: 396px"><option value="">請選擇...</option><option value="會破壞流程設計的完整性">會破壞流程設計的完整性</option><option value="會讓程式變慢">會讓程式變慢</option><option value="Python 不支援 break">Python 不支援 break</option><option value="break 只能在 for 迴圈使用">break 只能在 for 迴圈使用</option></select>

---

## 📘 總結

程式的執行流程主要可以分成三種基本型態：

1️⃣ 循序結構 (Sequential)：程式由上而下，依順序逐行執行。

2️⃣ 選擇結構 (Conditional)：`if`-`elif`-`else`  

- 根據條件「是否成立」決定要不要執行某些命令。
- 縮排區塊表示後半句。

3️⃣ 重複結構 (Loops / Iteration)：`for`、`while`  

- 重複執行一段程式 (縮排) 區塊，直到條件不成立或被強制中斷 (break)。

### 設計觀念

- `if` 結構控制要不要做。

- `while`、`for` 結構控制要重複幾次或重複到什麼時候。

    - `break` 提前離開重複。

在實際設計中，「條件」與「重複」常常會交錯出現。
例如要重複輸入直到符合條件、或在迴圈中根據不同條件做不同處理。

這些控制流程的組合，是程式邏輯的骨架。
能夠靈活運用它們，
就能讓程式不只是「照順序做事」，
而是能夠「根據情況思考、靈活反應」。

---

### <span style="color:silver">無窮迴圈</span>

<span style="color:silver">下面這兩段程式</span>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">while</span> <span class="n">__</span><span class="p">(</span><span class="n">a</span><span class="p">)</span><span class="n">__</span><span class="p">:</span>
    <span class="n">__</span><span class="p">(</span><span class="n">b</span><span class="p">)</span><span class="n">__</span>
</code></pre></div></code></pre></div>

<span style="color:silver">和</span>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">__</span><span class="p">(</span><span class="n">a</span><span class="p">)</span><span class="n">__</span><span class="p">:</span>
        <span class="k">break</span>
    <span class="n">__</span><span class="p">(</span><span class="n">b</span><span class="p">)</span><span class="n">__</span>
</code></pre></div></code></pre></div>

<p style="color:silver">

作用是一樣的。<br><br>

第二段是無窮迴圈裡面有一個條件判斷的後半句是 <code>break</code> 中斷迴圈。<br><br>

以初學、練習解題而言，一般不會刻意使用無窮迴圈。不是實際應用上，像你的手機、以及你現在在操作的這個課程介面，本身都是無窮迴圈的應用。需要和使用者互動的應用，基本上使用的設計機制是在一個迴圈中「輪詢 Polling」<b><u>輪</u></b>流<b><u>詢</u></b>問看看哪個使用者有沒有點了哪個按鈕，或是輸入了什麼文字、點了哪個圖示。

</p>


<span style="color: rgba(170, 170, 170, 1); font-weight: bold; font-size: 1.2em">2025 © Elton Huang</span>
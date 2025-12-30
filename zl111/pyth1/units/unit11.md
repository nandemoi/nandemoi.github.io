<link rel="stylesheet" href="../assets/css/works_inline.css">

# 單元 11：(Time) Complexities (時間) 複雜度們

「時間複雜度」是衡量程式執行效率的一種方式。

衡量程式執行效率，我們在意的不是程式在處理小資料量時的快慢。程式 A 在處理小資料量的時候可能比程式 B 快，卻在大資料量的時候較慢，例如有序數列的循序搜尋和[二分搜尋](#二分搜尋完整分析)的比較。

我們在意的是：**當資料量變成 <span style='font-family: "Computer Modern"'><em>n</em></span> 倍的時候，程式處理需要花費的時間會是原來的幾倍？**

我們會使用一個 Big-O 的標記 <span class="arithmatex">\(O\)</span>(...) 來表示一個程式/演算法來表示效率的度量，這個效率的度量又稱為「複雜度 Complexity」。<span style="color:silver"><span class="arithmatex">\(O\)</span> 是從 <span style="font-family: Times">Order</span> 縮寫來的，可以理解成「等級」。</span>

通常會先關心執行的快慢，也就是「時間」複雜度 (Time Complexity)。<span style="color:silver">比較完整的討論也要考慮衡量記憶體使用的「空間」複雜度 (Space Complexity)。不過這裡我們先專注在前者。</span>

演算法的研究與開發經常使用的技巧之一是利用空間換取時間<span style="color:silver">；計算資源因為在設計結構上比較複雜，相對上比記憶資源稀缺</span>。

## (1st Order) Polynomial Time (一階) 多項式時間 (P)

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">acc</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 3 | </span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">acc</span> <span class="o">=</span> <span class="n">acc</span> <span class="o">+</span> <span class="n">n</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">-</span> <span class="mi">1</span></em>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">acc</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span style='font-family: "Times New Roman"'>O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">factorial</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">factorial</span> <span class="o">=</span> <span class="n">factorial</span> <span class="o">*</span> <span class="n">n</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">-</span> <span class="mi">1</span></em>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">factorial</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div style="display: grid; grid-template-columns: 40fr 7fr 53fr; gap: 5px; margin-bottom: -0.9em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">acc</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 3 | </span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">acc</span> <span class="o">=</span> <span class="n">acc</span> <span class="o">+</span> <span class="n">n</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">-</span> <span class="mi">1</span></em>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">acc</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
<div style="margin-top: 6em; text-align: center;">

比<br>較

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">factorial</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">factorial</span> <span class="o">=</span> <span class="n">factorial</span> <span class="o">*</span> <span class="n">n</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">-</span> <span class="mi">1</span></em>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">factorial</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
</div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">a1</span><span class="p">,</span> <span class="n">b1</span><span class="p">,</span> <span class="n">c1</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">a2</span><span class="p">,</span> <span class="n">b2</span><span class="p">,</span> <span class="n">c2</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 3 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 4 | </span>
<span style="color: silver;"> 5 | </span><span class="n">mx</span> <span class="o">=</span> <span class="o">-</span><span class="mi">9999999999</span>
<span style="color: silver;"> 6 | </span><span class="n">x1</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 7 | </span>
<span style="color: #5d5d5d;"> 8 | </span><em><span class="k">while</span> <span class="n">x1</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 9 | </span>    <span class="n">y1</span> <span class="o">=</span> <span class="n">a1</span> <span class="o">*</span> <span class="n">x1</span> <span class="o">*</span> <span class="n">x1</span> <span class="o">+</span> <span class="n">b1</span> <span class="o">*</span> <span class="n">x1</span> <span class="o">+</span> <span class="n">c1</span>
<span style="color: silver;">10 | </span>    <span class="n">x2</span> <span class="o">=</span> <span class="n">n</span> <span class="o">-</span> <span class="n">x1</span>
<span style="color: silver;">11 | </span>    <span class="n">y2</span> <span class="o">=</span> <span class="n">a2</span> <span class="o">*</span> <span class="n">x2</span> <span class="o">*</span> <span class="n">x2</span> <span class="o">+</span> <span class="n">b2</span> <span class="o">*</span> <span class="n">x2</span> <span class="o">+</span> <span class="n">c2</span>
<span style="color: silver;">12 | </span>    <span class="k">if</span> <span class="n">mx</span> <span class="o">&lt;</span> <span class="n">y1</span> <span class="o">+</span> <span class="n">y2</span><span class="p">:</span>
<span style="color: silver;">13 | </span>        <span class="n">mx</span> <span class="o">=</span> <span class="n">y1</span> <span class="o">+</span> <span class="n">y2</span>
<span style="color: #5d5d5d;">14 | </span><em>    <span class="n">x1</span> <span class="o">=</span> <span class="n">x1</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">15 | </span>
<span style="color: silver;">16 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">mx</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

## Various Variables

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span><span class="p">,</span> <span class="n">r</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">pnr</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">r</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">pnr</span> <span class="o">=</span> <span class="n">pnr</span> <span class="o">*</span> <span class="p">(</span><span class="n">n</span> <span class="o">-</span> <span class="n">i</span><span class="p">)</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;"> 7 | </span><span class="nb">print</span><span class="p">(</span><span class="n">pnr</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">m</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">m</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span> <span class="o">*</span> <span class="n">j</span><span class="p">)</span>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;"> 9 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="k">pass</span> <span class="c1"># or do something</span>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;"> 9 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div style="display: flex; gap: 20px">
<div style="flex: 1 1 47.5%">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">m</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">m</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span> <span class="o">*</span> <span class="n">j</span><span class="p">)</span>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;"> 9 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

</div>
<div style="flex: 1 1 47.5%">

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="k">pass</span> <span class="c1"># or do something</span>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;"> 9 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

</div>
</div>

---

## Logarithmic 對數的

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="k">while</span> <span class="n">n</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
<span style="color: #5d5d5d;"> 4 | </span><em>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">//</span> <span class="mi">2</span></em>
<span style="color: silver;"> 5 | </span>
<span style="color: silver;"> 6 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">n</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
<span style="color: silver;"> 5 | </span>    <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">*</span> <span class="mi">2</span></em>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div style="display: grid; grid-template-columns: 40fr 10fr 50fr; gap: 5px; margin-bottom: -0.9em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;"> 3 | </span><span class="k">while</span> <span class="n">n</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
<span style="color: silver;">   | </span><em></em>
<span style="color: #5d5d5d;"> 4 | </span><em>    <span class="n">n</span> <span class="o">=</span> <span class="n">n</span> <span class="o">//</span> <span class="mi">2</span></em>
<span style="color: silver;"> 5 | </span>
<span style="color: silver;"> 6 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">n</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
<div style="margin-top: 6em; text-align: center;">

比<br>較

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: silver;"> 3 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
<span style="color: silver;"> 5 | </span>    <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">*</span> <span class="mi">2</span></em>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
</div>

<span class="arithmatex">\(O(?)\)</span>

---

## 比較

<img src="https://nandemoi.github.io/zl111/media/cplx/simpchart.png" width="70%" style="display: block; margin-left: auto; margin-right: auto; margin-top: -2em;" loading="lazy">

---

## Nested

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span> </em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="k">pass</span> <span class="c1"># or do something</span>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;"> 9 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 6 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 7 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 8 | </span>        <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 9 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">*</span> <span class="mi">2</span></em>
<span style="color: #5d5d5d;">10 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">11 | </span>
<span style="color: silver;">12 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 6 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 7 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 8 | </span>        <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 9 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;">10 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">*</span> <span class="mi">2</span></em>
<span style="color: silver;">11 | </span>
<span style="color: silver;">12 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

<div style="display: grid; grid-template-columns: 45fr 7fr 48fr; gap: 5px; margin-bottom: -0.9em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 6 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 7 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 8 | </span>        <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 9 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">*</span> <span class="mi">2</span></em>
<span style="color: #5d5d5d;">10 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">11 | </span>
<span style="color: silver;">12 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
<div style="margin-top: 9em; text-align: center;">

比<br>較

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">c</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 6 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 7 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 8 | </span>        <span class="n">c</span> <span class="o">=</span> <span class="n">c</span> <span class="o">+</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 9 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;">10 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">*</span> <span class="mi">2</span></em>
<span style="color: silver;">11 | </span>
<span style="color: silver;">12 | </span><span class="nb">print</span> <span class="p">(</span><span class="n">c</span><span class="p">)</span>
</code></pre></div></code></pre></div>

</div>
</div>

<span class="arithmatex">\(O(?)\)</span>

---

## 非多項式時間 Non-polynomial Time

`exp (n)` 算出 { 1, 2, ..., n } 的子集合個數

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">def</span><span class="w"> </span><span class="nf">exp</span> <span class="p">(</span><span class="n">n</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;</span> <span class="n">n</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>  <span class="c1"># 1~n 都考慮的，算一個子集合</span>
    <span class="k">return</span> <span class="n">exp</span> <span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">+</span> <span class="n">exp</span> <span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>  <span class="c1"># 有和沒有</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

`fact_perm (a)` 算出 a 中元素所有可能排列會有幾種。

$n$ 是 `len(a)` (`a` 的長度)，即 `a` 有 $n$ 項元素。

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">def</span><span class="w"> </span><span class="nf">fact_perm</span> <span class="p">(</span><span class="n">a</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
    <span class="k">if</span> <span class="nb">len</span> <span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>  <span class="c1"># 一種排列</span>
    <span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="nb">len</span> <span class="p">(</span><span class="n">a</span><span class="p">)):</span>         <span class="c1"># 首有 n 個選擇 </span>
        <span class="n">b</span> <span class="o">=</span> <span class="n">a</span> <span class="p">[:</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="n">a</span> <span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">:]</span>           <span class="c1"># 餘項</span>
        <span class="n">total</span> <span class="o">=</span> <span class="n">total</span> <span class="o">+</span> <span class="n">fact_perm</span> <span class="p">(</span><span class="n">b</span><span class="p">)</span>     <span class="c1"># 遞迴少了首項</span>
    <span class="k">return</span> <span class="n">total</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

## All Chart

<img src="https://nandemoi.github.io/zl111/media/cplx/allfs.png" width="100%" style="display: block; margin-left: auto; margin-right: auto; margin-top: -1em;" loading="lazy">

---

對數尺度 Log/logarithmic Scale

<img src="https://nandemoi.github.io/zl111/media/cplx/alllogs.png" width="100%" style="display: block; margin-left: auto; margin-right: auto; margin-top: -.5em;" loading="lazy">

---

## 《費波那契數列 (Fibonacci Sequence)》

<div style="display: grid; grid-template-columns: 45fr 5fr 50fr; gap: 10px; margin-top: -0.85em; margin-bottom: 1.2em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">def</span><span class="w"> </span><span class="nf">fib_recr</span> <span class="p">(</span><span class="n">n</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>
    <span class="k">elif</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">fib_rec</span> <span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> \
             <span class="o">+</span> <span class="n">fib_rec</span> <span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">2</span><span class="p">)</span>

　            
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

</div>
<div style="margin-top: 8em; text-align: center;">

vs.

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">def</span><span class="w"> </span><span class="nf">fib_iter</span> <span class="p">(</span><span class="n">n</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>
    <span class="k">elif</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="c1"># F (1), F (2)</span>
        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
            <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>  
        <span class="k">return</span> <span class="n">b</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

</div>
</div>

---

`fib_recr (n)` 直接從[定義](https://openhome.cc/zh-tw/algorithm/basics/fibonacci/)用遞迴的方式算出費式數列第 `n` 項：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">def</span><span class="w"> </span><span class="nf">fib_recr</span> <span class="p">(</span><span class="n">n</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>
    <span class="k">elif</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">fib_rec</span> <span class="p">(</span><span class="n">n</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="o">+</span> <span class="n">fib_rec</span> <span class="p">(</span><span class="n">n</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)</span>
</code></pre></div></code></pre></div>

這個做法的問題是會有很多重複的動作：以求 $F (7)$ 為例

<blockquote>
<p><span class="arithmatex">\(F (7) = F (6) + \)</span><span class="arithmatex" style="color: red">\(F (5)\)</span></span></p>
<p><span class="arithmatex">\(F (6) = \)</span>&nbsp;<span class="arithmatex" style="color: red">\(F (5)\)</span><span class="arithmatex">\( + F (4)\)</span></p>
</blockquote>

這表示 `fib_recr(5)` 會被重複執行，而每次執行 `fib_recr(5)` 又會重複執行 `fib_rec(3)` 等等 ....

<img src="../images/unit11_1.svg" alt="Graph" style="max-width: 100%; height: auto;">

<span class="arithmatex">\(O(?)\)</span> ($1 \lt k \lt 2$)

---

`fib_iter (n)` 則使用迭代／動態規劃 (Dynamic Programming)：

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span class="k">def</span><span class="w"> </span><span class="nf">fib_iter</span> <span class="p">(</span><span class="n">n</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>
    <span class="k">elif</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>  <span class="c1"># a = F(1), b = F(2)</span>
        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
            <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>  <span class="c1"># 進一階：新的 b 為前兩項之和</span>
        <span class="k">return</span> <span class="n">b</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

## 《大衛牧羊》

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span> <span class="o">=</span> <span class="nb">int</span> <span class="p">(</span><span class="nb">input</span> <span class="p">())</span>
<span style="color: silver;"> 2 | </span>
<span style="color: silver;"> 3 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 4 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span> </em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="k">pass</span> <span class="c1"># or do something</span>
<span style="color: #5d5d5d;"> 8 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: #5d5d5d;"> 9 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

[題目](/prac1/p6-5)

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span><span class="p">,</span> <span class="n">m</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">backs</span> <span class="o">=</span> <span class="nb">list</span> <span class="p">(</span><span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()))</span>
</code></pre></div></code></pre></div>

<div style="display: grid; grid-template-columns: 45fr 5fr 50fr; gap: 10px; margin-top: -0.85em; margin-bottom: 1.2em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;">   | </span>　
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">if</span> <span class="n">i</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">backs</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: #5d5d5d;"> 8 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

</div>
<div style="margin-top: 10.5em; text-align: center;">

vs.

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 4 | </span><span class="c1"># 有回來的先一個一個登記到點名表</span>
<span style="color: silver;"> 5 | </span><span class="n">board</span> <span class="o">=</span> <span class="p">[</span> <span class="kc">False</span> <span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> 
<span style="color: silver;"> 6 | </span><span class="c1"># (題目說羊隻編號從 1 開始)</span>
<span style="color: silver;"> 7 | </span>
<span style="color: silver;"> 8 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 9 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">m</span><span class="p">:</span></em>
<span style="color: silver;">10 | </span>    <span class="n">board</span> <span class="p">[</span><span class="n">backs</span> <span class="p">[</span><span class="n">i</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">True</span>
<span style="color: #5d5d5d;">11 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">12 | </span>
<span style="color: silver;">13 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;">14 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;">15 | </span>    <span class="k">if</span> <span class="ow">not</span> <span class="n">board</span> <span class="p">[</span><span class="n">i</span><span class="p">]:</span>
<span style="color: silver;">16 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: #5d5d5d;">17 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

</div>
</div>

---

<a href="https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python" target="_blank"><code>in</code> 的複雜度是 <span class="arithmatex">\(O(n)\)</span></a>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span><span class="p">,</span> <span class="n">m</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">backs</span> <span class="o">=</span> <span class="nb">list</span> <span class="p">(</span><span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()))</span>
</code></pre></div></code></pre></div>

<div style="display: grid; grid-template-columns: 45fr 5fr 50fr; gap: 10px; margin-top: -1em; margin-bottom: -0.8em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;">   | </span>　
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;">   | </span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">if</span> <span class="n">i</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">backs</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: #5d5d5d;"> 8 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

</div>
<div style="margin-top: 10.5em; text-align: center;">

<span class="arithmatex">\(\approx\)</span>

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: #5d5d5d;"> 4 | </span><em><span class="k">def</span><span class="w"> </span><span class="nf">myIn</span> <span class="p">(</span><span class="n">who</span><span class="p">,</span> <span class="n">backlist</span><span class="p">,</span> <span class="n">m</span><span class="p">):</span></em>
<span style="color: silver;"> 5 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">m</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="n">backs</span> <span class="p">[</span><span class="n">j</span><span class="p">]:</span>
<span style="color: silver;"> 8 | </span>            <span class="k">return</span> <span class="kc">True</span>
<span style="color: #5d5d5d;"> 9 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">10 | </span>    <span class="k">return</span> <span class="kc">False</span>
<span style="color: silver;">11 | </span>
<span style="color: silver;">12 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;">13 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: #5d5d5d;">14 | </span><em>    <span class="k">if</span> <span class="ow">not</span> <span class="n">myIn</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">backs</span><span class="p">,</span> <span class="n">m</span><span class="p">):</span></em>
<span style="color: silver;">15 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: #5d5d5d;">16 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

</div>
</div>

或

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span><span class="p">,</span> <span class="n">m</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">backs</span> <span class="o">=</span> <span class="nb">list</span> <span class="p">(</span><span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()))</span>
</code></pre></div></code></pre></div>

<div style="display: grid; grid-template-columns: 45fr 5fr 50fr; gap: 10px; margin-top: -1em; ">
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: silver;">   | </span><em></em>
<span style="color: #5d5d5d;"> 6 | </span><em>    <span class="k">if</span> <span class="n">i</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">backs</span><span class="p">:</span></em>
<span style="color: silver;"> 7 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: silver;">   | </span><em></em>
<span style="color: #5d5d5d;"> 8 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

</div>
<div style="margin-top: 11.25em; text-align: center;">

<span class="arithmatex">\(\approx\)</span>

</div>
<div>

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 4 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;"> 5 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;"> 6 | </span>    <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: silver;"> 7 | </span>    <span class="n">bBack</span> <span class="o">=</span> <span class="kc">False</span>
<span style="color: #5d5d5d;"> 8 | </span><em>    <span class="k">while</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">m</span><span class="p">:</span></em>
<span style="color: silver;"> 9 | </span>        <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="n">backs</span> <span class="p">[</span><span class="n">j</span><span class="p">]:</span>
<span style="color: silver;">10 | </span>            <span class="n">bBack</span> <span class="o">=</span> <span class="kc">True</span>
<span style="color: silver;">11 | </span>            <span class="k">break</span>
<span style="color: #5d5d5d;">12 | </span><em>        <span class="n">j</span> <span class="o">=</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">13 | </span>
<span style="color: silver;">14 | </span>    <span class="k">if</span> <span class="ow">not</span> <span class="n">bBack</span><span class="p">:</span>
<span style="color: silver;">15 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: silver;">16 | </span>
<span style="color: #5d5d5d;">17 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
</code></pre></div></code></pre></div>

</div>
</div>

<span class="arithmatex">\(O(?)\)</span>

---

<div class="highlight"><pre><span></span><code><div class="highlight"><pre><span></span><code><span style="color: silver;"> 1 | </span><span class="n">n</span><span class="p">,</span> <span class="n">m</span> <span class="o">=</span> <span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span style="color: silver;"> 2 | </span><span class="n">backs</span> <span class="o">=</span> <span class="nb">list</span> <span class="p">(</span><span class="nb">map</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">input</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()))</span>
<span style="color: silver;"> 3 | </span>
<span style="color: silver;"> 4 | </span><span class="c1"># 有回來的先一個一個登記到點名表</span>
<span style="color: silver;"> 5 | </span><span class="n">board</span> <span class="o">=</span> <span class="p">[</span> <span class="kc">False</span> <span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="c1"># 羊隻編號從 1 開始但 board 的索引序號會從 0 開始</span>
<span style="color: silver;"> 6 | </span>
<span style="color: silver;"> 7 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span style="color: #5d5d5d;"> 8 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">m</span><span class="p">:</span></em>
<span style="color: silver;"> 9 | </span>    <span class="n">board</span> <span class="p">[</span><span class="n">backs</span> <span class="p">[</span><span class="n">i</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">True</span>
<span style="color: #5d5d5d;">10 | </span><em>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></em>
<span style="color: silver;">11 | </span>
<span style="color: silver;">12 | </span><span class="n">i</span> <span class="o">=</span> <span class="mi">1</span>
<span style="color: #5d5d5d;">13 | </span><em><span class="k">while</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">n</span><span class="p">:</span></em>
<span style="color: silver;">14 | </span>    <span class="k">if</span> <span class="ow">not</span> <span class="n">board</span> <span class="p">[</span><span class="n">i</span><span class="p">]:</span>
<span style="color: silver;">15 | </span>        <span class="nb">print</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span style="color: silver;">16 | </span>    <span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
</code></pre></div></code></pre></div>

<span class="arithmatex">\(O(?)\)</span>

---

### 比較

<img src="https://nandemoi.github.io/zl111/media/cplx/shepardchart.png" width="70%" style="display: block; margin-left: auto; margin-right: auto; margin-top: -2em;" loading="lazy">

---


<span style="color: rgba(170, 170, 170, 1); font-weight: bold; font-size: 1.2em">2025 © Elton Huang</span>

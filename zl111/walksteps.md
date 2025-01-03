# 行走機構完成步驟

轉動結合：
* 一樓天花板接二樓地板
* 一樓地板和二樓地板不在同一層平面
* 一樓天花板接不到三樓地板

[參考影片](https://youtube.com/shorts/H1iwLd8_MyQ?feature=share)<!--、[模型](https://cad.onshape.com/documents/4c110d09bdf5554a7430363d/w/c4e2f10b63d866876f8b7ca0/e/fdd9f35863b2bc35ee63c351?renderMode=0&uiState=656fe0be07e9a2349c6a81a0)-->

## 先做左腳

1. 做四個長度不同的桿件 (須決定固定件、主動件、從動件)
2. 將四個桿件組合成四連桿機構
3. 延伸下肢、延伸主動件的另一端

## 雙腳

1. 右腳和左腳鏡射對稱：可以用以下方法之一完成
   1. 同樣的四個桿件再組合成一個鏡射對稱的右腳
   2. 或是複製左腳翻轉兩次後會得到鏡射的右腳
   3. 更高級的做法是左腳組合成一個 Assembly，新增一個雙腳的 Assembly，插入左腳的 Assembly 兩次，翻轉其中一個兩次即得右腳
<br>
1. <span style="color: red">每隻腳都是一組<ins>**四連桿機構**</ins>，四根桿件中：
   * <ins>**固定件**</ins>固定不動
   * <ins>**主動件**</ins>會轉滿 360&deg; 
2. <span style="color: red">設計一連接零件 (不要用圓柱) 將左右腳的<ins>**固定件**</ins>以緊固結合的方式連接在一起
3. <span style="color: red">設計另一個連接零件 (不要用圓柱) 將左右腳的<ins>**主動件**</ins>以緊固結合的方式連接在一起</span> → 同步連動

注意：

1. 兩個<span style="color: red">連接零件的長度</span>要計算匹配
2. 緊固結合方孔比原孔來得合理，而且操作結合連接器的設定也比較容易  
3. <span style="color: red">確定各個桿件的性質 (固定件、主動件)</span>，連接雙腳時不要結合錯桿件
4. 主動件多出另一頭軸孔的目的：請不要做成**同手同腳**的跳躍機構

之前的參考影片：[第 1 版](https://www.youtube.com/watch?v=Lr9cCsh8WKs&authuser=0)、[第 2 版](https://youtube.com/shorts/2CAeg648HeE?feature=share&authuser=0)、[第 3 版](https://youtube.com/shorts/9pnYUpbbxhY?feature=share&authuser=0)
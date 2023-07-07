# Onshape 專題設計建議

## 專題設計要領 <!--([範例們](https://app.box.com/s/2h1j3wm1niglm4ny5te20254036ekts8))-->

* 你如果對要做什麼沒有想法，先從簡單的開始，例如：撲滿、骰子、各種加蓋子。或書寫回答以下問題
  - 想想看你或家人的生活中有什麼不方便的地方？你可以做個什麼樣的東西解決這個問題？
  - 或是你平常喜歡什麼美好的事物或看什麼動漫？你可以試著複製這些物品或是裡面的人物造型。
  - 試著先在紙上畫畫看。
* 可以隨參考教科書附的學習手札。
* 如果不知道怎麼開始畫草圖，可以先在紙上稍微畫一下輪廓，就會有想法了。
* 盡量利用重合共點、等長關係的限制條件，盡量不要設定尺寸，這樣要修改設計會比較容易  
* 美學要領：對稱、[黃金比](https://www.elegantthemes.com/blog/design/the-golden-ratio-the-ultimate-guide-to-understanding-and-using-it) ([費氏數列](https://youtu.be/2tv6Ej6JVhohttps://youtu.be/2tv6Ej6JVho))、質數  
* 多數的功能都在按滑鼠右鍵下拉的功能表裡例如隱藏/顯示 (所有) 零件、草圖、結合連接器等功能項目都在相應的表單區塊按右鍵下拉功能表中  
* 結構設計考量限制零件的自由度 (三個軸向的平移與旋轉)
* 轉角的結構強度，圓角會比直角來得強 (例如：拱門結構)
* 你如果有想要完成怎麼樣的一套步驟，可以問老師，我可能把比較快的方法跟你講，或是給你一個方向

## [機構設計 Mechanism Design](https://nandemoi.github.io/zl111/Mech_Design.pdf)
課本第 4 章：機構。4-2 Ⓑ 四連桿

* 其他結合：轉動 (蓋子、機構)、相切 (凸輪)
    - [thắng 的機構設計](https://www.youtube.com/channel/UCli_RJkGWfZvw4IlDLHNCQg)
    - Disney's [Computational Design of Mechanical Characters](https://www.youtube.com/watch?v=DfznnKUwywQ)
    - [grippers](https://www.youtube.com/watch?v=YM2O3TufUlY)
* 齒輪
  * [Free Gear Generator](https://evolventdesign.com/pages/spur-gear-generator) 設定 Tooth Counts 齒數 → 
  "Download DXF" → 
  Onshape 左下角「+」匯入 → 
  編輯草圖：「插入 DXF」工具
  * [Onshape How To: Gears](https://www.youtube.com/watch?v=AxCgO_eJocc)
  * [齒輪技術入門篇](https://www.khkgears.co.jp/tw/gear_technology/pdf/gear_guide1.pdf)、[齒輪技術實用篇](https://www.khkgears.co.jp/tw/gear_technology/pdf/gear_guide2.pdf)

## 其他

* 結合連接器的
    - 移動
    - 重新對齊 (零件要先旋轉到大概的角度)
        1. 選副軸 (紅) 或 主軸 (藍)
        2. 點選零件上要對齊的圖元
* 版本、分支

#### 學習任何工具的原則

* 越厲害的工具解決更困難或複雜的問題越有效率，但是需要學習的成本
* 先確定基礎概念的認識，熟悉基本的操作，再學習進階

步調節奏自己拿捏，每個人狀況不一樣，但有時會有時間壓力

<!--
#### 製圖丙級檢定相關

製圖丙檢使用 Autodesk Inventor，學生應可申請教育用途免費使用一年，詳查網站

* 草圖可以畫在任何平面上
    1. 最初只有三個空間平面
    2. 有擠出零件後可畫在任何擠出零件的平面
    3. 擠出有「新 」、「移除」等 4 個選項。可以有第二結束位置 ([1-6](https://cad.onshape.com/documents/9249c2150d122e1502f1ed34/w/a4d15f37f689df1031355301/e/288c812cc62fa31f95ebfe11), [1-21](https://cad.onshape.com/documents/c6b1e35a65795c97c66802b2/w/0ff0667ea435dcce608790cf/e/998a91825e14f91f3e840a64))
* 旋轉、疊層拉伸 (放樣、loft)、[螺紋](https://cad.onshape.com/documents/c008ee8ea8cf3d37d94ef197/w/2c3761f6657c5655b858a0d7/e/59318cb525f0d3f451b6dc0c?renderMode=0&uiState=6361d99c52cea82f364af199)
    - [spring](https://www.youtube.com/watch?v=kvPe4xL_3tM): helix on a cylinder → hide cylinder (→ sweep with curve (not helix))  
    - [my turbine](https://cad.onshape.com/documents/6516990dfb7b111938482bcc/w/4816bf2c26d5c6e1b660a654/e/c9770ba1b9c090db5e21a4e7?renderMode=0&uiState=636476f1e931cd608134074e) (外圓和內多邊不能在同一個草圖), [turbine toturial](https://www.youtube.com/watch?v=L1OqJp5kW0U), [advanced blade](https://www.youtube.com/watch?v=DIfwAZwuAjE)
* [金字塔：(1-21) 3D 配適不規則曲線 （3D fit spline) + 疊層拉伸 (loft)](https://cad.onshape.com/documents/39a652e02f04760b3553b242/w/2e1123d31be357a511c37e43/e/559d40ee06e6a56e4d32811d)

Onshape 操作學習可參考趙珩宇等編著 &lt;動手入門 Onshape 3D 繪圖到機構製作&gt; 台科大圖書 2019。
-->

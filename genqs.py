import pandas as pd, subprocess

total = 99

def genstr (setdf):
    setstr = ""
    for _, row in setdf.iterrows():
        setstr += "({}, {}) ".format (row ['x'], row ['y']) 
    return setstr

def inCol (q, setdf, xy):
    for _, row in setdf.iterrows():
        q.write ('{}\n'.format (row [xy]))

def inColpdf (setdf, xy):
    ret = ""
    for _, row in setdf.iterrows():
        ret += '{} \\\\\n'.format (row [xy])
    return ret

def genlsvm (q, ti, cnt, i):
    q.write (f'第{ti}題 (5 分)：線性支持向量機\n\n')
    seta = pd.read_csv (f't23/{cnt:02d}T{i}A.csv', header=None)
    setb = pd.read_csv (f't23/{cnt:02d}T{i}B.csv', header=None)
    cand = pd.read_csv (f't23/{cnt:02d}T{i}C.csv', header=None)
    seta.columns, setb.columns, cand.columns = [ 'x', 'y' ], [ 'x', 'y' ], [ 'x', 'y' ]
    q.write ('A 集合兩點座標：{}\n'.format (genstr (seta)))
    q.write ('B 集合兩點座標：{}\n'.format (genstr (setb)))
    q.write ('測試點座標：({}, {})\n\n'.format (cand.iloc[0]['x'], cand.iloc[0]['y']))      
    q.write ('請找出適合 A、B 集合分類的線性支持向量機，依序回答：\n')
    q.write ('  (1) 測試點應屬 A 或 B 分類\n')
    q.write ('  (2) 線性支持向量機\n')
    q.write ('      (A) 與 A 集合兩點連線平行或\n')
    q.write ('      (B) 與 B 集合兩點連線平行或\n')
    q.write ('      (C) 是 A 與 B 最靠近兩點的中垂線？\n')
    q.write ('須交代理由、解題過程。\n')

def genlsvmpdf (tmpl, cnt, i):
    seta = pd.read_csv (f't23/{cnt:02d}T{i}A.csv', header=None)
    setb = pd.read_csv (f't23/{cnt:02d}T{i}B.csv', header=None)
    cand = pd.read_csv (f't23/{cnt:02d}T{i}C.csv', header=None)
    seta.columns, setb.columns, cand.columns = [ 'x', 'y' ], [ 'x', 'y' ], [ 'x', 'y' ]
    tmpl = tmpl.replace (f'\ASET{i}', genstr (seta))
    tmpl = tmpl.replace (f'\BSET{i}', genstr (setb))
    tmpl = tmpl.replace (f'\CAND{i}', f"{cand.iloc[0]['x']}, {cand.iloc[0]['y']}") 
    
    return tmpl

def genqtxt (cnt):
    with open  (f'qs/{cnt:02d}.txt', 'w') as q:
        q.write (f'試卷編號：{cnt:02d}\n共三題以大寫羅馬數字編碼\n注意閱讀卷尾如何繳交作答\n\n\n')
        q.write ('第 I 題 (5 分)：最短距離分類器、kNN 分類器\n\n')
        seta = pd.read_csv (f't1/{cnt:02d}MA.csv', header=None)
        setb = pd.read_csv (f't1/{cnt:02d}MB.csv', header=None)
        cand = pd.read_csv (f't1/{cnt:02d}MC.csv', header=None)
        seta.columns, setb.columns, cand.columns = [ 'x', 'y' ], [ 'x', 'y' ], [ 'x', 'y' ]
        q.write ('A 集合各點座標：{}\n'.format (genstr (seta)))
        q.write ('B 集合各點座標：{}\n'.format (genstr (setb)))
        q.write ('測試點座標：({}, {})\n\n'.format (cand.iloc[0]['x'], cand.iloc[0]['y']))      
        q.write ('請依序回答根據 (1) 最段距離分類器、(2) 1NN、(3) 3NN、(4) 5NN、(5) 7NN\n分別會將測試點分類為 A 或 B。須交代理由、解題過程。\n\n')  
        q.write ('以下以不同格式重複 A、B 兩集合座標：\n')
        q.write ('A 集合各點 x 座標依序為：\n')
        inCol (q, seta, 'x')
        q.write ('A 集合各點 y 座標依序為：\n')
        inCol (q, seta, 'y')
        q.write ('B 集合各點 x 座標依序為：\n')
        inCol (q, setb, 'x')
        q.write ('B 集合各點 y 座標依序為：\n')
        inCol (q, setb, 'y')
        q.write ('\n\n')
        genlsvm (q, ' II ', cnt, 1)
        q.write ('\n\n')
        genlsvm (q, ' III ', cnt, 2)
        q.write ('\n\n')
        q.write ('如何繳交作答：繳交至「機器學習」評量測驗的 Google Classroom 作業\n')
        q.write (f'以檔名為「編號{cnt:02d}」的 Google Doc 條列或列表或 Google Sheet 列表依序回答上述問題：\n')
        q.write (f'編號{cnt:02d}\n')
        q.write ('I   (1)\n')
        q.write ('    (2)\n')
        q.write ('    (3)\n')
        q.write ('    (4)\n')
        q.write ('    (5)\n')
        q.write ('II  (1)\n')
        q.write ('    (2)\n')
        q.write ('III (1)\n')
        q.write ('    (2)\n')
        q.write ('其他注意事項與需要繳交的資料詳閱 Google Classroom 作業說明\n')
        q.write ('所有電子檔案或連結繳交至 Google Classroom 作業\n')
        q.write ('紙筆計算寫上班級座號姓名繳交給老師\n\n')
        q.write ('加油！！！\n')

def genqpdf (cnt):
    with open('q.tex', 'r') as f:
        tmpl = f.read()
        tmpl = tmpl.replace ('\CNT', f'{cnt:02d}')
        seta = pd.read_csv (f't1/{cnt:02d}MA.csv', header=None)
        setb = pd.read_csv (f't1/{cnt:02d}MB.csv', header=None)
        cand = pd.read_csv (f't1/{cnt:02d}MC.csv', header=None)
        seta.columns, setb.columns, cand.columns = [ 'x', 'y' ], [ 'x', 'y' ], [ 'x', 'y' ]
        tmpl = tmpl.replace ('\ASET0', genstr (seta))
        tmpl = tmpl.replace ('\BSET0', genstr (setb))
        tmpl = tmpl.replace ('\CAND0', f"{cand.iloc[0]['x']}, {cand.iloc[0]['y']}")
        tmpl = tmpl.replace ('\SETA0X', inColpdf (seta, 'x'))
        tmpl = tmpl.replace ('\SETA0Y', inColpdf (seta, 'y'))
        tmpl = tmpl.replace ('\SETB0X', inColpdf (setb, 'x'))
        tmpl = tmpl.replace ('\SETB0Y', inColpdf (setb, 'y'))
        tmpl = genlsvmpdf (tmpl, cnt, 1)
        tmpl = genlsvmpdf (tmpl, cnt, 2)
        with open (f'temp.tex', 'w') as stex:
            stex.write (tmpl)
        subprocess.call (['pdflatex', 'temp.tex'])
        subprocess.call (['mv', 'temp.pdf', f'qs/{cnt:02d}q.pdf'])

for cnt in range (1, total + 1):
    # genqtxt (cnt)
    genqpdf (cnt)
    
subprocess.call (['open', f'qs/{cnt:02d}q.pdf'])
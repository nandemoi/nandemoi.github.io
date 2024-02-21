# 《APCS 容易題二》參考提示

## e286

入門版
```python
h11, h12, h13, h14 = map (int, input ().split ())
g11, g12, g13, g14 = map (int, input ().split ())
h21, h22, h23, h24 = map (int, input ().split ())
g21, g22, g23, g24 = map (int, input ().split ())
...
h1 = ...
g1 = ...
h2 = ...
g2 = ...
...
print (str (h1) + ":" + str (g1))
print (str (h2) + ":" + str (g2))
...
print ("...")
```

符合程度版
```python
h1scores = list (map (int, input ().split ()))
h2scores = list (map (int, input ().split ()))
g1scores = list (map (int, input ().split ()))
g2scores = list (map (int, input ().split ()))
...
h1total = ...
g1total = ...
h2total = ...
g2total = ...
...
print (str (h1total) + ":" + str (g1total))
print (str (h2total) + ":" + str (g2total))
...
print ("...")
```

## i399

```python
a1, a2, a3 = map (int, input ().split ())
...
print (...)
```
這題做法很多，有比較高級的做法。
不過如果以入門等級的做法來看，
因為輸入只會有 3 個數字，
所以你可以拿處理這 3 個數字的各種組合狀況來解題。
題目最後說依序輸出，
你可以看看是不是在什麼時間點做排序就可以讓後面的處理邏輯更簡單。

<!--

## m931

```python
n = int (input ())
all = []
while n > 0:
    a, d = map (int, input ().split ())
    all.append (...)
    n = n - 1
...
print (all [...])
```

-->
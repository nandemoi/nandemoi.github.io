# 參考提示

## a053, a799, c290 ([原題 PDF](https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2018/12/1060304APCSImplementation.pdf))

```python
n = int (input ())
...
print (...)
```

## d226

```python
v, t = map (int, input().split())
...
print (...)
```

## j286

```python
a, b, c = map (int, input().split())
...
print (...)
```

## f312

```python
a1, b1, c1 = map (int, input().split())
a2, b2, c2 = map (int, input().split())
n = int (input ())
...
print (...)
```

### Python 輸出以空格相隔的多個數字

在 ```print (...)``` 的括弧中把要輸出的數字<span style="color:red">或變數</span>依序以逗號分開，例如：

```python
a = 1
c = 3
print (a, 2, c)
```

就會在螢幕上輸出

```python
1 2 3
```

## j605

```python
k = int (input ())

while k > 0:
    t, s = map (int, input().split())
    ...
    k = k - 1
    
print (..., ...)
```

## i428 <span style="color:red">(此提示評量時會隱藏)</span>

題目補充：行進時間 ＝ 行進距離 × 1

```python
n = int (input())
x1, y1 = map (int, input().split()) # 讀入第一站的座標
xx, yy = map (int, input().split()) # 讀入下一站的座標

mxmx = abs (xx - x1) + abs (yy - y1) # 目前最大距離
mnmn = mxmx                          # 目前最小距離

for _ in range(2, n):
    nx, ny = map (int, input().split()) # 讀入下一站的座標
    ...
    xx = nx
    yy = ny
    
print (mxmx, mnmn)
```

## k731 <span style="color:red">(此提示評量時會隱藏)</span>

```python
n = int (input())
xx, yy = map (int, input().split()) # 讀入第一個的座標

ltc = 0 # 左轉計數
rtc = 0 # 右轉計數
utc = 0 # 迴轉計數

for _ in range(2, n):
    nx, ny = map (int, input().split()) # 讀入下一個的座標
    ...
    xx = nx
    yy = ny
    
print (ltc, rtc, utc)
```

### Python 輸出文字

把你要的文字放在 ```"..."``` 裡，然後整個連 "" 放在 ```print (...)``` 的括弧裡就可以了，例如：

```python
print ("hello world")
```

就會在螢幕上輸出

```python
hello world
```

## c294

[原題 PDF](https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2022/10/實作題_題型範例.pdf) (往下捲第 3 頁)

```python
a, b, c = map (int, input ().split())
...
print (...)
print ("...")
```

## [d587](https://officeguide.cc/python-sort-sorted-tutorial-examples/), b294

```python
n = int (input ())
nums = list (map (int, input().split()))
...
print (...)
```

## [d587](https://officeguide.cc/python-sort-sorted-tutorial-examples/)

```python
# alist 是一個 List, 下面這句程式把 alist 內容印出來，每個元素之間用一個空格分開
print (*alist) 
```

## b964

[原題 PDF](https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2022/10/實作題_題型範例.pdf)

```python
n = int (input ())
grades = list (map (int, input().split()))
...
print (...)
print (...)
print (...)
```

## b526

[Introduction to Priority Queues in Python](https://builtin.com/data-science/priority-queues-in-python)


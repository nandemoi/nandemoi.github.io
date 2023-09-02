# Python 重點整理

## [程式是什麼？寫程式要幹什麼？](https://nandemoi.github.io/zl111/prog.pdf)

## 輸出

要讓程式在螢幕上印出東西很簡單就是用```print (...)```。例如：

```python
print (3)
```

就會印出

```
3
```

我們的課程在一開始會先處理整數就好，如果要印出多個整數，彼此之間空一格，則用<b>逗號</b>將他們分開就可以了。例如

```python
print (1, 2, 3)
```

就會印出

```
1 2 3
```

## 輸入

前測的輸出入程式碼都有提示。你如果做了幾題可能就可以發現了以下規律：

1. 如果要輸入一個整數，就是

   ```python
   n = int (input ())
   ```

2. 如果要輸入已知會有幾個的多個整數，例如已知會有 3 個，就是

   ```python
   a, b, c = map (int, input().split())
   ```

3. 如果要輸入一串幾個都可以的整數串到一個 list，就是

   ```python
   nums = list (map (int, input().split()))
   ```

至於爲什麼這樣寫，等到了《函式》的部分會解釋，不過你也可以試著先找資料自學了解。  

可以先試著了解的是 Python 是 line-based，每次```input()```會從輸入裝置抓一列 (換行) 資料處理，而 C++ 則是 token-based，換行符號 (newline) 和空格等同屬[空白符號 (whitespace)](https://www.codesdope.com/cpp-gear-up/)，將其他符號串分成分成一個一個 token，可以用 std:cin 一一讀取。這個之後也是會解釋。

## 變數名稱

一個好的編程習慣其實不要使用過於簡短的變數名稱，最好是能一看就知道它代表什麼。

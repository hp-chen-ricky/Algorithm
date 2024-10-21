
# 最佳化演算法

這邊記錄一些演算法
- 二分法 (Bisection method)
- 牛頓法 (Newton's method)

## 二分法（Bisection method）: 
是一種方程式根的近似值求法。

### 演算法執行步驟

若要求已知函數 $f(x) = 0$ 的根 ($x$ 的解)，則 :
1. 先找出一個區間 $[a, b]$，使得 $f(a)$ 與 $f(b)$ 異號。根據勘根定理，這個區間內一定包含著方程式的根。
2. 求該區間的中點 $m=\frac{a+b}{2}$，並找出 $f(m)$ 的值。
3. 若 $f(m)$ 與 $f(a)$ 正負號相同則取 $[m, b]$ 為新的區間, 否則取 $[a, m]$。
4. 重複第2和第3步至理想精確度為止。

## 牛頓法 (Newton's method) : 
使用函數 $g(x)$ 的泰勒級數的前面幾項來尋找方程式 $g(x)=0$ 的根。

### 演算法執行步驟
1. 令初始值 $x^{0}$。
2. 計算函數值 $g(x^{0})$ 之切線，經切線方向與 $x$軸交於 $x^{1}$，其做為下一個疊代點。
3. 利用 $x^{1}$ 進行下一輪疊代。
4. 重複第2和第3步至理想精確度為止。

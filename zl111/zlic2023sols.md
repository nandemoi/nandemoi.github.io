# 中崙高中 2023 資訊學科能力競賽參考解答

## ZeroJudge《l491. pA. 圓仔的遊戲（一）》解

```c++
#include <bits/stdc++.h>
using namespace std;

int warps [64], n, s; 

int walk () {
    int nowat = 0;
    for (int i = 0; i < s; i++) {
        int steps;
        cin >> steps;
        nowat = warps [(nowat + steps) % n]; // 走 steps 步之後瞬間轉移
    }
    return nowat;
}

int odd_d (int nowat) { 
    return (nowat > n/2 ? n - nowat : nowat);
} // 如果超過中點，和原點的較近距離會是繞回去那段

int main () {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie (0);
    int p, q;
    cin >> n >> p >> q >> s;
    for (int i = 0; i < n; i++)
        cin >> warps [i]; // warps 是瞬間傳送的目的地
    int nowat1 = walk (); // 1 號玩家走完全部路程
    int nowat2 = walk (); // 2 號玩家走完全部路程
    
    if (n % 2 == 0) { // 圓盤有偶數個刻度
        int d1 = abs (nowat1 - n/2);
        int d2 = abs (nowat2 - n/2);
        if (d1 == d2)
            cout << 0 << " " << n/2 - d1 << "\n";
        else if (d1 > d2)
            cout << 1 << " " << n/2 - d1 << "\n";
        else
            cout << 2 << " " << n/2 - d2 << "\n";
    } else { // 圓盤有奇數個刻度
        int d1 = odd_d (nowat1);
        int d2 = odd_d (nowat2);
        if (d1 == d2)
            cout << 0 << " " << d1 << "\n";
        else if (d1 > d2)
            cout << 2 << " " << d2 << "\n";
        else
            cout << 1 << " " << d1 << "\n";
    }
    
    return 0;
}
```

## ZeroJudge《l532. pB. 容易版貪吃蛇》解

```c++
#include <bits/stdc++.h>
using namespace std;

const int mv [][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} }; // 右下左上
int area [64][64];
int dss [64];

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie (0);

    int n, r;
    cin >> n >> r;

    for (int i = 0; i < 2*r; ++i) {
        cin >> dss[i];
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> area[i][j];
        }
    }

    for (int i = 0; i < n + 2; i++) {  // wall
        area [i][0] = -1;
        area [i][n + 1] = -1;
        area [0][i] = -1;
        area [n + 1][i] = -1;
    }

    int nowat [] = {n / 2 + 1, n / 2 + 1};
    int trace = 0;
    int pts = 0;
    bool bGoOn = true;

    while (trace < 2*r && bGoOn) {
        int d = dss[trace]; // 方向
        int s = dss[trace + 1]; // 移幾格
        trace += 2;

        for (int i = 0; i < s; ++i) { // 一格一格移動
            nowat [0] += mv[d][0];
            nowat [1] += mv[d][1];
            if (area [nowat [0]][nowat [1]] == -1) { // wall
                bGoOn = false;
                break;
            } else {
                pts += area[nowat [0]][nowat [1]];
                area [nowat [0]][nowat [1]] = 0; // 吃到分數後該格分數歸 0
            }
        }
    }

    cout << pts << endl;

    return 0;
}
```

## ZeroJudge《l490. pC. 史萊姆王》解

```c++
#include <bits/stdc++.h>
using namespace std;

int slimes [1024];

int main () {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie (0);
    int n;
    while (cin >> n) {
        for (int i = 0; i < n; i++)
            cin >> slimes[i];
        int t = 0;
        sort (slimes, slimes + n);
        for (int i = 0; i < n - 1; i++) {
            int m = slimes [i] + slimes [i + 1];
            slimes [i + 1] = m;
            t += m;
            int j = i + 2;
            for (; j < n; j++) { // 把新合併後的史萊姆移到正確的排序位置
                if (slimes [j] < m) // 比新史萊姆小的都要往前移
                    slimes [j - 1] = slimes [j];
                else {
                    slimes [j - 1] = m;
                    break;
                }
            }
            if (j == n) // 所有尚未合併的史萊姆都比新史萊姆小
                slimes [n - 1] = m;
        }
        cout << t << "\n";
    }
}
```

這個解執行時間 35ms，有學長用 priority_queue 執行時間 29ms。

## ZeroJudge《l492. pD. 圓仔的遊戲（二）》解

```c++
#include <bits/stdc++.h>
using namespace std;

int warps [1000005];
bool yet_visited [1000005];

int main () {
    ios::sync_with_stdio (0); cin.tie (0); cout.tie (0);
    int n, p, q;
    while (cin >> n >> p >> q) {
        for (int i = 0; i < n; i++)
            cin >> warps [i];
        queue<int> breaths;
        int depths = 1;
        breaths.push (0); // 起始在原點
        breaths.push (-1); // 隔層
        fill_n (yet_visited, n, true);
        
        bool bReached = false;
        while (breaths.size () != 1) {
            int nowat = breaths.front ();
            breaths.pop ();
            if (nowat == -1) {
                depths++;
                breaths.push (-1);
            } else {
                int lf = warps [ (nowat + p) % n ];
                int rt = warps [ (nowat + q) % n ];
                if (lf == 0 or rt == 0) {
                    bReached = true;
                    break;
                } else {
                    if (yet_visited [lf]) { // lf 還沒走過
                        yet_visited [lf] = false;
                        breaths.push (lf);
                    }
                    if (yet_visited [rt]) { // rt 還沒走過
                        yet_visited [rt] = false;
                        breaths.push (rt);
                    }
                }
            }
        }
        
        if (bReached)
            cout << depths << "\n";
        else
            cout << -1 << "\n";
    }
}
```

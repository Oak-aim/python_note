# Python 学習ノート

## Pythonとは

* すばやく効果的にシステムを開発できる汎用プログラミング言語
* Script言語で開発しやすい
* ライブラリが豊富
* 機械学習・AI・統計解析・理学計算に強い
* コードの書き方が比較的統一されやすい

### 主な利用例

* Webサービス開発
* 機械学習・AI
* データ分析
* 自動化ツール

### Pythonを利用しているサービス

* Google
* YouTube
* Instagram
* Dropbox

---

# 基本データ型

| 型     | 説明           |
| ----- | ------------ |
| int   | 整数           |
| float | 浮動小数点数       |
| str   | 文字列          |
| bool  | True / False |

```python
a = 10          # int
b = 3.14        # float
c = "Python"    # str
d = True        # bool
```

---

# 演算子

## 算術演算子

```python
+   # 足し算
-   # 引き算
*   # 掛け算
/   # 割り算
//  # 整数除算
%   # 余り
**  # べき乗
```

### 例

```python
print(5 ** 2)
# 25
```

```python
print(-13 / 4)
# -3.25

print(-13 // 4)
# -4
```

---

## 比較演算子

```python
==
!=
<
>
<=
>=
in
not in
```

```python
s = "abc"

print("a" in s)
# True

print("d" not in s)
# True
```

---

## ブール演算子

### and

```python
a = 1 == 1
b = 1 >= 0

print(a and b)
# True
```

### or

```python
a = 1 < 0
b = 1 >= 1

print(a or b)
# True
```

### not

```python
a = 0 == 0

print(a)
# True

print(not a)
# False
```

推奨:

```python
1 not in li
```

非推奨:

```python
not 1 in li
```

---

# 演算子の優先順位

高い ↓

```text
()
**
* / %
+ -
比較演算子
not
and
or
```

---

# コメント

## 1行コメント

```python
# コメント
```

## 複数行コメント

```python
'''
コメント
コメント
'''
```

---

# print関数

```python
print("Hello")
```

複数出力

```python
print("A", "B", "C")
```

改行なし

```python
print("Hello", end="")
print("World")
```

出力

```text
HelloWorld
```

---

# 文字列

## インデックス

```python
s = "Hello"

print(s[0])
# H

print(s[-1])
# o
```

## スライス

```python
s = "Hello, World!"

print(s[1:4])
# ell

print(s[:5])
# Hello

print(s[7:])
# World!
```

## 長さ

```python
len(s)
```

## 文字列結合

```python
s = "Hello "
t = "World"

print(s + t)
```

## 繰り返し

```python
print("abc" * 3)

# abcabcabc
```

---

# f文字列

```python
time = "10"
place = "会議室A"

print(f"{time}時から{place}で会議を行います")
```

出力

```text
10時から会議室Aで会議を行います
```

---

# 変数

```python
player = "勇者"

print(player + "は荒野を歩いていた")
```

---

# 型変換

```python
number = 100

print("スライムが" + str(number) + "匹現れた")
```

---

# ランダム

```python
import random

random.randint(1, 100)
random.randrange(10)
random.random()
```

---

# 条件分岐

```python
if number == 1:
    print("スキ")
elif number == 2:
    print("キライ")
else:
    print("その他")
```

### pass

```python
if a < 0:
    pass
```

---

# for文

```python
for i in range(10):
    print(i)
```

## range

```python
range(10)
# 0〜9

range(6, 11)
# 6〜10
```

---

# while文

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

### ループ制御

```python
break
continue
```

---

# 入力

## 文字列

```python
line = input()
```

## 整数

```python
num = int(input())
```

## 複数入力

```python
a, b = map(int, input().split())
```

---

# リスト

## 作成

```python
team = ["勇者", "戦士", "魔法使い"]
```

## 追加

```python
team.append("盗賊")
```

## 更新

```python
team[0] = "英雄"
```

## 削除

```python
team.pop()
```

```python
team.remove("盗賊")
```

```python
del team[0]
```

---

# リストの操作

## ソート

```python
a = [3, 1, 2]

a.sort()
```

降順

```python
a.sort(reverse=True)
```

## sorted

```python
b = sorted(a)
```

---

# リスト内包表記

```python
numbers = [i for i in range(10)]
```

偶数のみ

```python
evens = [i for i in range(10) if i % 2 == 0]
```

---

# enumerate

```python
team = ["勇者", "戦士", "魔法使い"]

for i, player in enumerate(team):
    print(i, player)
```

---

# 辞書(Dictionary)

## 作成

```python
student = {
    "name": "Alice",
    "age": 21
}
```

## 取得

```python
student["name"]

student.get("age")
```

## 更新

```python
student["age"] = 22
```

## 追加

```python
student["grade"] = "A"
```

## 削除

```python
del student["grade"]
```

---

# タプル(Tuple)

## 作成

```python
t = (1, 2, 3)
```

## アンパック

```python
a, b, c = t
```

特徴

* 要素変更不可
* 高速
* 安全

---

# 集合(Set)

## 作成

```python
st = {1, 2, 3}
```

## 追加

```python
st.add(4)
```

## 削除

```python
st.remove(2)
```

---

## 集合演算

### 和集合

```python
a | b
```

### 積集合

```python
a & b
```

### 差集合

```python
a - b
```

### 対称差

```python
a ^ b
```

---

# 関数

## 定義

```python
def say_hello():
    print("Hello")
```

## 引数

```python
def add(a, b):
    return a + b
```

## デフォルト引数

```python
def introduce(name="村人"):
    print(name)
```

## 可変長引数

```python
def func(*args):
    print(args)
```

## キーワード引数

```python
def func(name, age):
    print(name, age)

func(age=20, name="Alice")
```

---

# スコープ

## ローカル変数

```python
def test():
    msg = "hello"
```

## グローバル変数

```python
x = 10

def func():
    global x
    x = 20
```

---

# クラス

```python
class Greeting:

    def say_hello(self):
        print("hello")
```

## インスタンス

```python
g = Greeting()
g.say_hello()
```

---

# コンストラクタ

```python
class Player:

    def __init__(self, job):
        self.job = job

    def walk(self):
        print(self.job)
```

```python
player = Player("戦士")
player.walk()
```

---

# モジュール

## import

```python
import random
```

## from import

```python
from random import randint
```

## alias

```python
import random as rd
```

---

# 例外処理

```python
try:
    num = int(input())

except ValueError:
    print("数字を入力してください")
```

複数例外

```python
except (ValueError, ZeroDivisionError):
    print("エラー")
```

---

# よく使う標準ライブラリ

## random

```python
import random
```

## math

```python
import math

math.sqrt(2)
```

## datetime

```python
import datetime

year = datetime.date.today().year
```

## sys

```python
import sys

sys.exit()
```

---

# Python学習の優先順位

1. 変数
2. 型(int, float, str)
3. 演算子
4. if文
5. for文
6. while文
7. リスト
8. 辞書
9. 関数
10. クラス
11. モジュール
12. 例外処理
13. 内包表記
14. オブジェクト指向
15. 再帰関数

この順番で学ぶと理解しやすい。

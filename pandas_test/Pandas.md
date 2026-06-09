# 🔷 Pandasとは（簡単）

**Pandas（パンダス）** は、Pythonでデータを表形式（ExcelやCSVのような表）で扱うためのライブラリです。

大量のデータを整理・加工・集計・分析することができ、データ分析やAI開発で必須級のライブラリです。

NumPyが数値計算の土台なら、Pandasはデータ分析の土台といえます。

---

# 🔷 Pandasでできること

- ExcelやCSVファイルの読み込み
- データの検索・抽出
- データの並び替え
- 集計（平均・合計など）
- 欠損値（空欄）の処理
- データの加工・整形
- グラフ作成用データの準備

---

# 🔷 Pandasの基本データ構造

Pandasには主に2つのデータ構造があります。

| 構造 | 説明 |
|--------|--------|
| Series | 1列のデータ |
| DataFrame | 表形式データ |

---

## ① Series

1列だけのデータです。

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

出力

```text
0    10
1    20
2    30
3    40
dtype: int64
```

---

## ② DataFrame

Excelの表のようなデータです。

```python
import pandas as pd

df = pd.DataFrame({
    "名前": ["田中", "佐藤", "鈴木"],
    "年齢": [25, 30, 28]
})

print(df)
```

出力

```text
   名前  年齢
0 田中   25
1 佐藤   30
2 鈴木   28
```

---

# 🔷 データの読み込み

CSVファイルを読み込む例

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df)
```

---

# 🔷 データの確認

## 先頭5行を見る

```python
df.head()
```

例

```text
   名前  年齢
0 田中   25
1 佐藤   30
2 鈴木   28
```

---

## データの情報を見る

```python
df.info()
```

例

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries
Data columns (total 2 columns)
```

---

## 基本統計量を確認

```python
df.describe()
```

例

```text
平均値
最大値
最小値
標準偏差
```

などが表示されます。

---

# 🔷 データの抽出

## 列を取り出す

```python
print(df["名前"])
```

出力

```text
0    田中
1    佐藤
2    鈴木
```

---

## 条件で抽出

30歳以上を抽出

```python
result = df[df["年齢"] >= 30]

print(result)
```

出力

```text
   名前  年齢
1 佐藤   30
```

---

# 🔷 データの追加

新しい列を追加

```python
df["給与"] = [300, 400, 350]

print(df)
```

出力

```text
   名前  年齢  給与
0 田中   25 300
1 佐藤   30 400
2 鈴木   28 350
```

---

# 🔷 データの並び替え

年齢順に並び替え

```python
df.sort_values("年齢")
```

---

# 🔷 集計処理

平均年齢

```python
df["年齢"].mean()
```

出力

```text
27.67
```

---

## 合計

```python
df["給与"].sum()
```

出力

```text
1050
```

---

# 🔷 欠損値処理

データが空欄の場合

```python
import numpy as np

df = pd.DataFrame({
    "年齢": [20, np.nan, 30]
})

print(df)
```

出力

```text
   年齢
0 20
1 NaN
2 30
```

---

## 欠損値を0で埋める

```python
df.fillna(0)
```

出力

```text
   年齢
0 20
1 0
2 30
```

---

# 🔷 NumPyとの関係

Pandasは内部でNumPyを利用しています。

```python
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3]
})

print(df["A"].values)
```

出力

```text
array([1, 2, 3])
```

NumPyの配列として取得できます。

---

# 🔷 車業界での使い道（重要）

## ① センサーデータ解析

車両ログデータ

```python
df = pd.read_csv("sensor.csv")
```

- 車速
- 加速度
- エンジン回転数

などを分析できます。

---

## ② CANデータ解析

CAN通信ログ

```python
df.head()
```

で確認できます。

---

## ③ 試験データ整理

実験結果

| 時刻 | 車速 |
|--------|--------|
| 0 | 10 |
| 1 | 15 |
| 2 | 20 |

を簡単に管理できます。

---

## ④ AI学習データ作成

```python
df.dropna()
```

不要データを削除し、

```python
df.to_csv("clean_data.csv")
```

学習用データとして保存できます。

---

# 🔷 普通のPythonとの違い

| 項目 | Python | Pandas |
|--------|--------|--------|
| 表形式データ | 扱いにくい | 得意 |
| CSV読込 | 面倒 | 簡単 |
| 集計 | 手作業 | 一瞬 |
| データ分析 | 非効率 | 高効率 |
| AI前処理 | 不向き | 必須級 |

---

# 🔷 重要ポイントまとめ

✅ Pythonのデータ分析ライブラリ

✅ Excelのような表形式データを扱える

✅ CSVやExcelを簡単に読み込める

✅ データの抽出・加工・集計が得意

✅ 欠損値処理が簡単

✅ NumPyを内部で利用している

✅ AI・機械学習の前処理で必須

✅ 車業界では

- センサーデータ解析
- CANログ解析
- 実験データ整理
- AI学習データ作成

などで活用される

> Pandasは「データを整理・分析するための標準ライブラリ」であり、NumPy・Matplotlib・Scikit-learnと組み合わせて使われることが非常に多いです。
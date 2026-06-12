# HTTPメソッド

GET と POST 以外にも HTTP メソッドはいくつかあります。

| メソッド | 主な用途 |
|----------|----------|
| GET | データ取得 |
| POST | データ作成・送信 |
| PUT | データ更新（全体更新） |
| PATCH | データ更新（一部更新） |
| DELETE | データ削除 |
| HEAD | ヘッダ情報だけ取得 |
| OPTIONS | 利用可能なメソッド確認 |

---

# 情報漏れの観点

## GETの注意点

```text
/login?user=taro&password=1234
```

URLにパスワードが見えてしまいます。

### 問題点

- ブラウザ履歴に残る
- ブックマークできる
- ログに記録される
- 画面共有で見える

そのため、

- ❌ パスワード
- ❌ クレジットカード情報
- ❌ 個人情報

には向きません。

---

## POSTなら安全？

```http
POST /login

user=taro
password=1234
```

データはURLに表示されません。

しかし、

**POSTだから暗号化されるわけではありません。**

---

# Flaskでの実務的な使い分け

## GET

検索：

```html
<form method="get">
```

例：

```text
/search?keyword=python
```

---

## POST

- ログイン
- 会員登録
- 問い合わせ
- データ登録

```html
<form method="post">
```

---

# Flaskでよくあるミス

```python
password = request.args["password"]
```

パスワードをGETで送る

↓

```text
/login?password=1234
```

となるので避ける。

代わりに、

```python
password = request.form["password"]
```

としてPOSTで送るのが一般的です。

---

# HTTPSの場合

SSL/TLSという仕組みで暗号化され、暗号文として

```text
8fj3Kx9a...
A2mPq7...
```

のような読めないデータとして送られます。

途中で通信を見ても内容は分かりません。

---

# Flaskでは

開発中は、

```python
app.run(debug=True)
```

で起動すると通常は HTTP です。

本番では

- Nginx
- Apache
- クラウドサービス

などが HTTPS 対応を行います。

例えば

- Render
- Railway
- PythonAnywhere

などにデプロイすると、HTTPS が自動で有効になることが多いです。

---

# クエリ文字列とは

GET メソッドで送信し、`?` の後ろの部分を **クエリ文字列** といいます。

例：

```text
/?name=勇者
```

---

## 複数なら

```text
/?name=勇者&level=10
```

---

## 取得方法

```python
request.args["name"]
request.args["level"]
```

---

## Flaskサーバ側から見ると

```python
ImmutableMultiDict([])
```

---

# GET と POST について

GET POST はどちらもブラウザからサーバへ送るリクエストの種類（HTTPメソッド）

- GET = データの取得を目的としたリクエスト
- POST = データの登録・変更を目的としたリクエスト

- GET → URLに付けて送る（`request.args`）（見える）
- POST → 本文に入れて送る（`request.form`）（URLには見えない）

- HTTPS = 通信を暗号化する

---

# GETの流れ

## ブラウザ（送信）

```http
GET /?name=勇者 HTTP/1.1
```

↓

## Flask（受信）

```python
name = request.args["name"]
```

↓

## Flask（送信）

```html
<h1>勇者</h1>
```

↓

## ブラウザ（受信）

---

# POSTの流れ

## ブラウザ（送信）

```http
POST /result HTTP/1.1

name=勇者
```

↓

## Flask（受信）

```python
name = request.form["name"]
```

↓

## Flask（送信）

```html
<h1>勇者はモンスターと戦った！</h1>
```

↓

## ブラウザ（受信）
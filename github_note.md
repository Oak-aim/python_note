# VS Code & GitHub 学習ノート

## 1. VS Codeとは

Visual Studio Code（VS Code）は Microsoft が提供する無料のソースコードエディタ。

特徴

- 無料
- 軽量で高速
- Windows / Mac / Linux対応
- Gitと連携可能
- 拡張機能が豊富
- Web開発、Python、C++、Flutterなどに対応

公式サイト
https://code.visualstudio.com/

---

# 2. VS Codeの基本操作

## フォルダを開く

メニュー

```
ファイル
↓
フォルダーを開く
```

ショートカット

```
Ctrl + K
Ctrl + O
```

---

## ファイル作成

エクスプローラー

```
新しいファイル
```

例

```
main.cpp
app.py
README.md
```

---

## 保存

```
Ctrl + S
```

---

## 検索

```
Ctrl + F
```

---

## 全体検索

```
Ctrl + Shift + F
```

---

## ターミナル起動

```
Ctrl + `
```

---

# 3. Gitとは

Gitはバージョン管理システム。

できること

- 変更履歴を記録
- 過去に戻せる
- チーム開発
- バックアップ

---

# 4. GitHubとは

GitHubはGitで管理されたソースコードを保存するサービス。

できること

- ソースコード管理
- 公開
- チーム開発
- ポートフォリオ作成

公式

https://github.com/

---

# 5. Gitの初期設定

名前設定

```bash
git config --global user.name "Your Name"
```

メール設定

```bash
git config --global user.email "sample@example.com"
```

確認

```bash
git config --list
```

---

# 6. GitHubアカウント作成

1. GitHubへアクセス
2. Sign Up
3. メール登録
4. ユーザー名設定
5. パスワード設定

---

# 7. リポジトリとは

プロジェクト保管場所。

例

```
todo_app
portfolio
django_app
```

---

# 8. GitHubでリポジトリ作成

右上

```
New Repository
```

設定例

```
Repository Name
todo_app
```

---

# 9. Git管理開始

フォルダ移動

```bash
cd todo_app
```

初期化

```bash
git init
```

---

# 10. Gitの状態確認

```bash
git status
```

---

# 11. ファイル追加

全て追加

```bash
git add .
```

個別追加

```bash
git add README.md
```

---

# 12. コミット

```bash
git commit -m "first commit"
```

例

```bash
git commit -m "add login function"
```

---

# 13. GitHub接続

確認

```bash
git remote -v
```

追加

```bash
git remote add origin URL
```

例

```bash
git remote add origin https://github.com/user/todo_app.git
```

---

# 14. 初回Push

```bash
git branch -M main
```

```bash
git push -u origin main
```

---

# 15. 更新時の流れ

状態確認

```bash
git status
```

追加

```bash
git add .
```

コミット

```bash
git commit -m "update"
```

Push

```bash
git push origin main
```

---

# 16. Pull

GitHubから取得

```bash
git pull origin main
```

---

# 17. コミット履歴

```bash
git log
```

簡易表示

```bash
git log --oneline
```

---

# 18. README.md

プロジェクト説明ファイル。

例

```md
# Todo App

タスク管理アプリです。

## 使用技術

- Flutter
- Dart
- SQLite
```

---

# 19. .gitignore

管理対象外ファイル設定

例

```gitignore
.vscode/
build/
.env
```

---

# 20. VS CodeでGit利用

左メニュー

```
Source Control
```

できること

- 変更確認
- コミット
- Push
- Pull

---

# 21. よく使うショートカット

保存

```
Ctrl + S
```

コピー

```
Ctrl + C
```

貼り付け

```
Ctrl + V
```

検索

```
Ctrl + F
```

置換

```
Ctrl + H
```

ターミナル

```
Ctrl + `
```

---

# 22. よく使うGitコマンド

```bash
git init
```

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "message"
```

```bash
git push origin main
```

```bash
git pull origin main
```

```bash
git log --oneline
```

```bash
git remote -v
```

---

# 23. GitHub活用方法

- ポートフォリオ公開
- 学習記録
- チーム開発
- ソースコード管理
- バックアップ

---

# 24. 学習成果

習得内容

- VS Code基本操作
- Git基本コマンド
- GitHub連携
- Push / Pull
- README作成
- コミット管理
- リポジトリ作成
- バージョン管理

今後はFlutter、Django、C++学習成果をGitHubへ公開し、ポートフォリオとして活用する。
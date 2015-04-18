Getaji-Bot
====
Getajiが運用しているBotです。コマンド機能とかがあります。

コマンド機能についての説明: https://gist.github.com/Getaji/ea040d7e72208b66291a

# How to run
1. `src/bot`ディレクトリにTwitter接続に必要な4つのキーを記述し、`config.json`の名前で保存。
2. `@Getaji`が使うことを想定しているので、その他のアカウント上で動かす場合は幾つかの処理を書き換える。
3. `src/bot/main.py`を実行する。

# Params
|パラメータ|説明|
|---|---|
|`--locally`|ローカルで稼働させることを明示。infoコマンドで使う。|
|`--silent`|起動時にツイートをしない。|

# License
各ライブラリのライセンスに従い著作権を表記します。

"requests" by Kenneth Reitz (http://python-requests.org/)
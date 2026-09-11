# 7つの扉

同じ歌詞を七通りの旋律で贈るための、プレゼント用ミュージックプレイヤー（試作 v0.1）。

- ディスクを選ぶ → デッキの丸窓に吸い込まれて回りはじめる
- 再生 / 一時停止 / 早送り / 巻き戻し / 前後の曲 / 取り出し
- 上のブラウン管テレビに映像（画像・動画・自動生成のいずれか）
- 右の歌詞カードが再生に合わせて流れる（七曲とも歌詞は共通）

## 見る

`index.html` をブラウザで開くだけ。ビルド不要・依存なし（書体だけ Google Fonts）。

## 差し替える

編集するのは `src/app.html` の上のほうにある 2 か所だけです。編集したら
`python3 tools/build.py` で配布用の `index.html` を作り直します。

### 1. 曲 — `TRACKS`

```js
{ n:'01', title:'あさやけ', tag:'MORNING PIANO', c:'#FFC46B', dur:204, scene:0,
  src:'assets/audio/01.mp3',        // 音源。null のあいだは仮のデモ音が鳴る
  visual:'assets/visuals/01.jpg' }  // テレビに映すもの。画像 / .mp4 / null
```

| 項目 | 意味 |
|---|---|
| `n` `title` `tag` | 盤面の番号・曲名・副題 |
| `c` | その曲の色（ディスクのラベル、テレビの発光色、選択中の枠） |
| `dur` | 尺（秒）。`src` を入れると実ファイルの長さで上書きされる |
| `src` | mp3 / m4a / wav。取得に失敗したら「よみこめません」と表示し、押せば取り直す |
| `visual` | 既定は `assets/visuals/NN.jpg`。置けば映り、無ければ `scene`(0–6) の自動生成映像 |
| `fit` | `contain`（既定・全体を収めて余りは黒帯）か `cover`（画面を埋めて切り取る） |
| `focus` | `cover` のときの縦の寄せ。`0`=上 / `.5`=中央（既定）/ `1`=下 |
| `cues` | 歌詞行の秒数 `[12.0, 18.4, ...]`。**これがある曲だけ**歌詞が曲に追従する |

### 1b. 贈り物の設定 — `GIFT`

```js
const GIFT = {
  to:   '',                            // 宛名。例: 'ゆうき と さき へ'。空なら出さない
  from: '',                            // 差出人。例: '同級生一同より'
  idleVisual: 'assets/visuals/07.jpg', // 何も入っていないときテレビに映す絵
  endAfterLast: true,                  // 最後の曲のあと、最初に戻らず締める（false で繰り返し）
};
```

宛名は見出しの上と、待受のテレビ画面に出ます。

### 2. 歌詞 — `LYRICS`

七曲共通なので一度書くだけ。`''` は空行、`[Chorus]` のような角括弧はセクション見出し。

歌詞を曲に合わせるには **`tools/sync.html`** を開きます（公開後なら
<https://roguepink.github.io/cdtukuru/tools/sync.html>）。曲を聴きながら行が変わるたびに
<kbd>SPACE</kbd> を叩くと秒数が並び、それを `TRACKS[].cues` に貼れば追従します。
`cues` が無い曲の歌詞は動きません（当て推量で動かすと歌とずれて読みづらいため）。

## 公開する（GitHub Pages）

`.github/workflows/deploy.yml` が入っているので、**push するたびに自動で公開されます**。
初回の実行が Pages 自体も有効にするため、設定画面を触る必要はありません。

公開先: <https://roguepink.github.io/cdtukuru/>

うまく動かないときは Actions タブで `Deploy to GitHub Pages` の実行結果を見てください。
手動で有効にする場合は Settings → Pages → Source: *Deploy from a branch* →
Branch: `claude/music-gift-app-design-b7blh5` / `/ (root)` → Save。

公開したリポジトリは誰でも見られます。曲・歌詞ごと公開になる点は承知のうえで。
オフラインで渡したいときは、フォルダごと ZIP にして `index.html` を開いてもらうだけでも動きます。

### スマホのホーム画面に追加すると

`manifest.webmanifest` と `assets/icon-*.png` を入れてあるので、iPhone / Android とも
「ホーム画面に追加」でアイコンが付き、アドレスバーの無い全画面で開きます。
リンクを送ったときのサムネイルは `assets/og.png`。公開先を変えたら `tools/build.py` の
`SITE` を直して作り直してください（`python3 tools/build.py`）。

アイコンとサムネイルの作り直しは `NODE_PATH=$(npm root -g) node tools/make-assets.js`（元は `tools/card.html`）。

## 構成

```
index.html        配布用（tools/build.py が生成。直接編集しない）
src/app.html      本体。HTML + CSS + JS が 1 枚に入っている
tools/build.py    src/app.html を index.html に包む
assets/audio/     01.mp3 〜 07.mp3（収録済み）
assets/visuals/   01.jpg 〜 07.jpg（収録済み。上書きすれば差し替わる）
assets/icon-*.png ホーム画面用アイコン / og.png リンクのサムネイル
manifest.webmanifest, .nojekyll   公開用
```

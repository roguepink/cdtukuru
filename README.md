# 七枚の同じ歌

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
| `src` | mp3 / m4a / wav。`assets/audio/` に置くのがおすすめ |
| `visual` | 既定は `assets/visuals/NN.jpg`。置けば映り、無ければ `scene`(0–6) の自動生成映像 |
| `fit` | `contain`（既定・全体を収めて余りは黒帯）か `cover`（画面を埋めて切り取る） |
| `focus` | `cover` のときの縦の寄せ。`0`=上 / `.5`=中央（既定）/ `1`=下 |
| `cues` | 任意。`[12.0, 18.4, ...]` と歌詞行の秒数を並べると手動同期になる |

### 2. 歌詞 — `LYRICS`

七曲共通なので一度書くだけ。`''` は空行（連の区切り）。
`cues` を書かない曲は、尺に合わせて自動で行送りします。

## 公開する（GitHub Pages）

1. リポジトリを **Public** にする — Settings → General → 一番下の Danger Zone → Change visibility
2. **Settings → Pages** → Source: *Deploy from a branch* → Branch: `claude/music-gift-app-design-b7blh5` / `/ (root)` → Save
3. 数分待つと <https://roguepink.github.io/cdtukuru/> で開く

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

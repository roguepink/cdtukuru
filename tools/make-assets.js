// アイコンとリンクプレビュー画像を tools/card.html から書き出す
// 使い方: NODE_PATH=$(npm root -g) node tools/make-assets.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const root = path.resolve(__dirname, '..');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:1200,height:700} });
  await p.goto('file://' + path.join(__dirname, 'card.html'));
  await p.waitForTimeout(1200);
  for (const size of [512, 192, 180]) {
    await p.evaluate(s => { const i = document.querySelector('#icon'); i.style.width = i.style.height = s + 'px'; }, size);
    await p.waitForTimeout(120);
    await (await p.$('#icon')).screenshot({ path: path.join(root, `assets/icon-${size}.png`) });
  }
  await (await p.$('#og')).screenshot({ path: path.join(root, 'assets/og.png') });
  await b.close();
  console.log('written');
})();

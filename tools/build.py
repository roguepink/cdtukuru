#!/usr/bin/env python3
"""src/app.html（Artifact としてもそのまま公開できる本体）を
   単体で開ける index.html に包む。"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
# リンクを送ったときのプレビュー画像の置き場所（公開先が変わったらここを直す）
SITE = "https://roguepink.github.io/cdtukuru"
body = (root / "src" / "app.html").read_text(encoding="utf-8")
doc = (
    "<!doctype html>\n<html lang=\"ja\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"description\" content=\"同じ歌詞・違う旋律の七曲を、CDプレイヤーとブラウン管で贈るプレイヤー\">\n"
    "<meta name=\"theme-color\" content=\"#0C0D10\">\n"
    "<link rel=\"icon\" href=\"assets/icon-192.png\" sizes=\"192x192\">\n"
    "<link rel=\"apple-touch-icon\" href=\"assets/icon-180.png\">\n"
    "<link rel=\"manifest\" href=\"manifest.webmanifest\">\n"
    "<meta name=\"apple-mobile-web-app-capable\" content=\"yes\">\n"
    "<meta name=\"apple-mobile-web-app-status-bar-style\" content=\"black\">\n"
    "<meta name=\"apple-mobile-web-app-title\" content=\"七枚の同じ歌\">\n"
    f"<meta property=\"og:title\" content=\"七枚の同じ歌\">\n"
    "<meta property=\"og:description\" content=\"おなじ歌詞を、七通りの旋律で。\">\n"
    "<meta property=\"og:type\" content=\"website\">\n"
    f"<meta property=\"og:url\" content=\"{SITE}/\">\n"
    f"<meta property=\"og:image\" content=\"{SITE}/assets/og.png\">\n"
    "<meta name=\"twitter:card\" content=\"summary_large_image\">\n"
    + body.split("<div class=\"room\">")[0].rstrip() + "\n</head>\n<body>\n"
    + "<div class=\"room\">" + body.split("<div class=\"room\">", 1)[1].strip() + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(doc, encoding="utf-8")
print("index.html:", len(doc), "bytes")

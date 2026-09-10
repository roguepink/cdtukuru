#!/usr/bin/env python3
"""src/app.html（Artifact としてもそのまま公開できる本体）を
   単体で開ける index.html に包む。"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
body = (root / "src" / "app.html").read_text(encoding="utf-8")
doc = (
    "<!doctype html>\n<html lang=\"ja\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"description\" content=\"同じ歌詞・違う旋律の七曲を、CDプレイヤーとブラウン管で贈るプレイヤー\">\n"
    "<meta name=\"theme-color\" content=\"#0C0D10\">\n"
    + body.split("<div class=\"room\">")[0].rstrip() + "\n</head>\n<body>\n"
    + "<div class=\"room\">" + body.split("<div class=\"room\">", 1)[1].strip() + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(doc, encoding="utf-8")
print("index.html:", len(doc), "bytes")

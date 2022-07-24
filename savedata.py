from asyncio.windows_events import NULL
import os
import json
import codecs  # 文字コード指定でのファイル読み書き


def save(score, data=".save"):
    nakami = load()
    nakami["生存時間"] = score
    save = json.dumps(nakami, ensure_ascii=False)  # ディクショナリ → json形式に変換
    file = codecs.open(data, "w", "utf-8")  # ファイルを書き込みモードで開く
    file.write(save)  # データ書き込み
    file.close()


def load(data=".save"):
    nakami = {}
    file = NULL
    # セーブデータが無ければ新規作成
    if os.path.exists(data) == False:  # 指定したファイルが無ければ
        # 初期データ用意
        nakami = {"生存時間": 0}
        save = json.dumps(nakami, ensure_ascii=False)  # ディクショナリ → json形式に変換

        file = codecs.open(data, "w", "utf-8")
        file.write(save)  # ファイル書き込み
    else:
        file = codecs.open(data, "r", "utf-8")  # 読み込み用でファイル開く
        nakami = json.load(file)  # ファイルの中身をjson → ディクショナリに変換
    file.close()  # ファイルを閉じる
    return nakami

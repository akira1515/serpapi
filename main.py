from serpapi import GoogleSearch
import os
import time
import re
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
API_KEY = os.getenv("API_KEY")

# Google検索用の基本パラメータ
BASE_PARAMS = {
    "api_key": API_KEY,
    "engine": "google",
    "q": "site:https://hrmos.co/pages/*/jobs",
    "location": "Japan",
    "google_domain": "google.co.jp",
    "gl": "jp",
    "hl": "ja",
    "num": 10,  # 1ページあたりの結果数
}

# 取得したURLを保存するリスト（重複を除くためにsetを使用）
job_urls = set()

# URL整形関数（不要なパラメータ削除）
def clean_url(url):
    return re.sub(r"(/jobs)/.*$", r"\1", url)  # `/jobs` の後ろに何かあれば削除

# 最大98ページ分の検索を実行（start=0,10,20...970）
for start in range(280, 290, 10):  # 例: 98ページなら range(0, 980, 10)
    print(f"🔍 {start//10+1}ページ目を取得中...")

    # ページごとの検索パラメータ
    params = BASE_PARAMS.copy()
    params["start"] = start  # ページの開始位置

    # SerpApi にリクエスト
    search = GoogleSearch(params)
    results = search.get_dict()

    # `organic_results` から `link` のみを取得
    if "organic_results" in results:
        for result in results["organic_results"]:
            link = result.get("link", "")
            if link.startswith("https://hrmos.co/pages/"):
                cleaned_link = clean_url(link)  # 整形処理
                job_urls.add(cleaned_link)  # setに追加（重複を除外）

    # 2秒の遅延（API制限を考慮）
    time.sleep(2)

# 結果を `newURL.txt` に保存
with open("newURL.txt", "w", encoding="utf-8") as f:
    for url in sorted(job_urls):  # ソートして保存
        f.write(url + "\n")

print(f"✅ 取得完了！ {len(job_urls)} 件のURLを `newURL.txt` に保存しました。")


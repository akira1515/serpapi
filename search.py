# ファイルを読み込んでセットに格納（重複削除＆高速検索）
def load_urls(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

# `check.txt` と `jobListingUrls.txt` をロード
check_urls = load_urls("check.txt")
job_listing_urls = load_urls("jobListingUrls.txt")

# `jobListingUrls.txt` に含まれる URL を `check.txt` から削除
deleted_urls = check_urls.intersection(job_listing_urls)  # 被ったURLを取得
remaining_urls = check_urls - deleted_urls        # 残ったURL

# `check.txt` を更新（被りを削除）
with open("check.txt", "w", encoding="utf-8") as f:
    for url in sorted(remaining_urls):  # ソートして書き込み（任意）
        f.write(url + "\n")

# `delete.txt` を作成（削除されたURLを記録）
with open("delete.txt", "w", encoding="utf-8") as f:
    for url in sorted(deleted_urls):
        f.write(url + "\n")

print(f"✅ 完了: {len(deleted_urls)} 件のURLを削除し、delete.txt に記録しました。")

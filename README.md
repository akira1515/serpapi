# serpapi

### 📘 **HRMOS 求人一覧 スクレイピング & URL管理スクリプト**

このプロジェクトでは、HRMOS の求人一覧ページ (`https://hrmos.co/pages/*/jobs`) を SerpApi を使用して Google 検索し、求人ページの URL を収集・管理します。  
また、既存の URL リスト (`jobListingUrls.txt`) を基に、不要な URL を削除するスクリプト (`search.py`) も含まれています。

---

## **📌 ファイル構成**
```
.
├── main.py        # SerpApi を使って求人 URL を収集
├── search.py      # 既存の URL リストと比較して重複を削除
├── .env           # 環境変数を保存（APIキーを格納）
├── newURL.txt     # 取得した求人 URL を保存
├── check.txt      # 追加の URL リスト（既存の URL と比較するため）
├── jobListingUrls.txt # 既存の URL リスト
├── delete.txt     # `check.txt` から削除された URL を記録
└── README.md      # このファイル（説明）
```

---

## **⚡ `main.py`（求人 URL 収集スクリプト）**
### **🔹 スクリプトの役割**
- SerpApi（Google 検索 API）を使用して、`site:https://hrmos.co/pages/*/jobs` の検索結果を取得
- 98ページ（最大 980 件）分の求人ページ URL を収集
- `/jobs/xxx` のようにパラメータがついた URL を整理し、`/jobs` までの形式に統一
- 取得した URL を `newURL.txt` に保存

### **🔹 使い方**
#### **1️⃣ 必要な Python パッケージをインストール**
以下のコマンドで `SerpApi` と `dotenv` をインストールしてください。

```sh
pip install google-search-results python-dotenv
```

#### **2️⃣ `.env` ファイルを作成**
プロジェクトのルートディレクトリに `.env` を作成し、APIキーを記載してください。

```
API_KEY=your_serpapi_key_here
```

#### **3️⃣ スクリプトを実行**
```sh
python main.py
```

#### **4️⃣ 実行後の出力**
- `newURL.txt` に、求人ページの URL がリストアップされます。

---

## **🛠️ `search.py`（URL の重複削除スクリプト）**
### **🔹 スクリプトの役割**
- `check.txt` にある URL と `jobListingUrls.txt`（既存の求人 URL）を比較
- `jobListingUrls.txt` に含まれる URL を `check.txt` から削除
- 削除された URL を `delete.txt` に記録

### **🔹 使い方**
#### **1️⃣ `check.txt` に新しい URL を記載**
新しく取得した URL（`newURL.txt` の中身）を `check.txt` にコピーしてください。

#### **2️⃣ スクリプトを実行**
```sh
python search.py
```

#### **3️⃣ 実行後の出力**
- `check.txt` から `jobListingUrls.txt` に含まれる重複 URL が削除されます。
- 削除された URL は `delete.txt` に記録されます。

---

## **📜 例**
**✅ `check.txt`（スクリプト実行前）**
```
https://hrmos.co/pages/onecareer/jobs
https://hrmos.co/pages/kpgluxuryhotels/jobs
https://hrmos.co/pages/examplecorp/jobs
```

**✅ `jobListingUrls.txt`（既存の URL）**
```
https://hrmos.co/pages/onecareer/jobs
https://hrmos.co/pages/examplecorp/jobs
```

**🏁 実行後**
- `check.txt`（`jobListingUrls.txt` にある URL を削除）
  ```
  https://hrmos.co/pages/kpgluxuryhotels/jobs
  ```

- `delete.txt`（削除された URL）
  ```
  https://hrmos.co/pages/onecareer/jobs
  https://hrmos.co/pages/examplecorp/jobs
  ```

---

## **📌 注意点**
- `main.py` を実行する際には **SerpApi の APIキー** が必要です。
- `check.txt` を `search.py` で更新する際、削除された URL は `delete.txt` に保存されます。
- `.env` に APIキーを保存し、`gitignore` に `.env` を追加することで **Git に APIキーを載せないように** してください。

---

## **🚀 まとめ**
| ファイル名       | 役割 |
|-----------------|------------------------------------------------|
| `main.py`       | SerpApi を使って求人一覧ページの URL を取得 |
| `search.py`     | `check.txt` の URL を `jobListingUrls.txt` と比較し、重複を削除 |
| `.env`          | APIキーを保存（Git に載せない） |
| `newURL.txt`    | 取得した URL のリスト |
| `check.txt`     | 追加の URL リスト（`jobListingUrls.txt` との比較用） |
| `jobListingUrls.txt` | 既存の URL リスト |
| `delete.txt`    | `check.txt` から削除された URL を記録 |


## Công nghệ sử dụng (Tech Stack)

* **Ngôn ngữ:** Python 3.10+
* **Data Extraction:** Apify (Google Maps Crawler)
* **Data Processing:** Pandas (DataFrames, JSON normalization)
* **Database:** SQLite 3
* **Tools:** VS Code, DB Browser for SQLite, Git/GitHub

## Cấu trúc dự án

```
WEEK01/
└── google_place_cleaner/
    ├── data_raw/
    │   └── locations_raw.json      # Dữ liệu thô từ Apify (JSON)
    ├── output/
    │   ├── locations_cleaned.csv   # Dữ liệu địa điểm đã làm sạch
    │   └── reviews_cleaned.csv     # Dữ liệu đánh giá tách riêng
    ├── sqlite_demo/
    │   └── final_places.db         # Database SQLite kết quả
    ├── scripts/
    │   ├── crawler.py              # Script cào dữ liệu từ Apify
    │   ├── scripts.py              # Script làm sạch & chuẩn hóa dữ liệu
    │   └── load_to_db.py           # Script import CSV vào SQLite
    ├── .env                        # Chứa API KEY (Không push lên Git)
    └── README.md                   # Tài liệu hướng dẫn
```

# Trình tự project (Project Workflow)

### 1️Bước 1: Thu thập dữ liệu (Extract)
Kết nối API Apify để lấy dữ liệu thô.
- **Input:** Cấu hình trong `crawler.py`.
- **Output:** File `data_raw/locations_raw.json`.

```bash
python google_place_cleaner/scripts/crawler.py
````

### 2️Bước 2: Làm sạch dữ liệu (Transform)

Xử lý JSON, chuẩn hóa dữ liệu và tách bảng.

  **Output:** 2 file CSV sạch trong thư mục `output/`.

```bash
python google_place_cleaner/scripts/scripts.py
```

### 3️Bước 3: Load vào Database (Load)

Tự động import các file CSV vào SQLite.

  **Output:** Tạo file database trong thư mục `sqlite_demo/`.


```bash
python google_place_cleaner/scripts/load_to_db.py
```
-----

### Hướng dẫn mở Project:

1.  Mở phần mềm **DB Browser for SQLite**.
2.  Chọn menu -\> **Open Project...**
3.  Điều hướng vào thư mục `sqlite_demo/`.
4.  Chọn file **`final_places.sqbpro`**.
import pandas as pd
import sqlite3
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

CSV_DIR = os.path.join(PROJECT_ROOT, "output")

DB_DIR = os.path.join(PROJECT_ROOT, "sqlite_demo")

DB_NAME = "final_places.db" 
DB_PATH = os.path.join(DB_DIR, DB_NAME)

def create_fresh_database():
    os.makedirs(DB_DIR, exist_ok=True)
    
    # if os.path.exists(DB_PATH):
    #     os.remove(DB_PATH)
    #     print(f"Đã xóa database cũ: {DB_NAME}")

    try:
        conn = sqlite3.connect(DB_PATH)
        print(f"Kết nối với SQLite tại: {DB_PATH}")
        return conn
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return None

def import_csv_to_sqlite(conn, csv_filename, table_name):
    csv_path = os.path.join(CSV_DIR, csv_filename)

    if not os.path.exists(csv_path):
        print(f"Không tìm thấy file {csv_filename} trong {CSV_DIR}")
        return

    try:
        print(f"Đang đọc file {csv_filename}...")
        
        df = pd.read_csv(csv_path)
        
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        print(f"Đã import {len(df)} dòng vào bảng '{table_name}'")
        
    except Exception as e:
        print(f"Lỗi khi import {csv_filename}: {e}")


if __name__ == "__main__":
    conn = create_fresh_database()
    
    if conn:
        # 1. Import bảng địa điểm
        import_csv_to_sqlite(conn, "locations_cleaned.csv", "locations")
        
        # 2. Import bảng đánh giá
        import_csv_to_sqlite(conn, "reviews_cleaned.csv", "reviews")
        
        conn.close()
        print("Import thành công")

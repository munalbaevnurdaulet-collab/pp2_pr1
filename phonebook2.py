import psycopg2
from config import load_config

def connect():
    config = load_config()
    return psycopg2.connect(**config)

# 1. Қосу немесе Жаңарту (CALL қолданамыз)
def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()
        print("✅ Done!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        cur.close()
        conn.close()

# 2. Іздеу (SELECT арқылы функцияны шақыру)
def search_contact():
    pattern = input("Search for: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

# 3. Өшіру (CALL)
def delete_contact():
    identifier = input("Enter name or phone to delete: ")
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("CALL delete_contact(%s)", (identifier,))
        conn.commit()
        print("🗑 Deleted!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        cur.close()
        conn.close()

# 4. Пагинация (Бетке бөлу)
def show_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n--- PHONEBOOK V2 (Procedures) ---")
        print("1. Add/Update Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show Paginated")
        print("0. Exit")
        
        choice = input("Choice: ")
        if choice == "1": upsert_contact()
        elif choice == "2": search_contact()
        elif choice == "3": delete_contact()
        elif choice == "4": show_paginated()
        elif choice == "0": break

if __name__ == "__main__":
    menu()
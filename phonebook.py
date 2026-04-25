import psycopg2
from config import load_config


# 🔌 Connection
def connect():
    config = load_config()
    return psycopg2.connect(**config)


# 🔍 FUNCTION: search
def search_pattern():
    pattern = input("Enter search pattern: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# 🔄 PROCEDURE: insert or update
def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

    print("✅ Inserted or updated")

    cur.close()
    conn.close()


# 📂 PROCEDURE: bulk insert
def insert_many():
    n = int(input("How many users: "))

    names = []
    phones = []

    for _ in range(n):
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        phones.append(phone)

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()

    print("✅ Bulk insert done")

    cur.close()
    conn.close()


# 📄 FUNCTION: pagination
def pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# ❌ PROCEDURE: delete
def delete_user():
    value = input("Enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    print("✅ Deleted")

    cur.close()
    conn.close()


# 📋 MENU
def menu():
    while True:
        print("\n===== PHONEBOOK MENU (ADVANCED) =====")
        print("1. Search (pattern)")
        print("2. Insert or Update")
        print("3. Bulk Insert")
        print("4. Pagination")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_pattern()
        elif choice == "2":
            insert_or_update()
        elif choice == "3":
            insert_many()
        elif choice == "4":
            pagination()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    menu()
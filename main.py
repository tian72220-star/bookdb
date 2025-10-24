from database import init_db, add_book, find_book, list_books, delete_book, update_book

def main():
    init_db()
    while True:
        print("1. Add book  2. Search  3. Delete  4. Update  5. List  6. Exit")
        ch = input("Select: ")
        if ch == "1":
            t, a, d, i = input("Title: "), input("Author: "), input("Date: "), input("ISBN: ")
            try:
                add_book(t, a, d, i)
                print("Added ✅")
            except Exception as e:
                print("Error:", e)
        elif ch == "2":
            row = find_book(input("Title to search: "))
            print(row if row else "Not found.")
        elif ch == "3":
            print("Deleted ✅" if delete_book(input("Title: ")) else "Not found.")
        elif ch == "4":
            old, nt, na, nd, ni = input("Old title: "), input("New title: "), input("New author: "), input("New date: "), input("New ISBN: ")
            print("Updated ✅" if update_book(old, nt, na, nd, ni) else "Not found.")
        elif ch == "5":
            for r in list_books():
                print("id={} | title={} | author={} | date={} | isbn={}".format(*r))
        elif ch == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

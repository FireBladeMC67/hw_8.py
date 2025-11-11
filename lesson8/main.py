from database.db_manager import DataBaseManager
from utils.menu import Menu  # если у тебя есть класс Menu

def main():
    db = DataBaseManager()  

    while True:
        choice = Menu.show_menu()

        if choice == "1":
            f = input("First Name: ")
            l = input("Last Name: ")
            a = int(input("Age: "))
            sid = input("Student ID: ")
            db.add_student(f, l, a, sid)

        elif choice == "2":
            for s in db.list_student():
                print(s)

        elif choice == "3":
            sid = int(input("Student numeric ID: "))
            cid = int(input("Course ID: "))
            g = float(input("Grade: "))
            db.add_grade(sid, cid, g)
            print("OK")

        elif choice == "4":
            rows = db.get_average_by_course()
            if not rows:
                print("Нет данных — добавь курсы и оценки.")
            else:
                for row in rows:
                    print(f"{row[0]} - {row[1]:.2f}")

        elif choice == "5":
            name = input("Course name: ")
            tid = int(input("Teacher ID: "))
            db.add_course(name, tid)
            print("Course added!")

        elif choice == "0":
            print("Exit")
            break

        else:
            print("Error")


main()

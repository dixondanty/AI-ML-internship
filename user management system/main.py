from auth import*
from exceptions import*
from util import line

while True:
    line()
    print("1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            dashboard(user)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except UserExistsError as e:
        print(e)

    except UserLoginError as e:
        print(e)

    finally:
        print("Operation completed")

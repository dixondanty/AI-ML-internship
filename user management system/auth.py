from filehandler import*
from exceptions import*
from log import logactivity
def register():
    users=readuser()
    un=input("Enter username:")
    pw=input("Enter password:")
    if un in users:
        raise UserExistsError("User already exists\n")
    saveuser(un,pw)
    logactivity(f"{un} registered")
    print("Registered succesfully")
    
def login():
    users=readuser()
    for i in range(3):
        usn=input("Enter username:")
        psw=input("Enter password:")
        if usn in users and users[usn]==psw:
            logactivity(f"{usn} logged in")
            print("Login Successful\n")
            return usn
    raise UserLoginError("Invalid credentials\n")
    

def dashboard(usn):
    while True:
        print("\n1.View")
        print("2.Update")
        print("3.Delete")
        print("4.Logout")

        choice = input("Choose: ")

        if choice == "1":
            print("Username:", usn)

        elif choice == "2":
            nun = input("New username: ")
            npw = input("New password: ")
            updateuser(usn, nun, npw)
            logactivity(f"{usn} updated account")
            username = nun
            print("Updated successfully")

        elif choice == "3":
            deleteuser(usn)
            logactivity(f"{usn} deleted account")
            print("Account deleted")
            break

        elif choice == "4":
            print("Logged out")
            break


    
    

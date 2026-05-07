filename="users.txt"
def readuser():
    user={}
    try:
        with open(filename,"r") as file:
            for line in file:
                un,pw=line.strip().split(",")
                user[un]=pw
    except FileNotFoundError:
        open(filename,"w").close()
    return user
def saveuser(usn,psw):
    with open(filename,"a") as file:
        file.write(f"{usn},{psw}\n")
def updateuser(osn,nun,npw):
    users=readuser()
    users.pop(osn)

    with open(filename,"w") as file:
        users[nun]=npw
        for usne,paswd in users.items():
            file.write(f"{usne},{paswd}\n")
def deleteuser(usn):
    users=readuser()
    users.pop(usn)

    with open(filename,"w") as file:
        for usne,paswd in users.items():
            file.write(f"{usne},{paswd}\n")
    

from datetime import datetime
def logactivity(mess):
    with open ("activity.log","a") as file:
        file.write(f"{datetime.now()} : {mess}\n")

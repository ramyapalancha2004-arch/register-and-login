import requests as r

def registerdata():
    username = input("enter the username: ")
    password = input("enter the password: ")
    mail = input("enter the mail: ")

    if username == "" or password == "" or mail == "":
        print("Please fill all details correctly.")
        return registerdata()   
    else:
        return {"username": username, "password": password, "mail": mail}

        

def register():
    res = r.get("http://localhost:3000/posts")
    existinguser= res.json()
    print("Existing:", existinguser)

    newuser= registerdata()
    print("New:",  newuser)

    exists=False
    for u in existinguser:
        if "username" in u and u["username"]==newuser["username"]:
            exists=True
        

    if exists:
        print("Username already exists!")
    else:
        res1 = r.post("http://localhost:3000/posts", json=newuser)
        print(res1.text)
        print("Successfully registered!")

register()



def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

  
    res = r.get("http://localhost:3000/posts")
    existinguser = res.json()

    for u in existinguser:
         if "username" in u and "password" in u:
            if u["username"] == username and u["password"] == password:
             found = True
             break

    if found:
        print("login successful! Welcome,", username)
    else:
        print("invalid username or password.")

def main():
    print("1.register")
    print("2.login")
    choice = input("entter choice:")
    if choice == "1":
        register() 
    elif choice == "2":
        login()
    else:
        print("Invalid choice! Try again.")
if __name__=="__main__":
    main()

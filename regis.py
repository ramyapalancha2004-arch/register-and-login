import streamlit as st
import requests as r

API_URL = "http://localhost:3000/posts"


def register():
    st.subheader(" Register")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    mail = st.text_input("Enter Email")

    if st.button("Register"):
        if not username or not password or not mail:
            st.warning(" Please fill all details correctly.")
            return

       
        res = r.get(API_URL)
        if res.status_code != 200:
            st.error(" Unable to connect to the server.")
            return

        existing_users = res.json()

        if any(u.get("username") == username for u in existing_users):
            st.error("Username already exists! Choose another one.")
        else:
            new_user = {"username": username, "password": password, "mail": mail}
            res1 = r.post(API_URL, json=new_user)

            if res1.status_code == 201:
                st.success("Registration Successful!")
            else:
                st.error(" Registration failed. Try again.")

def login():
    st.subheader("Login")
    username = st.text_input("Enter Username", key="login_user")
    password = st.text_input("Enter Password", type="password", key="login_pass")

    if st.button("Login"):
        res = r.get(API_URL)
        if res.status_code != 200:
            st.error("Unable to connect to the server.")
            return

        users = res.json()
        found = False
        for u in users:
            if u.get("username") == username and u.get("password") == password:
                found = True
                break

        if found:
            st.success(f" Login Successful! Welcome, {username}.")
        else:
            st.error(" Invalid username or password.")

def main():
    st.title(" User Authentication App")
    st.write("A simple Register & Login system using Streamlit + JSON Server")

    menu = ["Register", "Login"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Register":
        register()
    else:
        login()

if __name__ == "__main__":
    main()

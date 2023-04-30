import customtkinter 
import mysql.connector
from tkinter import messagebox


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1903920A-z",
  database="user_bank"
)
def bank_details():
    global deposit
    global withdrawal_now
    global show_details_window
    user_homepage = customtkinter.CTkToplevel()
    user_homepage.title("Bank Account homepage")
    user_homepage.geometry("1200x700")
    frame = customtkinter.CTkFrame(master= user_homepage)
    frame.pack(pady = 10, padx = 20, fill="both", expand=True,)
    welcome_message = customtkinter.CTkLabel(frame, text=("Homepage"))
    welcome_message.pack(pady = 12, padx= 10)
    deposit_money = customtkinter.CTkLabel(frame, text="Enter money you want to deposit")
    deposit_money.pack(pady = 12, padx= 10)
    deposit_entry = customtkinter.CTkEntry(frame)
    deposit_entry.pack()
    def deposit():
        password_entry_g = password_entry.get()
        db_g = deposit_entry.get()
        cursor.execute("UPDATE user_account SET Balance = Balance + %s WHERE password = %s", (db_g, password_entry_g))
        db.commit()
        customtkinter.CTkLabel(frame, text="deposit sucessfull").pack()

    deposit_button = customtkinter.CTkButton(frame, text="Deposit", command=deposit)
    deposit_button.pack(pady = 12, padx= 10)
    withdrawal_money = customtkinter.CTkLabel(frame, text="Enter ammount you want to withdraw Bellow")
    withdrawal_money.pack()
    withdrawal_entry = customtkinter.CTkEntry(frame)
    withdrawal_entry.pack(pady = 12, padx= 10)
    def withdrawal_now():
        withdrawal_entry_g = withdrawal_entry.get()
        password_entry_g = password_entry.get()
        cursor.execute("SELECT Balance FROM user_account WHERE password = %s", (password_entry_g,))
        result = cursor.fetchone()
        balance = result[0]
        if balance < int(withdrawal_entry_g):
            messagebox.showinfo("You do not have enough in your balance")
        else:
            update_statement = "UPDATE user_account SET Balance = Balance - %s WHERE password = %s"
            cursor.execute(update_statement, (withdrawal_entry_g, password_entry_g))
            db.commit()
            deposit_suc = customtkinter.CTkLabel(frame, text="Withdrawal sucessfull").pack()
        
    withdrawal_button = customtkinter.CTkButton(frame, text="Withdrawal", command= withdrawal_now)
    withdrawal_button.pack(pady = 12, padx= 10)
    
                
    def show_details_window():
        cursor.execute("SELECT balance FROM user_account ")
        result = cursor.fetchone()
        balance = result[0]
        customtkinter.CTkLabel(user_homepage, text="Account Balance:" + str(balance)).pack()
        return balance
                 

    customtkinter.CTkLabel(frame, text="Or if you want to check your account balance ").pack()
    show_details = customtkinter.CTkButton(frame, text="Check Balance", command=show_details_window)
    show_details.pack()
    customtkinter.CTkButton(frame, text="Exit", command=root.destroy).pack(pady = 12, padx= 10)



                               

cursor = db.cursor()
def open_new_window():
    new_window = customtkinter.CTkToplevel()
    new_window.title("Create account")
    new_window.geometry("900x7500")
    frame = customtkinter.CTkFrame(master= new_window)
    frame.pack(pady = 10, padx = 20, fill="both", expand=True,)
    new_account_message = customtkinter.CTkLabel(master=frame, text="Create username and password bellow")
    new_account_message.pack()
    new_username = customtkinter.CTkLabel(master= frame, text = " Create Username")
    new_username.pack()
    new_username_entry = customtkinter.CTkEntry(master= frame)
    new_username_entry.pack(pady = 12, padx= 10)
    new_password = customtkinter.CTkLabel(master= frame, text = " Create Password")
    new_password.pack()
    new_password_entry = customtkinter.CTkEntry(master= frame, show="*")
    new_password_entry.pack()
    display_name = customtkinter.CTkLabel(master=frame, text="what should we call you(First and last name)")
    display_name.pack()
    display_name_entry= customtkinter.CTkEntry(master=frame)
    display_name_entry.pack()
    get_age = customtkinter.CTkLabel(master=frame, text="how old are you")
    get_age.pack()
    get_age_entry = customtkinter.CTkEntry(master=frame)
    get_age_entry.pack()
    get_gender = customtkinter.CTkLabel(master=frame, text="what is your gender Male or Female")
    get_gender_entry = customtkinter.CTkEntry(master=frame)
    get_gender.pack()
    get_gender_entry.pack()
    def create_account():
        user_username = new_username_entry.get()
        user_password = new_password_entry.get()
        user_name = display_name_entry.get()
        user_age = get_age_entry.get()
        user_gender = get_gender_entry.get()
        query =("INSERT INTO user_account (username, password, Name, Age, Gender, registered) VALUES (%s, %s,%s, %s, %s, TRUE)")
        cursor.execute(query, (user_username, user_password, user_name,user_age,user_gender))
        db.commit()


    new_login_button = customtkinter.CTkButton(master=frame, text = "Register", command=lambda: (create_account(), new_window.destroy))
    new_login_button.pack(pady = 15, padx= 10)


    
    



def login():
    username = username_entry.get()
    password = password_entry.get()

    sql = "SELECT * FROM user_account WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(sql, values)

    user = cursor.fetchone()
    if user is not None:
        message_label.configure(text= "Login Successfull")
        root.withdraw()
        bank_details()

    else:
        message_label.configure(text= "INVALID USERNAME OR PASSWORD")      


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()


root.title("log in")
root.geometry("300x250")
username_lable = customtkinter.CTkLabel(root, text = "username")
username_lable.pack()
username_entry = customtkinter.CTkEntry(root)
username_entry.pack()

password_label = customtkinter.CTkLabel(root, text="Password ")
password_label.pack()
#show * displays the password as * instead of numbers
password_entry = customtkinter.CTkEntry(root, show="*")
password_entry.pack()

login_button = customtkinter.CTkButton(root, text= "log in", command=login)
login_button.pack(pady = 12, padx= 10)

message_label = customtkinter.CTkLabel(root, text="")
message_label.pack()

no_account = customtkinter.CTkLabel(root, text = "If you dont have an account creat one bellow")
no_account.pack()
creataccount_button = customtkinter.CTkButton(root, text= "creat account", command = open_new_window)
creataccount_button.pack()

root.mainloop()





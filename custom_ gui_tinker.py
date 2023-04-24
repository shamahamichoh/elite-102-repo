import customtkinter 
import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1903920A-z",
  database="user_bank"
)
def bank_details():
    def deposit():
        query = "SELECT Name, Age, Gender, Balance FROM user_account WHERE id = 1"
        cursor.execute(query)
        result = cursor.fetchone()
        customtkinter.CTkLabel(frame, text=result)
    def withdrawal():
        pass
    def show_user_details():
        pass    
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
    deposit_button = customtkinter.CTkButton(frame, text="Deposit", command=deposit())
    deposit_button.pack(pady = 12, padx= 10)
    withdrawal_money = customtkinter.CTkLabel(frame, text="Enter ammount you want to withdraw Bellow")
    withdrawal_money.pack()
    withdrawal_entry = customtkinter.CTkEntry(frame)
    withdrawal_entry.pack(pady = 12, padx= 10)
    withdrawal_button = customtkinter.CTkButton(frame, text="Withdrawal")
    withdrawal_button.pack(pady = 12, padx= 10)
                

    customtkinter.CTkLabel(frame, text="Or if you want to see your bank details ").pack()
    show_details = customtkinter.CTkButton(frame, text="Show Account Details", command= show_user_details)
    show_details.pack()

                               

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
        root.destroy()
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





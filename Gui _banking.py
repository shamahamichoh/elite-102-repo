import customtkinter

class BankingApp(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Banking App")
        self.master.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label_account = customtkinter.CTkLabel(self.master, text="Account Number")
        self.label_balance = customtkinter.CTkLabel(self.master, text="Balance")

        # create entry fields
        self.entry_account = customtkinter.CTkEntry(self.master)
        self.entry_balance = customtkinter.CTkEntry(self.master)

        # create buttons
        self.button_deposit = customtkinter.CTkButton(self.master, text="Deposit", command=self.deposit)
        self.button_withdraw = customtkinter.CTkButton(self.master, text="Withdraw", command=self.withdraw)
        self.button_exit = customtkinter.CTkButton(self.master, text="Exit", command=self.master.quit)

        # add labels, entry fields, and buttons to layout
        self.label_account.grid(row=0, column=0)
        self.entry_account.grid(row=0, column=1)
        self.label_balance.grid(row=1, column=0)
        self.entry_balance.grid(row=1, column=1)
        self.button_deposit.grid(row=2, column=0)
        self.button_withdraw.grid(row=2, column=1)
        self.button_exit.grid(row=3, column=0, columnspan=2)

    def deposit(self):
        account = self.entry_account.get()
        balance = float(self.entry_balance.get())
        # code to deposit balance into account

    def withdraw(self):
        account = self.entry_account.get()
        balance = float(self.entry_balance.get())
        # code to withdraw balance from account

root = customtkinter.CTk()
app = BankingApp(master=root)
app.mainloop()


#parent class
class User():
    def __init__(self,name,age,gender,):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender",self.gender)

#child class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("account balance has been updated: $", self.balance)
        
        
    def witdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficeint balance: Ballance Avalaible : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("acount balance has been updated: $", self.balance)
    def view_balance(self):
        self.show_details()
        print("balance: $", self.balance)
    
            

        
              
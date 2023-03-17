import tkinter as tk
from constants import *


class AuthFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)

        self.name = tk.StringVar(self, None)
        self.pwd = tk.StringVar(self, None)
        self.configure(background=P_COL)


        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_W, background=P_COL)

        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.pack()
        imageLbl.photo = image

        credit = tk.Label(leftFrame, text="Developed By: Utpal", font=(FONT_FAM, VSM_FONT_SIZE), background=P_COL, foreground=TXT_COL)
        credit.pack(side="left", padx=(5, 0), pady=(20, 0))

        leftFrame.pack(side=tk.LEFT, ipadx=5, ipady=5)


        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_W, background=P_COL)

        heading = tk.Label(rightFrame, text="Auth Pannel", font=(FONT_FAM, FONT_SIZE_HEADING), background=P_COL, foreground=TXT_COL)
        heading.pack(pady=(0, 30))

        inputFrame = tk.Frame(rightFrame, padx=5, background=P_COL)
        userLbl = tk.Label(inputFrame, text="Enter a username:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        userLbl.pack(pady=2, fill=tk.X)
        username = tk.Entry(inputFrame, textvariable=self.name, font=(FONT_FAM, FONT_SIZE), width=25)
        username.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)
    
        passwordLbl = tk.Label(inputFrame, text="Enter a password:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        passwordLbl.pack(pady=2, fill=tk.X)
        password = tk.Entry(inputFrame, show="֍", textvariable=self.pwd, font=(FONT_FAM, FONT_SIZE), width=25)
        password.pack(pady=2, fill=tk.X)
        inputFrame.pack(pady=5)

        submitFrame = tk.Frame(rightFrame, padx=10, background=P_COL)
        register = tk.Button(submitFrame, text="Sign Up", font=(FONT_FAM, FONT_SIZE), width=11, pady=5, command=lambda: self.register(controller), background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        register.pack(side=tk.LEFT, padx=5, pady=5)
        register.bind('<Enter>', controller.hoverBtn)
        register.bind('<Leave>', controller.unhoverBtn)

        login = tk.Button(submitFrame, text="Sign In", font=(FONT_FAM, FONT_SIZE), width=11, pady=5, command=lambda: self.login(controller), background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        login.pack(side=tk.RIGHT, padx=5, pady=5)
        login.bind('<Enter>', controller.hoverBtn)
        login.bind('<Leave>', controller.unhoverBtn)
        submitFrame.pack(padx=10, pady=5)

        rightFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, ipadx=10, ipady=10)


    def register(self, controller: tk.Tk):
        print("SIGN UP")
        name, pwd = self.name.get(), self.pwd.get()

        if len(name) !=0 and len(pwd) !=0:
            
            if " " in name and name.isalnum():
                print("Username cannot contain space and should be only alpha numeric!")

            
            elif len(pwd) < 8 or len(pwd) > 20:
                print("Password should be of 8 to 20 letters.")

            else:
                if name == "admin":
                    print("SIGNED UP")
                    info = controller.database.insertIntoAuthTable(AUTH_TABLE, (name, pwd), True)
                    print(info)
                else:
                    info = controller.database.insertIntoAuthTable(AUTH_TABLE, (name, pwd))
                    print(info)


    def login(self, controller: tk.Tk):
        name, pwd = self.name.get(), self.pwd.get()

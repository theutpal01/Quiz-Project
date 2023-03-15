from constants import *
import tkinter as tk
import tkinter.messagebox as msg
from Frames.AuthFrame import AuthFrame
from Frames.MenuFrame import MenuFrame
from Frames.QuizFrame import QuizFrame
from Frames.ResultFrame import ResultFrame
from Frames.AdminFrame import AdminFrame
from Frames.UserManageFrame import UserManageFrame
from Frames.QuizManageFrame import QuizManageFrame


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title(WIN_T)
        self.geometry(f"{WIN_W}x{WIN_H}")
        self.resizable(False, False)
        # self.iconbitmap("deps/quizImg.ico")

        self.configure(background=P_COL)
        self.bind("<Configure>", self.refresh)
        self.protocol("WM_DELETE_WINDOW", self.on_quit)

        # self.initial()

        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=2, pady=2)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (AuthFrame, MenuFrame, QuizFrame, ResultFrame, AdminFrame, UserManageFrame, QuizManageFrame):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames.update({F: frame})
        self.showFrame(QuizManageFrame)


    # SHOW THE FRAME ON THE MAIN APP
    def showFrame(self, toShowCont):
        frame = self.frames.get(toShowCont)
        frame.tkraise()


    # WHEN ANY BUTTON IS HOVERED
    def hoverBtn(self, event):
        event.widget["bg"] = T_COL


    # WHEN ANY BUTTON IS UNHOVERED
    def unhoverBtn(self, event):
        event.widget["bg"] = S_COL


    # METHOD TO REFRESH THE GUI
    def refresh(self, e=None):
        self.update_idletasks()


    # METHOD TO PROMPT QUIT DIALOG
    def on_quit(self):
        if msg.askyesno("Close App", "Do you really want to quit the application?"):
            self.destroy()



def main():
    app = App()
    app.mainloop()
    
    
if __name__ == '__main__':
    main()
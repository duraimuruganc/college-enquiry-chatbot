from tkinter import *
from chat import get_response, bot_name
import webbrowser

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        #Icon
        self.window.wm_iconbitmap("DSU.ico")
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("DSU Chat-Bot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=600)
        self.canvas = Canvas(self.window,bg="#475F47",height = 600,width = 1000,bd = 0,highlightthickness = 0,
        relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        
        #Bot Image
        global bot_img
        bot_img = PhotoImage(file=f"college.png")
        bot = self.canvas.create_image(500,300,image=bot_img)

        #DSU Logo
        global dsu_logo
        dsu_logo = PhotoImage(file=f"DSU.png")
        dsu = self.canvas.create_image(490,90,image=dsu_logo)

        #100 years Logo
        global centenary_logo
        centenary_logo = PhotoImage(file=f"logo.png")
        centenary = self.canvas.create_image(950,100,image=centenary_logo)

        #DSU Text
        self.canvas.create_text(
        556.0,16.0,anchor="nw",
        text="Dayananda Sagar University  \n",
        fill="#FFFFFF",font=("Revalia",15))
        
        #Text
        self.canvas.create_text(
        650.0,60.0,anchor="nw",
        text="Live the Dream!",
        fill="#FFFFFF",font=("Revalia", 13))

        #Link Button
        dsu_link=Label(self.window,bg="#475F47",fg="blue",text="www.dsu.edu.in",pady=10,cursor="hand2",font=("Revalia",15))
        dsu_link.pack()
        dsu_link.bind("<Button-1>",lambda e:
        self.callback("https://www.dsu.edu.in/"))
        dsu_link.place(x=635,y=93,width=198,height=34)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg="#222831", fg="#FFFFFF",
                                 padx=5, pady=5)
        self.text_widget.place(x=420,y=192,width=571,height=307)
        msg3 = f"{bot_name}: Hey there.Welcome to Dayananda Sagar  University \nLive the Dream!\nHow can I help you?\n"
        self.text_widget.insert(END,msg3)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.984,width=10)
        scrollbar.configure(command=self.text_widget.yview)

        
        # message entry box
        self.msg_entry = Entry(self.window, bg="#C9EDFF", font="Abadi")
        self.msg_entry.place(x=420,y=515,width=418,height=60)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_pressed)

        #send button
        send_button = Button(self.window, text="Send", font="Raleway", width=20, bg="#C9EDFF",fg="blue",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(x=849,y=515,width=107,height=60)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg,"Student")
        ###sname=self.msg_entry.get()
        ###self._insert_message(msg,f"{sname}")

        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

    #Call WebBrowser    
    def callback(self,url):
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()

import customtkinter
from frames.ToolBar_Frame import ToolBar
import config

class WindowMain:
    def __init__(self, master):
        self.master = master
        self.master.title('Meu Todo List')
        self.master.geometry('1200x700')
        self.master.resizable(False, False)
        customtkinter.set_appearance_mode('dark')
       
        # self.master.iconbitmap(config.ICON_HOME)

        toolbar = ToolBar(self.master)  # Remover se não for necessário usar toolbar em outro local
        toolbar.create_tool_bar()

    def mainloop(self):
        self.master.mainloop()


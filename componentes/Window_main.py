import config
from frames.ToolBar_Frame import ToolBar

class WindowMain:
    def __init__(self, master):

        self.master = master
        self.master.title('Lista da Italazinha')
        self.master.configure(background=config.BACKGROUND_COLOR)
        self.master.geometry('1200x700')
        self.master.resizable(False,False)
        #self.master.iconbitmap(config.ICON_HOME)

        toolbar = ToolBar(self.master) #remover se eu não precisar usar toolbar em outro local
        toolbar.create_tool_bar()
      
    def mainloop(self):
        self.master.mainloop()


from tkinter import Frame, ttk, PhotoImage
import config

class ToolBar:
    def __init__(self, master):
        self.master = master
        self.create_tool_bar()

    def create_tool_bar(self):
        # Criando a barra de ferramentas
        self.frame_ToolBar = Frame(self.master, bg=config.SECONDARY_COLOR, padx=25, pady=10)
        self.frame_ToolBar.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        # Criando uma frame para os botões
        self.button_frame = Frame(self.frame_ToolBar, bg=config.SECONDARY_COLOR)
        self.button_frame.grid(row=0, column=0, sticky="nsew")

        # Criando os botões
        self.create_button(config.ICON_MENU, 'ToolBar.TButton', 0, 0, 0, 10, self.master.destroy)
        self.create_button(config.ICON_HOME, 'ToolBar.TButton', 1, 0, 0, 0, None)

    def create_button(self, image: str, ButtonStyle: str, col_grid: int, row_grid: int, pxLeft: int, pxRight: int, Btn_command) -> None:
        home_icon = PhotoImage(file=image)

        style = ttk.Style()
        style.theme_use('alt')
        style.configure(ButtonStyle, background=config.SECONDARY_COLOR, relief='flat')
        style.map(ButtonStyle, 
              background=[('active', config.BACKGROUND_COLOR)],
              relief=[('pressed', 'sunken'), ('!pressed', 'flat')]  
              )

        button = ttk.Button(self.button_frame, cursor="hand2", image=home_icon, style=ButtonStyle, command=Btn_command, takefocus=False)
        button.image = home_icon  
        button.grid(column=col_grid, row=row_grid, padx=(pxLeft, pxRight))



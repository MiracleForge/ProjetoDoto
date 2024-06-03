from tkinter import Frame, ttk, PhotoImage
import config

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
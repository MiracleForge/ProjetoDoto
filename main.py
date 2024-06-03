import customtkinter
from componentes.Window_main import WindowMain

def main():
    root = customtkinter.CTk()  # Usando CTk em vez de Tk
    app = WindowMain(root)
    app.mainloop()

if __name__ == "__main__":
    main()

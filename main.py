from tkinter import Tk
from componentes.Window_main import WindowMain

def main(): 
    root = Tk()
    app = WindowMain(root)
    app.mainloop()

if __name__ == "__main__":
    main()

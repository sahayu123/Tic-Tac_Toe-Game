from home_tic_tac_toe import Home
import tkinter
root=tkinter.Tk()
root.geometry("800x800")
root.title("Tic-Tac-Toe Game")


home=Home()
root.config(bg="antiquewhite")
home.create_home_page(root)

   


       
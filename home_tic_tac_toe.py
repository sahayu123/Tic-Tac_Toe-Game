import tkinter
from game_tic_tac_toe import Game

class Home():
    def __init__(self):
        pass
    def create_home_page(self,root):
        
        display_label=tkinter.Label(root,text="Tic-Tac-Toe-Game",font=("Times 18"))
        display_label.place(relx=0.5,rely=0.1,anchor="center")


        display_label_player_one_score=tkinter.Label(root,text="Player One Score",font=("Times 14"))
        display_label_player_one_score.place(relx=0.3,rely=0.3,anchor="center")

        display_label_player_one_score_show=tkinter.Label(root,text="0",font=("Times 14"))
        display_label_player_one_score_show.place(relx=0.3,rely=0.4,anchor="center")

        def start_game():
            self.cont.set(1)
        
        def on_close():
            self.cont.set(1)
            root.destroy()   


        display_label_player_two_score=tkinter.Label(root,text="Player Two Score",font=("Times 14"))
        display_label_player_two_score.place(relx=0.7,rely=0.3,anchor="center")

        display_label_player_two_score_show=tkinter.Label(root,text="0",font=("Times 14"))
        display_label_player_two_score_show.place(relx=0.7,rely=0.4,anchor="center")

        continue_btn=tkinter.Button(root,text="continue",font=("Times 14"),command=start_game)
        continue_btn.place(relx=0.5,rely=0.7,anchor="center")

        root.protocol("WM_DELETE_WINDOW", on_close)

        self.cont=tkinter.IntVar()
        root.wait_variable(self.cont)
        
        for widgets in root.winfo_children():
                    widgets.destroy()
        game=Game()
        game.initiate_game(root)
      

        print("outside")

        
        while True:
            for widgets in root.winfo_children():
                    widgets.destroy()
            game=Game()
            game.initiate_game(root)
            print("outside")
        
            root=tkinter.Tk()
            root.geometry("800x800")
            root.title("Tic-Tac-Toe Game")
            root.config(bg="antiquewhite")
            root.protocol("WM_DELETE_WINDOW", on_close)
            for widgets in root.winfo_children():
                print("destroying item")
                widgets.destroy()

            display_label=tkinter.Label(root,text="Tic-Tac-Toe-Game",font=("Times 18"))
            display_label.place(relx=0.5,rely=0.1,anchor="center")


            display_label_player_one_score=tkinter.Label(root,text="Player One Score",font=("Times 14"))
            display_label_player_one_score.place(relx=0.3,rely=0.3,anchor="center")

            display_label_player_one_score_show=tkinter.Label(root,text="0",font=("Times 14"))
            display_label_player_one_score_show.place(relx=0.3,rely=0.4,anchor="center")
   
            def start_game():
                self.cont.set(1)
                
             
            

            display_label_player_two_score=tkinter.Label(root,text="Player Two Score",font=("Times 14"))
            display_label_player_two_score.place(relx=0.7,rely=0.3,anchor="center")

            display_label_player_two_score_show=tkinter.Label(root,text="0",font=("Times 14"))
            display_label_player_two_score_show.place(relx=0.7,rely=0.4,anchor="center")

            continue_btn=tkinter.Button(root,text="continue",font=("Times 14"),command=start_game)
            continue_btn.place(relx=0.5,rely=0.7,anchor="center")

            self.cont=tkinter.IntVar()
            root.wait_variable(self.cont)



        


        


        root.mainloop()



#initialize root window
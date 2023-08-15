import tkinter
from game_tic_tac_toe import Game
from player import Player

class Home():
    def __init__(self):
        self.player_one=Player(1)
        self.player_two=Player(2)
    
    def create_home_page(self,root):
        
        display_label=tkinter.Label(root,text="Tic-Tac-Toe-Game",font=("Times 18"))
        display_label.place(relx=0.5,rely=0.1,anchor="center")


        display_label_player_one_score=tkinter.Label(root,text="Player One Score",font=("Times 14"))
        display_label_player_one_score.place(relx=0.3,rely=0.3,anchor="center")

        display_label_player_one_score_show=tkinter.Label(root,font=("Times 14"))
        display_label_player_one_score_show.place(relx=0.3,rely=0.4,anchor="center")
        display_label_player_one_score_show["text"]=str(self.player_one.score)

        def start_game():
            self.cont.set(1)
        
        def on_close():
            self.cont.set(1)
            root.destroy()   


        display_label_player_two_score=tkinter.Label(root,text="Player Two Score",font=("Times 14"))
        display_label_player_two_score.place(relx=0.7,rely=0.3,anchor="center")

        display_label_player_two_score_show=tkinter.Label(root,font=("Times 14"))
        display_label_player_two_score_show.place(relx=0.7,rely=0.4,anchor="center")
        display_label_player_two_score_show["text"]=str(self.player_two.score)

        continue_btn=tkinter.Button(root,text="continue",font=("Times 14"),command=start_game)
        continue_btn.place(relx=0.5,rely=0.7,anchor="center")

        root.protocol("WM_DELETE_WINDOW", on_close)

        self.cont=tkinter.IntVar()
        root.wait_variable(self.cont)
        
        for widgets in root.winfo_children():
                    widgets.destroy()
        game=Game(self.player_one,self.player_two)
        game.initiate_game(root)
        
        
        first=self.player_two
        print("player one score ::"+str(self.player_one.score)+" \n player two score ::",str(self.player_two.score))
        while True:
            for widgets in root.winfo_children():
                    widgets.destroy()
            
            root.config(bg="antiquewhite")

            display_label=tkinter.Label(root,text="Tic-Tac-Toe-Game",font=("Times 18"))
            display_label.place(relx=0.5,rely=0.1,anchor="center")


            display_label_player_one_score=tkinter.Label(root,text="Player One Score",font=("Times 14"))
            
            display_label_player_one_score.place(relx=0.3,rely=0.3,anchor="center")

            display_label_player_one_score_show=tkinter.Label(root,font=("Times 14"))
            display_label_player_one_score_show.place(relx=0.3,rely=0.4,anchor="center")
            display_label_player_one_score_show["text"]=str(self.player_one.score)
   
            def start_game():
                self.cont.set(1)
                
            display_label_player_two_score=tkinter.Label(root,text="Player Two Score",font=("Times 14"))
            display_label_player_two_score.place(relx=0.7,rely=0.3,anchor="center")

            display_label_player_two_score_show=tkinter.Label(root,font=("Times 14"))
            display_label_player_two_score_show.place(relx=0.7,rely=0.4,anchor="center")
            display_label_player_two_score_show["text"]=str(self.player_two.score)

            continue_btn=tkinter.Button(root,text="continue",font=("Times 14"),command=start_game)
            continue_btn.place(relx=0.5,rely=0.7,anchor="center")

            root.protocol("WM_DELETE_WINDOW", on_close)

            self.cont=tkinter.IntVar()
            root.wait_variable(self.cont)

            for widgets in root.winfo_children():
                    widgets.destroy()
            if first==self.player_one:
                game=Game(self.player_one,self.player_two)
                game.initiate_game(root)
            else:
                game=Game(self.player_two,self.player_one)
                game.initiate_game(root)

            



        


        


        root.mainloop()



#initialize root window
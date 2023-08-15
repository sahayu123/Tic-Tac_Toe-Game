import tkinter
from PIL import Image, ImageTk

#import libraries
class Game():
    def __init__(self,player_one,player_two):
        self.stop_game=False

        self.player_one=player_one
        self.player_two=player_two
        
        self.click=dict()

        self.top_left_clicked=False
        self.middle_left_clicked=False
        self.bottom_left_clicked=False
      

        self.top_middle_clicked=False
        self.middle_clicked=False
        self.bottom_middle_clicked=False

        self.top_right_clicked=False
        self.middle_right_clicked=False
        self.bottom_right_clicked=False
        
        
        self.left_column=list()
        self.right_column=list()
        self.middle_column=list()
        
        self.top_row=list()
        self.middle_row=list()
        self.bottom_row=list()

        self.left_diagnol=list()
        self.right_diagnol=list()
        
        self.spaces_filled=0
        self.turn=self.player_one
    
    def end(self,root):
            for widgets in root.winfo_children():
                widgets.destroy()
            self.cont.set(1)
            print("In here")
            
    def set_var(self,var):
            if var=="top_left":
                self.top_left_clicked=self.turn
                self.left_column.append(self.turn)
                self.left_diagnol.append(self.turn)
                self.top_row.append(self.turn)
            elif var=="middle_left":
                self.middle_left_clicked=self.turn
                self.left_column.append(self.turn)
                self.middle_row.append(self.turn)
            elif var=="bottom_left":
                self.bottom_left_clicked=self.turn
                self.left_column.append(self.turn)
                self.right_diagnol.append(self.turn)
                self.bottom_row.append(self.turn)

            elif var=="top_right":
                self.top_right_clicked=self.turn
                self.right_column.append(self.turn)
                self.right_diagnol.append(self.turn)
                self.top_row.append(self.turn)
            elif var=="middle_right":
                self.middle_right_clicked=self.turn
                self.right_column.append(self.turn)
                self.middle_row.append(self.turn)
            elif var=="bottom_right":
                self.bottom_right_clicked=self.turn
                self.right_column.append(self.turn)
                self.left_diagnol.append(self.turn)
                self.bottom_row.append(self.turn)

            elif var=="top_middle":
                self.top_middle_clicked=self.turn
                self.middle_column.append(self.turn)
                self.top_row.append(self.turn)
            elif var=="middle":
                self.middle_clicked=self.turn
                self.middle_column.append(self.turn)
                self.middle_row.append(self.turn)
                self.left_diagnol.append(self.turn)
                self.right_diagnol.append(self.turn)
            elif var=="bottom_middle":
                self.bottom_middle_clicked=self.turn
                self.middle_column.append(self.turn)
                self.bottom_row.append(self.turn)
    
    def round_check(self):
        holding_list=[self.left_column,self.right_column,self.middle_column,self.top_row,self.middle_row,self.bottom_row,self.left_diagnol,self.right_diagnol]
        tie_opt=0
        for lst in holding_list:
            if len(lst)==3:
                item=lst[0]
                winner=False
                for val in lst:
                    if val == item :
                        winner=True 
                        item=val
                    else:
                        winner=False
                        break
                if winner:
                    self.stop_game=True
                    return winner,item
                else:
                    tie_opt=tie_opt+1
            elif len(lst)==2:
                if lst[0]!=lst[1]:
                    tie_opt=tie_opt+1
            else:
                continue
        if self.spaces_filled==9:
            self.stop_game=True
            return "tie",None
        print("This is tie opt",tie_opt)
        if tie_opt==8:
            self.stop_game=True
            return "tie", None
        return False,None
    
    def initiate_game(self,root):
        display_label=tkinter.Label(root,text="Tic-Tac-Toe-Game",font=("Times 18"))
        display_label.place(relx=0.5,rely=0.1,anchor="center")

        turn_label=tkinter.Label(root,font=("Times 14"))
        turn_label["text"]="Player "+str(self.player_one.player_number) +" it is your turn"
        turn_label.place(relx=0.5,rely=0.2,anchor="center") 
        
      
        def pr(turn_label,btn,var):
            if self.click[btn]!=False:
                print("alderdy clicked square")
            elif self.stop_game:
                print("Game Over")
            else:
                if self.turn==self.player_one:
                    #print("turn x")
                    img=Image.open("tic-tac-toe-cross.png")
                    image=img.resize((90,90))
                    img_to_add=ImageTk.PhotoImage(image)
                    btn["image"]=img_to_add
                    btn.img=img_to_add
                    turn_label["text"]="Player "+str(self.player_two.player_number) +" it is your turn"
                    self.set_var(var)
                    self.turn=self.player_two
                    #print("turn in if ",turn)
                    self.click[btn]="x"
                    #print(self.click)
                else:
                    #print("turn o")
                    img=Image.open("tic-tac-toe-o.png")
                    image=img.resize((90,90))
                    img_to_add=ImageTk.PhotoImage(image)
                    btn["image"]=img_to_add
                    btn.img=img_to_add
                    turn_label["text"]="Player "+str(self.player_one.player_number)+" it is your turn"
                    self.set_var(var)
                    self.turn=self.player_one
                    self.click[btn]="o"
                    #print("Alderedy clicked")
                    #print(self.click)

                self.spaces_filled=self.spaces_filled+1
                ans=self.round_check()
                if ans[0]==True:
                    if self.turn==self.player_one:
                        self.player_two.score=self.player_two.score+1
                        turn_label["text"]="Player "+str(self.player_two.player_number)+ " has won the game"
                    else:
                        self.player_one.score=self.player_one.score+1
                        turn_label["text"]="Player "+str(self.player_one.player_number)+ " has won the game"

                    root.config(bg="cyan")
                    def on_close():
                        self.cont.set(1)
                        root.destroy()   
                    root.protocol("WM_DELETE_WINDOW", on_close)
                    next_button=tkinter.Button(root,text="Next",font=("Times 18"),command=lambda:self.end(root))
                    next_button.place(relx=0.5,rely=0.8,anchor="center")
                    self.cont=tkinter.IntVar()
                    root.wait_variable(self.cont)
                    self.done.set(1)
                    print("Game Over eee")
                elif ans[0]=="tie":
                    turn_label["text"]="Player 1 and 2 have tied the game"
                    root.config(bg="cyan")
                    def on_close():
                        self.cont.set(1)
                        root.destroy()   
                    root.protocol("WM_DELETE_WINDOW", on_close)
                    next_button=tkinter.Button(root,text="Next",font=("Times 18"),command=lambda: self.end(root))
                    next_button.place(relx=0.5,rely=0.8,anchor="center")
                    self.cont=tkinter.IntVar()
                    root.wait_variable(self.cont)
                    self.done.set(1)
                    print("Game Over ffff")
                    
        def add_blank_image(btn):
            img=Image.open("blank.png")
            image=img.resize((90,90))
            img_to_add=ImageTk.PhotoImage(image)
            btn["image"]=img_to_add
            btn.img=img_to_add

        
        top_left_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,top_left_square,"top_left"))
        top_left_square.place(relx=0.35,rely=0.35,anchor="center")
        add_blank_image(top_left_square)

        middle_left_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,middle_left_square,"middle_left"))
        middle_left_square.place(relx=0.35,rely=0.5,anchor="center")
        add_blank_image(middle_left_square)


        bottom_left_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,bottom_left_square,"bottom_left"))
        bottom_left_square.place(relx=0.35,rely=0.65,anchor="center")
        add_blank_image(bottom_left_square)



        top_middle_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,top_middle_square,"top_middle"))
        top_middle_square.place(relx=0.5,rely=0.35,anchor="center")
        add_blank_image(top_middle_square)

        middle_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,middle_square,"middle"))
        middle_square.place(relx=0.5,rely=0.5,anchor="center")
        add_blank_image(middle_square)

        bottom_middle_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,bottom_middle_square,"bottom_middle"))
        bottom_middle_square.place(relx=0.5,rely=0.65,anchor="center")
        add_blank_image(bottom_middle_square)



        top_right_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,top_right_square,"top_right"))
        top_right_square.place(relx=0.65,rely=0.35,anchor="center")
        add_blank_image(top_right_square)

        middle_right_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,middle_right_square,"middle_right"))
        middle_right_square.place(relx=0.65,rely=0.5,anchor="center")
        add_blank_image(middle_right_square)

        bottom_right_square=tkinter.Button(root,text="click here",command=lambda: pr(turn_label,bottom_right_square,"bottom_right"))
        bottom_right_square.place(relx=0.65,rely=0.65,anchor="center")
        add_blank_image(bottom_right_square)


        self.click[top_left_square]=self.top_left_clicked
        self.click[middle_left_square]=self.middle_left_clicked
        self.click[bottom_left_square]=self.bottom_left_clicked

        self.click[top_middle_square]=self.top_middle_clicked
        self.click[middle_square]=self.middle_clicked
        self.click[bottom_middle_square]=self.bottom_middle_clicked

        self.click[top_right_square]=self.top_right_clicked
        self.click[middle_right_square]=self.middle_right_clicked
        self.click[bottom_right_square]=self.bottom_right_clicked
        
        self.done=tkinter.IntVar()
        root.wait_variable(self.done)

        return "smth"


        root.mainloop()
        


import tkinter as tk
from tkinter import messagebox
from PIL import Image , ImageTk


class TicTacToe:
    def __init__(self, master):
        self.turn = 0 
        self.sign_list = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.master = master
        self.buttons = []
        self.onButtonClickedFirstTime = True
        
        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=0, column=0, padx=10, pady=10)

        self.info_label = tk.Label(master, text="Player 1's Turn", bg="blue", fg="white", font=("Helvetica", 14))
        self.info_label.grid(row=0, column=1, columnspan=3, sticky="ew")


        id = 1



        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.button_frame,image=self.resizeImage(None), text=f"Box {id}", width=250, height=250, command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
                id += 1
            self.buttons.append(button_row)

    def resizeImage(self,turn):
        original_image = None
        if turn is None :
            original_image = Image.new("RGBA", (250, 250), (0, 0, 0, 0))
        else : 
            original_image = Image.open('./images/' + turn + '.png')
        resized_image = original_image.resize((250, 250))  # Replace with your desired dimensions
        self.resized_photo = ImageTk.PhotoImage(resized_image)


    def reset_board(self):
            index = 1
            for button_row in self.buttons : 
                for button in button_row : 
                    button.config(text =f"Box {index}") 
                    index +=1
            self.turn = 0
            self.info_label.config(text="Player 1's turn")
            self.top.destroy()

    

    def on_button_click(self,row,col):
        button = self.buttons[row][col]
        if self.onButtonClickedFirstTime:
            for button_rows in self.buttons :
                for actual_button in button_rows:
                    actual_button = tk.Button(self.button_frame,image=self.resizeImage('X'), width=250, height=250, command=lambda row=row, col=col: self.on_button_click(row, col))
                    actual_button.config(image=self.resizeImage('X'))
                    
                    actual_button.config(width=250, height=250)
            self.onButtonClickedFirstTime = False
        
        self.sign_list[row][col] = self.turn
        if button["text"] != "X" :
            if self.turn == 0 : 
                button["text"] = "X"
                button.config(image=self.resizeImage('X'))
                self.info_label.config(text="Player 2's Turn")  
            else :  
                button["text"] = "O"
                self.info_label.config(text="Player 1's Turn")  
                button.config(image=self.resizeImage('O'))

        self.turn = 1 - self.turn
        self.check_game_completion()

        print("This row has been clicked " + str(row) + " and this is the column " + str(col))

    def display_pop_up(self, player_name):
        self.top = tk.Toplevel(self.master)
        # top.geometry("300X200")
        tk.Label(self.top,text=player_name + " has won the game").pack()
        tk.Button(self.top,text="Try Again",command=self.reset_board).pack()

    def check_game_completion(self):
        game_completed_list = [[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(1,0),(1,1),(1,2)],
         [(2,0),(2,1),(2,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
         [(0,0),(1,1),(2,2)]]
        
        for game_complete in game_completed_list :
            s = set()
            for row,col in game_complete : 
                 button = self.buttons[row][col]
                 print(button["text"])
                 s.add(button["text"])
            if len(s) == 1 and ( 'X' or 'O' in s):
                player_name = ""
                if self.turn == 0 : 
                    player_name = "Player 2"
                else : 
                    player_name = "Player 1"

                self.display_pop_up(player_name)
                print("Game Completed Dear") 







    # Write code for reseting the board !!!

        
        

root = tk.Tk()

tictactoe_ui = TicTacToe(root)
root.mainloop()

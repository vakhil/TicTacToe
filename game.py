import tkinter as tk



class TicTacToe:
    def __init__(self, master):
        self.turn = 0 
        self.sign_list = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.master = master
        self.buttons = []
        
        button_frame = tk.Frame(master)
        button_frame.grid(row=0, column=0, padx=10, pady=10)

        self.info_label = tk.Label(master, text="Player 1's Turn", bg="grey", fg="white", font=("Helvetica", 14))
        self.info_label.grid(row=0, column=1, columnspan=3, sticky="ew")


        id = 1

        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(button_frame, text=f"Box {id}", width=12, height=10, command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
                id += 1
            self.buttons.append(button_row)

    def on_button_click(self,row,col):
        button = self.master.grid_slaves(row=row, column=col)[0]
        self.sign_list[row][col] = self.turn
        if button["text"] != "X" :
            if self.turn == 0 : 
                button["text"] = "X"
            else :  
                button["text"] = "O"
        self.turn = 1 - self.turn
        self.check_game_completion()

        print("This row has been clicked " + str(row) + " and this is the column " + str(col))

    def check_game_completion(self):
        game_completed_list = [[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(1,0),(1,1),(1,2)],
         [(2,0),(2,1),(2,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
         [(0,0),(1,1),(2,2)]]
        
        for game_complete in game_completed_list :
            s = set()
            for row,col in game_complete : 
                 s.add(self.master.grid_slaves(row=row, column=col)[0]["text"])
            if len(s) == 1 and ( 'X' or 'O' in s):
                print("Game Completed Dear") 
        
        

root = tk.Tk()

tictactoe_ui = TicTacToe(root)
root.mainloop()

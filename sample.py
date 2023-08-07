import tkinter as tk
root = tk.Tk()
info_label = tk.Label(root, text="Player 1's Turn", bg="grey", fg="white", font=("Helvetica", 14))
info_label.grid(row=0, column=0, columnspan=3, sticky="ew")

root.mainloop()

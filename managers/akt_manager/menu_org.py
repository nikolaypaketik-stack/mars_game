import customtkinter as ctk

class MenuOrg:
    def __init__(self):
        self.game_state = "menu"


        self.root = ctk.CTk()
        self.root.geometry("720x720") 
        self.root.configure(fg_color="black")

        self.start_button = ctk.CTkButton(
            self.root,
            text="START",
            width=200,
            height=60,
            fg_color="#222222",
            hover_color="#00aa00",  
            command=self.start_game
        )


        self.exit_button = ctk.CTkButton(
            self.root,
            text="EXIT",
            width=200,
            height=60,
            fg_color="#222222",
            hover_color="#aa0000",
            command=self.root.destroy
        )

        self.start_button.pack(pady=20)
        self.exit_button.pack(pady=20)

    def start_game(self):
        self.game_state = "akt1"
        self.root.destroy()

    def run(self):
        self.root.mainloop()
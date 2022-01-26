
import tkinter

class Screen_CharacterSelection (tkinter.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
        self.roster = roster
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        self.character_index = tkinter.StringVar()
        self.character_index.set(None)

        tkinter.Label(self, text='Hit Points', font=('Verdana', 14)).grid(row=0, column=2, sticky=tkinter.N, padx=10, pady=15)
        tkinter.Label(self, text='Dexterity', font=('Verdana', 14)).grid(row=0, column=3, sticky=tkinter.N, padx=10, pady=15)
        tkinter.Label(self, text='Strength', font=('Verdana', 14)).grid(row=0, column=4, sticky=tkinter.N, padx=10, pady=15)

        for char in range(len(self.roster.character_list)):
            character = self.roster.character_list[char]
            
            tkinter.Radiobutton(self, text=character.name, variable=self.character_index, value=char, command=self.selectedCharacter, font=('Verdana', 12)).grid(
                row=char+2, column=0, sticky=tkinter.W, padx=(15, 10))
            
            image = tkinter.PhotoImage(file=f'images/{character.small_image}')
            imgLbl = tkinter.Label(self, text=character.name, image=image)
            imgLbl.photo = image
            imgLbl.grid(row=char+2, column=1, sticky=tkinter.N)

            tkinter.Label(self, text=character.hit_points, font=('Verdana', 13)).grid(row=char+2, column=2, sticky=tkinter.E + tkinter.W)
            tkinter.Label(self, text=character.dexterity, font=('Verdana', 13)).grid(row=char+2, column=3, sticky=tkinter.E + tkinter.W)
            tkinter.Label(self, text=character.strength, font=('Verdana', 13)).grid(row=char+2, column=4, sticky=tkinter.E + tkinter.W)
        
        self.continueBttn = tkinter.Button(self, text='Select a Character')
        self.continueBttn.grid(row=len(self.roster.character_list) + 2, column=3, columnspan=2, sticky=tkinter.E)
    
    def selectedCharacter(self):
        self.continueBttn['text'] = 'Prepare to Battle!'
        self.continueBttn['command'] = self.selected_clicked
       
    def selected_clicked(self):
        self.callback_on_selected(self.character_index.get())

from characters import Character
import tkinter

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        # labels to say who picked what character
        tkinter.Label(self, text = 'You', font = 'Calibri 18').grid(row = 0, column = 0)
        tkinter.Label(self, text = "Computer", font = 'Calibri 18').grid(row = 0, column = 1)
        
        #Picture of player's image
        playerImage = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label (self, image = playerImage)
        w.photo = playerImage # saving the image as a property is required for "saving" the image. It's odd.
        w.grid (row = 1, column = 0)

        #Picture of computer's image
        computerImage = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label (self, image = computerImage)
        w.photo = computerImage # saving the image as a property is required for "saving" the image. It's odd.
        w.grid (row = 1, column = 1)

        # create labels to show the health of the characters
        tkinter.Label(self, text = f'{self.player1.hit_points} HP', font = 'Calibri 18').grid(row = 2, column = 0, sticky = tkinter.E+tkinter.W)
        tkinter.Label(self, text = f'{self.player2.hit_points} HP', font = 'Calibri 18').grid(row = 2, column = 1, sticky = tkinter.E+tkinter.W)

        # create labels to show the dexterities of the characters
        tkinter.Label(self, text = f'{self.player1.dexterity} Dexterity', font = 'Calibri 18').grid(row = 3, column = 0, sticky = tkinter.E+tkinter.W)
        tkinter.Label(self, text = f'{self.player2.dexterity} Dexterity', font = 'Calibri 18').grid(row = 3, column = 1, sticky = tkinter.E+tkinter.W)

        # create labels to show the strengths of the characters
        tkinter.Label(self, text = f'{self.player1.strength} Strength', font = 'Calibri 18').grid(row = 4, column = 0, sticky = tkinter.E+tkinter.W)
        tkinter.Label(self, text = f'{self.player2.strength} Strength', font = 'Calibri 18').grid(row = 4, column = 1, sticky = tkinter.E+tkinter.W)

        # create a button to move onto the battle
        battle_start_button = tkinter.Button(self, text = "Commence Battle!", font = 'Calibri 18 bold', fg = 'Firebrick', bg = 'Dark Turquoise', command = self.commence_battle_clicked)
        battle_start_button.grid(row = 5, column = 1, sticky = tkinter.S+tkinter.E)

    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        
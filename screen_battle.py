import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.attackButton = tkinter.Button(self, text="Attack!", bg='black', fg='red', command=self.attack_clicked)
        self.attackButton.grid(row=0,column=0,sticky=tkinter.N)

        self.p1AttackText = tkinter.Label(self,text='')
        self.p1AttackText.grid(row=1,column=1)

        self.p2AttackText = tkinter.Label(self,text='')
        self.p2AttackText.grid(row=2,column=1)

        self.victoryText= tkinter.Label(self,text='',fg='red')
        self.victoryText.grid(row=3,column=1,sticky=tkinter.N)

        self.youText = tkinter.Label(self,text='You').grid(row=4,column=0,sticky=tkinter.N)
        self.compText = tkinter.Label(self,text='Computer').grid(row=4,column=1,sticky=tkinter.N)

        self.p1imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        self.p1image = tkinter.Label (self,image = self.p1imageLarge)
        self.p1image.photo = self.p1imageLarge
        self.p1image.grid(row=5,column=0)

        self.p2imageLarge = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        self.p2image = tkinter.Label (self,image = self.p2imageLarge)
        self.p2image.photo = self.p2imageLarge
        self.p2image.grid(row=5,column=1)

        self.p1healthText = tkinter.Label(self,text=f'{self.player1_max_hp}/{self.player1_max_hp}')
        self.p1healthText.grid(row=6,column=0,sticky=tkinter.N)
        self.p2healthText = tkinter.Label(self,text=f'{self.player2_max_hp}/{self.player2_max_hp}')
        self.p2healthText.grid(row=6,column=1,sticky=tkinter.N)

    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        
        self.p1AttackText['text'] = self.player1.attack(self.player2)
        if self.player2.hit_points > 0:
            self.p2AttackText['text'] = self.player2.attack(self.player1)
        self.p1healthText['text'] = f'{self.player1.hit_points}/{self.player1_max_hp}'
        self.p2healthText['text'] = f'{self.player2.hit_points}/{self.player2_max_hp}'

        if self.player1.hit_points <= 0 or self.player2.hit_points <= 0:
            self.exitButton = tkinter.Button(self, text='Exit', fg='red', font='Calibri 18',bg='black',command=self.exit_clicked).grid(row=7,column = 1, sticky=tkinter.E)
            self.attackButton.destroy()   
            self.victoryText['text'] = self.player1.name+" is victorious!" if self.player1.hit_points > 0 else self.player2.name+" is victorious!"
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()

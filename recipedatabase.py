import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os
from sitemapimport import *
import sitemapimport
from PIL import ImageTk, image


## This initializes the object that will be assigned the yes/no variable for the first window
class submitConf:
    def __init__(self, yesNo, recipeclass, ):
        self.__yesNo = yesNo
        self.__recipeclass = recipeclass
    
    def set_yesNo(self, yesNo):
        self.__yesNo = yesNo
        
    def set__recipeclass(self, recipeclass):
        self.__recipeclass = recipeclass

    def get_yesNo(self):
        return self.__yesNo
    
    def get_recipeclass(self):
        return self.__recipeclass

class recipeLookup:
    def __init__(self, master):
        
        self.master = master
        master.title("GF Recipe Database")
## Check to see if database exists
        if os.path.exists('database.csv'):
        ## If a database of the same name is present, the program will prompt the user with whether they want to recreate it or not
            ## This creates the text the user will see, and defines the alignment
            tk.Label(master, text='A recipe database already exists. \n Would you like to re-initialize the database? \n \n Note: re-initializing the database may take \n some time, and the program may appear stuck.').grid(row=0, column=0, padx= 10, pady= 10, columnspan=2)
            
            ## This initalizes the variable for the yes/no button
            self.yesNo_var = tk.StringVar(value='1')
       
            ## Information for the yes and no radio buttons
            R1 = tk.Radiobutton(master, text='Yes', value='yes', var = self.yesNo_var)
            R2 = tk.Radiobutton(master, text='No', value='no', var = self.yesNo_var)
       
            ## Radiobutton alignments
            R1.grid(row = 1, column= 0)
            R2.grid(row = 1, column = 1)    
       
            ## Creates the submit button and alligns it
            self.submit_button = tk.Button(master, text='Submit', command=self.submit)
            self.submit_button.grid(row= 2, column=0, padx=10, pady=10, columnspan=2)

    
    # Create the submit button function
    def submit(self):
    # Retrieves whether the yes or no button was clicked
        yesNo = self.yesNo_var.get()
    ## Shows error if submit is clicked without a radiobutton being selected
        if not yesNo:
            messagebox.showerror('Error', 'Please choose yes or no.')
            return
        ## If the user selects yes to recreating the database, the program will run the creation loop and then open the next window
        if yesNo == "yes":
            dbWin()
        ## If the user selects no to recreating the database, they will continue to the next window
        if yesNo == "no":
            secondWin()

def dbWin():
    sitemapimport.listMaker()
    secondWin()
    ## This function will create the next window for the program
    
def secondWin():
    ## .destroy is used to automatically close the previous window
    root.destroy()
    ## Naming the new window and defining the dimensions and name of it
    master2 = Tk()
    master2.geometry('350x250')
    master2.title("GF Recipe Database")
    
    ## Initalizes the values of the recipe selection menu
    recipe_var = tk.StringVar()
    masterList = ttk.Combobox(master2,  width=27, textvariable = recipe_var)
    masterList['values'] = (' Select Recipe Type:',
                        ' Fruits',
                        ' Vegetables',
                        ' Dairy',
                        ' Meat',
                        ' Dessert'
                        ' Pasta/Noodles', 
                        ' Drinks', 
                        ' Bread',
                        ' Breakfast',
                        ' Egg Dishes',
                        ' Nuts',
                        ' By Flavor', 
                        ' Misc. Foods')
        ## Sets the default value to the first value, "Select Recipe type"
    masterList.current(0)
    masterList.pack()
    ## Second submit button for the second window
    submit2_button = tk.Button(master2, text='Submit', command=submit2)
    submit2_button.pack(padx=10, pady=10)
    
 ## Saves the value chosen by the submit button
def submit2():
    recipeclass = recipe_var.get()
    
        ## Initializes sublists to creat another combomenu
    if recipeclass == " Fruits":
            fruitsList()
    if recipeclass == " Vegetables":
            vegetablesList()
    if recipeclass == " Dairy":
            dairyList()
    if recipeclass == " Meat":
            meatList()
    if recipeclass == " Dessert":
            dessertList()
    if recipeclass == " Pasta/Noodles":
            pastaList()
    if recipeclass == " Drinks":
            drinksList()
    if recipeclass == " Bread":
            breadList()
    if recipeclass == "Breakfast":
            breakfastList()
    if recipeclass == " Egg Dishes":
            eggsList()
    if recipeclass == " Nuts":
            nutsList()
    if recipeclass == " By Flavor":
            flavor()
    if recipeclass == ' Misc. Foods':
            miscList()
## If the fruit sublist is chosen, it will list all websites in the "fruit" list in label format.
def fruitsList():
    master2 = Tk()
        fruitImg = tk.PhotoImage(file="fruits.jpg")
        fruitImg.pack()
        for x in fruit:
            label = label(root, text=x)
            label.pack()
            label.append(label)

def vegetablesList():
    master2 = Tk()
        vegImg = tk.PhotoImage(file="veggies.jpg")
        vegImg.pack()
        for x in vegetable:
            label = label(root, text=x)
            label.pack()
            label.append(label)

## Starts the main program
if __name__ == '__main__':
    root = tk.Tk()
    app = recipeLookup(root)
    root.mainloop()


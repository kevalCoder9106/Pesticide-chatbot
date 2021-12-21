# db url
# mongodb+srv://admin992:8733981820@cluster0.mgtom.mongodb.net/prj1?retryWrites=true&w=majority

from tkinter import *
import pandas
#from pymongo import MongoClient, results

#Step 1: Connect to MongoDB - Note: Change connection string as needed
# client = MongoClient("mongodb+srv://admin992:8733981820@cluster0.mgtom.mongodb.net/prj1?retryWrites=true&w=majority")
# db = client.business

data = pandas.read_csv("data.csv")

grammer_words = ["my","is","a","an","are","not","like","name","number","address","animal","symptoms","symtoms","symtom","symptom","crop",","," "]

def find_word(to_find,array):
    """
        this function will return any particular word from list of string
    """
    for i in array:
        if i == to_find:
            return True

    return False

def differ_entity(array):
    """
        this function will return any word or list of word which are not grammer_word list and could be user data
    """
    is_differ = None
    entities = []

    for i in array: # looping through string list
        for y in grammer_words: # looping a string list through grammer_word list
            """
            if once the string element is equal to one of the grammer_word list element
            then is_differ will set to false which is sign that it is not a user data
            is_differ will stay True if the string is user data
            """
            if i == y:
                is_differ = False 
        
        # appending string
        if is_differ == True:
            entities.append(i)
        
        is_differ = True

    if len(entities) == 1: # if user has provided data in one word
        return entities[0]
    elif len(entities) == 0: # if user havent provided any data
        return 0
    elif len(entities) > 1: # if user has provided multiple data (Which will return a list)
        return entities 

def get_insectiside(crop_name):
    index = 0

    while True:
        try:
            if crop_name == data.iloc[index]['crop']: #----------------
                insectiside = data.iloc[index]['insect'] #----------------
                insectiside = str(insectiside).split(">>")
                return insectiside

            index = index + 1
        except:
            break

    return 0


def send():    
    message = "You ->" + e.get()
    txt.insert(END, "\n" + message)

    # convert the input text to lower case for case issues
    input_text = str(e.get()).lower()
    # spliting input sentence into array
    input_text_array = input_text.split(" ")

    if e.get() == 'hi' or e.get() == 'hello' or e.get() == 'my animal is not ok' or e.get() == 'i need help':
        txt.insert(END, "\n"+"Bot -> Hello there, enter crop name")
    elif find_word("crop",input_text_array):
        crop_name = differ_entity(input_text_array)
        insect_names = get_insectiside(crop_name)
        if insect_names != 0:
            txt.insert(END, "\n"+f"Bot -> \n")
            for data in insect_names:
                txt.insert(END, "\n"+f"{data}")
        else:
            txt.insert(END, "\n"+f"Data not found...")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry I didn't get you")

    e.delete(0, END)


root = Tk()
root.configure(background="black")

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send_button = Button(root, text="send", command=lambda:send()).grid(row=1, column=1)

e.grid(row=1, column=0)
root.title("ChatBot")
root.mainloop()
root.mainloop()


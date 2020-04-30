import json
from difflib import get_close_matches
file=json.load(open(r"G:\Projects\#FUN\Dictinary_app\data.json"))

def tranc(word):
    return file[word]
while(True):
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("----             THIS IS DICTIONARY APP           ----")
    print("----          PRESS 1 FOR THE SEARCH WORD         ----")
    print("----          PRESS 2 FOR THE  EXIT               ----")
    select=int(input("Enter your choice......"))
    if(select==1):
    
        input_word=input("Enter the word : ")
        input_word=input_word.lower()
        
        if input_word in file.keys():
            print(tranc(input_word))
        elif len(get_close_matches(input_word,file.keys()))>0:
            word=get_close_matches(input_word,file.keys())[0]
            print("Did you mean",word) 
            choice=input("If Yes press 'Y' If No press 'N' ")
            choice=choice.upper()
            if choice=='Y':
                print(tranc(word))
            elif choice=='N':
                print("THIS IS NOT RECOGNISE WORD PLEASE CHECK SPELLING...!!!!")
    elif(select==2):
        print("CODED BY RAPCHIK UMANG")
        break
        

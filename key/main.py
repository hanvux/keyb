import random
import os
import sys
import routes

def routes(key, first_word):
    def markov_lib(key, character1):
        data_sample = "moby-dick.txt"
        text_data = open(data_sample, 'r').read()
        text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')
        markov_lib = {}

        for i in range(len(text_data)-key):
            word = " ".join(text_data[i:i+key])
            if word.lower() in markov_lib.keys():
                markov_lib[word.lower()].append(text_data[i+key])
            else:
                markov_lib[word.lower()] = [text_data[i+key]]

        try:
            character2 = random.choice(markov_lib[character1.lower()])
        except KeyError as e:
            return ("fail")
        return character2
    
    message = first_word
    while(True):
        os.system('cls')
        first_word = " ".join(message.split()[0-key:])
        predicted_next_word = markov_lib(key,first_word)

        if predicted_next_word == "fail":
            print("-------------------------\nThe training text is not big enough to predict the next word. Exited")
        response = input(message +" ["+predicted_next_word+"] ")
        
        if response == "t" or response == "T":
            #os.system('cls')
            message = message + " " + predicted_next_word
        if response == "f" or response == "F":
            os.system('cls')
            r = input(message + " ")
            message = message + " " + r

        if response == "E" or response == "e":
            print(message)
            break
routes(1, "A")
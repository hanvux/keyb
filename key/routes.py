
from flask import Blueprint, render_template, request, redirect, Flask
app = Flask(__name__, template_folder='templates',static_folder='static')  
import random
import os
import sys


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/analyze", methods=['POST'])

def analyze():
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
    key = int(request.form['accuracy'])
    first_word = str(request.form['text'])
    message = first_word
    while(True):
        os.system('cls')
        first_word = " ".join(message.split()[0-key:])
        predicted_next_word = markov_lib(key,first_word)

        if predicted_next_word == "fail":
            print("-------------------------\nThe training text is not big enough to predict the next word. Exited")
        response = str(request.form['res'])
        
        if response == "t" or response == "T":
            #os.system('cls')
            message = message + " " + predicted_next_word
        if response == "f" or response == "F":
            os.system('cls')
            r = message + " " + {request.form['res']}
            message = message + " " + r

        if response == "E" or response == "e":
            print(message)
            break
    render_template('index.html', message = message)
if __name__=='__main__':
   app.run(debug=True)
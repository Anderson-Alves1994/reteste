import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    def primo (n):
    if n != 0 and n !=1:
        if n>3:
            for i in range(2,n):
                if n %i==0:
                    return False
        return True
    return


i=1
cont =0
while True:
    primo(i)
    i+=1
    if primo(i) == True:
        cont+=1
        print(i)
    if cont == 100:
        break

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

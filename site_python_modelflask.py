from flask import Flask

app = Flask(__name__)

#criar a 1 pagina do site 
#route-> link
#funcao -> O que voce que exibir na pagina

@app.route("/")
def homepage():
    return "Hello word   , esse e meu primeiro site em Python"

@app.route("/secundaria")
def secundaria():
    return "Essa e a segunda pagina do site"
 

#colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)
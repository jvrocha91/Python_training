from flask import Flask, render_template

app = Flask(__name__)

#criar a 1 pagina do site 
#route-> link
#funcao -> O que voce que exibir na pagina

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/secundaria")
def secundaria():
    return render_template("secundaria.html")
 

#colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)
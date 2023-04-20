from flask import Flask, render_template, request

app = Flask(__name__)

#criar a 1 pagina do site 
#route-> link
#funcao -> O que voce que exibir na pagina

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    nome = request.form['nome']
    cigarros = int(request.form['cigarros'])
    anos = int(request.form['anos'])

    tempo_perdido = (10 * cigarros * anos * 365)
    tempo_perdido_dias = (tempo_perdido / 1440)

    return render_template('resultado.html', nome=nome, tempo_perdido_dias=tempo_perdido_dias)

if __name__ == '__main__':
    app.run(debug=True)
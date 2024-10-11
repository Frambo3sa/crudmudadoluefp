from flask import Flask, render_template, request, redirect 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GELADO'

jogos = []

@app.route('/') # Rota raiz /
def index():
    return render_template("index.html", jogos = jogos)

@app.route('/criar', methods=['POST']) # Rota /criar
def create():
    nome = request.form['nome']
    jogos.append(nome)
    return redirect('/')

@app.route('/alterar', methods=['POST']) # rota /alterar 
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    if old_name in jogos:
        index = jogos.index(old_name)
        jogos[index] = new_name
    return redirect('/')

@app.route('/apagar', methods=['POST']) # rota /apagar
def delete():
    nome = request.form['nome'] 
    if nome in jogos:
        jogos.remove(nome)
    return redirect('/')



if __name__== '__main__':
    app.run(debug=True)

from flask import Flask, request

from random import randint

app = Flask(__name__)

itens = ('PEDRA', 'PAPEL', 'TESOURA')


@app.route('/')
def inicio():
    return '''
    <h1>🎮 PEDRA, PAPEL E TESOURA</h1>

    <p>Escolha sua jogada:</p>

    <form action="/jogar" method="post">
        <button name="jogador" value="0">PEDRA</button>
        <button name="jogador" value="1">PAPEL</button>
        <button name="jogador" value="2">TESOURA</button>
    </form>
    '''


@app.route('/jogar', methods=['POST'])
def jogar():

    jogador = int(request.form['jogador'])
    computador = randint(0, 2)

    if jogador == computador:
        resultado = 'EMPATE!'

    elif jogador == 0 and computador == 2:
        resultado = 'JOGADOR VENCEU!'

    elif jogador == 1 and computador == 0:
        resultado = 'JOGADOR VENCEU!'

    elif jogador == 2 and computador == 1:
        resultado = 'JOGADOR VENCEU!'

    else:
        resultado = 'COMPUTADOR VENCEU!'

    return f'''
    <h1>🎮 PEDRA, PAPEL E TESOURA</h1>

    <p>Computador jogou: <strong>{itens[computador]}</strong></p>
    <p>Você jogou: <strong>{itens[jogador]}</strong></p>

    <h2>{resultado}</h2>

    <a href="/">JOGAR NOVAMENTE</a>
    '''


app.run(debug=True)

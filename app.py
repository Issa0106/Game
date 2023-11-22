from flask import Flask, render_template, request

app = Flask(__name__)
players = {'player1': None, 'player2': None}

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/join_game', methods=['POST'])
def join_game():
    global players

    player_name = request.form.get('player_name')
    enemy_name = request.form.get('enemy_name')

    if player_name and enemy_name:
        players['player1'] = player_name
        players['player2'] = enemy_name
        return render_template('game.html', player_name=player_name, enemy_name=enemy_name)
    else:
        return "Veuillez entrer les deux noms de joueurs."

if __name__ == '__main__':
    app.run(debug=True)

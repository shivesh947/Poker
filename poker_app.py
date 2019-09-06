from flask import Flask, render_template
import random
import Poker

app = Flask(__name__)


@app.route('/')
def wellcomw():
    card = []
    card = ['AH', 'KH', 'QH', 'JH', '10H','9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
            'AD', 'KD', 'QD', 'JD', '10D','9D','8D', '7D', '6D', '5D', '4D', '3D', '2D',
            'AS', 'KS', 'QS', 'JS', '10S','9S','8S', '7S', '6S', '5S', '4S', '3S', '2S',
            'AC', 'KC', 'QC', 'JC', '10C','9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']
    random.shuffle(card)
    play0 = []
    play2 = []
    for i in range(0, 5):
        play0.append(card[i])
    for i in range(5, 10):
        play2.append(card[i])

    res1=Poker.check(play0)
    res2=Poker.check(play2)
    return render_template('home.html', name=card,res1=res1,res2=res2)


if __name__ == '__main__':
    app.run(debug=True)
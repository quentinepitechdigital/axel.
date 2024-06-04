from flask import Flask

app = Flask(__name__)

@app.route('/get_btc')
def get_btc():
    with open("json/btc.json") as btc_file:
        btc_json = btc_file.read()
    return btc_json

@app.route('/get_gold')
def get_gold():
    with open("json/gold.json") as gold_file:
        gold_json = gold_file.read()
    return gold_json

@app.route('/get_sp500')
def get_sp500():
    with open("json/sp500.json") as sp500_file:
        sp500_json = sp500_file.read()
    return sp500_json

if __name__ == '__main__':
    app.run(debug=True)
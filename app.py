import logging

from flask import Flask
from database import Database as db
from tools.generation import Generate

app = Flask(__name__)


@app.route('/sensors', methods=['GET'])
def sensors_get():  # put application's code here
    gen = Generate()
    gen.generate_data(100)
    return db.get_sensors()

@app.route('/sensors/<sensor>', methods=['GET'])
def sensors_get_correct(sensor):
    return db.get_sensors(sensor)

@app.route('/status', methods=['GET'])
def status_get():
    return [["Idle", "Sun, 20 Apr 2025 12:26:39 GMT", "Auto"], ["Toggle_Light","Sun, 20 Apr 2025 12:26:39 GMT", "Root"]]

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    # Ganti dengan logika untuk mendapatkan data cuaca
    weather_data = {
        'temperature': 25,
        'humidity': 60,
        'description': 'Clear sky'
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
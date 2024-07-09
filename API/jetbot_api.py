from flask import Flask, request, jsonify

app = Flask(__name__)

# Örnek JetBot durumu
jetbot_status = {
    'jetbot_status':'waiting',
    'battery_level': 80,
    'connection_status': 'not connected'
}

@app.route('/connect_jetbot', methods=['GET'])
def connect_jetbot():
    jetbot_status["connection_status"] ='Connected'
    return jsonify(jetbot_status)

@app.route('/disconnect_jetbot', methods=['GET'])
def disconnect_jetbot():
    jetbot_status["connection_status"] ='not connected'
    return jsonify(jetbot_status)

@app.route('/get_jetbot_status', methods=['GET'])
def get_jetbot_status():
    return jsonify(jetbot_status)

@app.route('/update_jetbot_status', methods=['POST'])
def update_jetbot_status():
    data = request.get_json()
    # JetBot durumu güncelleme işlemleri
    jetbot_status['battery_level'] = data.get('battery_level', jetbot_status['battery_level'])
    jetbot_status['connection_status'] = data.get('connection_status', jetbot_status['connection_status'])
    return jsonify({'message': 'JetBot status updated successfully'})

@app.route('/command_jetbot', methods=['POST'])
def command_jetbot():
    data = request.get_json()
    command = data.get('command')

    # Burada JetBot'a komut gönderme işlemleri yapılacak

    return jsonify({'message': 'Command sent to JetBot'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

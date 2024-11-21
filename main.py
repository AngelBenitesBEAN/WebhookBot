from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 4000

@app.route('/webhook', methods=['POST'])
def webhook():
    message_data = request.json  # Obtiene el cuerpo del mensaje como JSON

    print("Mensaje recibido: ", message_data)

    if 'messages' in message_data:
        for message in message_data['messages']:
            print(f"Mensaje de {message['from']}: {message['body']}")

    return jsonify({'status': 'OK'}), 200


if __name__ == '__main__':
    app.run(port=PORT)
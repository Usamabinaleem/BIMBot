# from flask import Flask, request, jsonify, render_template
# import requests
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('chatbot.html')
#
# @app.route('/send', methods=['POST'])
# def send():
#     user_message = request.json['message']
#     # Define the Rasa endpoint for sending messages
#     rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
#     # Prepare the payload in the format that Rasa expects
#     payload = {
#         "sender": "user",  # Can use session id or any unique identifier
#         "message": user_message
#     }
#     # Send the POST request to Rasa and get the response
#     response_from_rasa = requests.post(rasa_url, json=payload)
#     # Extract the text from Rasa's response
#     if response_from_rasa.ok:
#         bot_response = response_from_rasa.json()[0]['text']
#         return jsonify(message=bot_response)
#     else:
#         return jsonify(message="I'm having trouble understanding you.")
#
# if __name__ == '__main__':
#     app.run(debug=True)



#File upload code

# import requests
# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import os
#
# app = Flask(__name__)
#
# # Configure the upload folder
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
#
# @app.route('/')
# def home():
#     return render_template('chatbot.html')
#
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({"message": "No file part"}), 400
#
#     file = request.files['file']
#
#     if file.filename == '':
#         return jsonify({"message": "No selected file"}), 400
#
#     if file:
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)
#         return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200
#
#
# @app.route('/send', methods=['POST'])
# def send():
#     user_message = request.json['message']
#     rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
#     payload = {
#         "sender": "user",
#         "message": user_message
#     }
#     response_from_rasa = requests.post(rasa_url, json=payload)
#     if response_from_rasa.ok:
#         bot_response = response_from_rasa.json()[0]['text']
#         return jsonify(message=bot_response)
#     else:
#         return jsonify(message="I'm having trouble understanding you.")
#
#
# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True)



# import requests
# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import os
#
# app = Flask(__name__)
#
# # Configure the upload folder
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# # Function to delete existing IFC files
# def delete_existing_ifc_files():
#     for filename in os.listdir(app.config['UPLOAD_FOLDER']):
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         try:
#             if os.path.isfile(file_path) or os.path.islink(file_path):
#                 os.unlink(file_path)
#         except Exception as e:
#             print(f'Failed to delete {file_path}. Reason: {e}')
#
# @app.route('/')
# def home():
#     return render_template('chatbot.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # Delete any existing IFC files before saving the new one
#     delete_existing_ifc_files()
#
#     if 'file' not in request.files:
#         return jsonify({"message": "No file part"}), 400
#
#     file = request.files['file']
#
#     if file.filename == '':
#         return jsonify({"message": "No selected file"}), 400
#
#     if file:
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)
#         return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200
#
# @app.route('/send', methods=['POST'])
# def send():
#     user_message = request.json['message']
#     rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
#     payload = {
#         "sender": "user",
#         "message": user_message
#     }
#     response_from_rasa = requests.post(rasa_url, json=payload)
#     if response_from_rasa.ok:
#         bot_response = response_from_rasa.json()[0]['text']
#         return jsonify(message=bot_response)
#     else:
#         return jsonify(message="I'm having trouble understanding you.")
#
# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True)
#
#
#
#

import time
import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for
import os

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Function to delete existing IFC files
def delete_existing_ifc_files():
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


@app.route('/')
def home():
    return render_template('chatbot.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # Delete any existing IFC files before saving the new one
    delete_existing_ifc_files()

    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200


from flask import Response

@app.route('/send', methods=['POST'])
def send():
    user_message = request.json['message']
    rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
    payload = {
        "sender": "user",
        "message": user_message
    }

    # Send the request to Rasa
    response_from_rasa = requests.post(rasa_url, json=payload)

    if response_from_rasa.ok:
        bot_responses = response_from_rasa.json()
        full_response = "\n".join([resp['text'] for resp in bot_responses])

        def generate():
            for char in full_response:
                yield char
                time.sleep(0.01)  # Adjust the speed of the typing effect
            yield ''  # To ensure the generator closes properly

        return Response(generate(), content_type='text/plain')
    else:
        return jsonify(message="I'm having trouble understanding you.")



if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

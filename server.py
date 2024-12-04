from flask import Flask, request, jsonify
import json
import random
import requests

app = Flask(__name__)
backendServer = 'https://d665-182-209-39-164.ngrok-free.app'
backendServerSync = backendServer + '/api/v1/sync/request?type=sync'
backendServerUpgr = backendServer + '/api/v1/sync/request?type=upgr'
backendServerRepl = backendServer + '/api/v1/sync/request?type=repl'


# Function to extract action.parameters(parameters required for response)
def save_action_parameters(request_data):
    parameters = {}
    action_parameters = request_data.get('action', {}).get('parameters', {})
    for key, value in action_parameters.items():
        parameters[key] = value
    return parameters



@app.route('/action.wine_cellar_setup', methods=['POST'])
def wine_cellar_setup():
    try:
        response_data = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {}
        }
        response_data = json.dumps(response_data, indent=2)
        return response_data
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/action.wine_cellar_setup_complete', methods=['POST'])
def wine_cellar_setup_complete():
    try:
        response_data = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {}
        }
        response_data = json.dumps(response_data, indent=2)
        return response_data
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 3. 연말 영화 시나리오
@app.route('/action.winter_movie_mode', methods=['POST'])
def winter_movie_mode():
    try:
        response_data = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {}
        }
        response_data = json.dumps(response_data, indent=2)
        return response_data
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 4. 취침 시나리오
@app.route('/action.sleep_mode', methods=['POST'])
def sleep_mode():
    try:
        response_data = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {}
        }
        response_data = json.dumps(response_data, indent=2)
        return response_data
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
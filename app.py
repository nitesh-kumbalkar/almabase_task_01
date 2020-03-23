from flask import Flask, request, abort, jsonify
from model.request import RequestSchema
from src.service import process_request
app = Flask(__name__)

req_schema = RequestSchema()

@app.route('/api', methods=['POST'])
def github_api():
    # Payload validation
    payload = request.get_json()
    errors = req_schema.validate(payload)
    if errors:
        return jsonify(errors), 400
    else:
        return jsonify(process_request(payload)), 200

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')

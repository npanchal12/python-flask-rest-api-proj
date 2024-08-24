from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/codeworld', methods=['GET'])
def helloworld():
    """Returns a welcome message."""
    data = {"data": "Welcome to Nimesh TechWorld"}
    return jsonify(data), 200

@app.route('/greet/<string:name>', methods=['GET'])
def greet(name):
    """Returns a personalized greeting."""
    data = {"message": f"Hello, {name}! Welcome to Nimesh TechWorld."}
    return jsonify(data), 200

@app.route('/reverse', methods=['POST'])
def reverse_string():
    """Reverses a string sent in the request body."""
    content = request.json
    if 'string' not in content:
        return jsonify({"error": "No 'string' key in JSON body"}), 400

    original_string = content['string']
    reversed_string = original_string[::-1]
    return jsonify({"original": original_string, "reversed": reversed_string}), 200

@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    """Handles 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    import os
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 9001))
    app.run(host=host, port=port)

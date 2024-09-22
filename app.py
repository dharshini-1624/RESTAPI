from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Helper function to extract highest lowercase alphabet
def get_highest_lowercase_alphabet(input_list):
    lowercases = [ch for ch in input_list if ch.islower()]
    return max(lowercases) if lowercases else None

# POST method for /bfhl
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', None)
    
    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Get highest lowercase alphabet
    highest_lowercase_alphabet = get_highest_lowercase_alphabet(alphabets)
    
    # Handle file (if provided)
    file_valid = False
    file_mime_type = None
    file_size_kb = None
    if file_b64:
        try:
            decoded_file = base64.b64decode(file_b64)
            file_size_kb = len(decoded_file) / 1024
            # Assuming a common MIME type like image/png, adjust logic based on file inspection
            file_mime_type = "image/png"
            file_valid = True
        except Exception as e:
            file_valid = False
    
    # Return the response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with dynamic data
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }
    return jsonify(response)

# GET method for /bfhl
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)

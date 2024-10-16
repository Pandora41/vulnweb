from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Base directory where files are stored
BASE_DIR = os.path.abspath(".\\file")
print(f"Base directory: {BASE_DIR}")

@app.route('/readfile', methods=['GET'])
def read_file():
    filename = request.args.get('filename')
    
    # Debug: Print the filename and request to see if the route is being hit
    print(f"Requested filename: {filename}")

    # Check if the filename is not None
    if not filename:
        return "No filename provided", 400

    # Join the file path (intentionally vulnerable to path traversal)
    file_path = os.path.join(BASE_DIR, filename)
    
    # Debug: Print the file path to check if it's correct
    print(f"Full file path: {file_path}")

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the file content and return it
        with open(file_path, 'r') as file:
            return file.read(), 200
    else:
        return f"File {filename} not found.", 404

if __name__ == "__main__":
    app.run(debug=True)

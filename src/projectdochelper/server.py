from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

@app.route('/docs/<path:filename>')
def serve_docs(filename):
    return send_from_directory(app.config['DOCS_PATH'], filename)

@app.route('/append', methods=['POST'])
def append_requirement():
    data = request.json
    new_requirement = data.get('requirement', '')
    if new_requirement:
        doc_path = os.path.join(app.config['DOCS_PATH'], 'ProjectRequirements.md')
        with open(doc_path, 'a') as f:
            f.write(f"\n\n### 新需求\n{new_requirement}")
        return jsonify({"message": "需求已追加"}), 200
    return jsonify({"error": "未提供需求"}), 400

def start_service(path):
    app.config['DOCS_PATH'] = path
    app.run(host='0.0.0.0', port=5000)
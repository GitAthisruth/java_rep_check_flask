from flask import Flask, request, jsonify,render_template
from utils.dependency_check import dependency_check
import json

app = Flask(__name__)

folder_path = "C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_filename', methods=['POST'])
def upload_filename():
    try:
        if request.is_json:
            filename = request.form.get('filename')
        else:
            filename = request.form.get('filename')
       
        result = dependency_check(filename, folder_path)

        if isinstance(result, str):
            result = json.loads(result)
            
        return jsonify({'message': 'Dependency check completed', 'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

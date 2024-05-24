from flask import Flask, render_template, request, jsonify
import os
import imagel

app = Flask(__name__)
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')

value = ''
@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/new')
def about():
    return render_template ('new.html')

@app.route('/run', methods=['GET', 'POST'])
def get():
    # CODE FROM CHAT GPT
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        # Create the 'uploads' directory if it doesn't exist
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        # Save the file to the 'uploads' directory
        file_path = os.path.join(UPLOADS_DIR, file.filename)
        try:
            file.save(file_path)
        except Exception as e:
            return f'Failed to save file: {str(e)}', 500
        
        return imagel.extract_color(file_path, 10)



app.run(debug=True)

'''
This file created frontend for the application
'''
# pylint: disable=C0103, E0401, R1710
import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from csvYaml import converter


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'

# Ensure the upload and processed directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route('/')
def upload_form():
    '''This path function renders the frontend'''
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    '''This path function is responsible for processing the file'''
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        processed_filename = process_file(file_path, filename)
        return redirect(url_for('uploaded_file', filename=processed_filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    '''This path function is triggered when file is uploaded'''
    return render_template('index.html', filename=filename)

@app.route('/download/<filename>')
def download_file(filename):
    '''This path function is triggered when file is processed and ready to be downloaded'''
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename, as_attachment=True)

def process_file(file_path, filename):
    '''This function invokes the csvYaml python module to perform conversion'''
    app.logger.info("Input file is: " + filename)
    output_file = converter(file_path, app.config['PROCESSED_FOLDER'])
    app.logger.info("output file is: " + output_file)
    return output_file

if __name__ == '__main__':
    app.run(debug=True)

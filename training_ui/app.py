from flask import Flask, jsonify, Response, request, render_template, flash, redirect

from resources.data_management import DataManagement
import requests
import sys
import os
import json
import secrets
import logging

app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./tmp"

secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/data_upload', methods=['GET', 'POST'])
def training_ui():
    return render_template("training_template.html")  # this method is called of HTTP method is GET, e.g., when browsing the link

@app.route('/upload_json_data', methods=['GET', 'POST'])
def upload_data():
    if request.method == "POST":
        # No file in request
        if 'training_data' not in request.files:
            print("No file in request", file=sys.stdout)
            sys.stdout.flush()
            return redirect(request.url)
        # Retrieve file
        data_file = request.files['training_data']
        # No file
        if data_file.filename == '':
            print("No file selected", file=sys.stdout)
            sys.stdout.flush()
            return redirect(request.url)

        request_path = os.environ['TRAINING_API']
        upload_endpoint = os.environ['UPLOAD_ENDPOINT']
        upload_url = "{0}/{1}".format(request_path, upload_endpoint)
        json_format = json.load(data_file)
        upload_request = requests.post(upload_url, json=json_format)
        # Flush stdout to print in console
        return redirect('/data_upload')
    return redirect('/data_upload')

app.run(host='0.0.0.0', port=5000)

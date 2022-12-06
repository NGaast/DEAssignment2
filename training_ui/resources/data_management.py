import argparse
import json

from flask import Flask, request, render_template

from typing_extensions import Self
from google.cloud import storage
import google.cloud.aiplatform as aip
import pandas as pd



class DataManagement:

    def __init__(self, project_id, bucket_id):
        self.project_id = project_id
        self.bucket_id = bucket_id

    def store_dataframe(self, file_name):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json_post = request.get_json()
            df = pd.DataFrame.from_dict(json_post)

            # Configure
            client = storage.Client(project=self.project_id)
            bucket = client.get_bucket(self.bucket_id)
            blob = bucket.blob(file_name)

            # Upload the locally saved model
            blob.upload_from_string(df.to_csv(index=False), content_type='application/json')
            return True
        return False

    def store_json(self, file, file_name):
        # Configure bucket
        client = storage.Client(project=self.project_id)
        bucket = client.get_bucket(self.bucket_id)
        blob = bucket.blob(file_name)

        # Upload the locally saved model
        blob.upload_from_string(file, content_type='application/json')
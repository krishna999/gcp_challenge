import os
import datetime
import csv
import requests

from google.cloud import storage

filename = 'coinmarketcap.csv'

def upload_blob(bucket_name, source_file_name, destination_blob_name):
  """Uploads a file to the bucket."""
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_filename(source_file_name)

  print('File {} uploaded to {}.'.format(
      source_file_name,
      destination_blob_name))
      
upload_blob('coinmarketcap-2018', filename, 'crypto.csv')
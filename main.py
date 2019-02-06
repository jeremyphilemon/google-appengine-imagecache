from flask import Flask, render_template, request
from requests_toolbelt.adapters import appengine
from google.cloud import storage

from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext import ndb

app = Flask(__name__)

BUCKET_NAME="jrmyphlmn"
FOLDER_NAME="images/"

@app.route('/')
def landing():
	appengine.monkeypatch()
	storage_client = storage.Client()
	bucket = storage_client.get_bucket(BUCKET_NAME)
	blobs = bucket.list_blobs()
	photos = []
	length_folder_name = len(FOLDER_NAME)
	for blob in blobs:
		if blob.name.startswith(FOLDER_NAME):
			photos.append(blob.name)
	cached_links = []
	for photo in photos[1:]:
		blob_key = blobstore.create_gs_key("/gs/"+BUCKET_NAME+"/"+FOLDER_NAME+photo[length_folder_name:])
		cached_links.append(images.get_serving_url(blob_key, secure_url=True))
	return render_template('landing.html', photos = photos, cached_links = cached_links)

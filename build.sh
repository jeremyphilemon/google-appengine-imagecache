#!/bin/bash
echo 'Hey, this will help you configure your appengine app for deploy.'
echo 'Name of the bucket: '
read BUCKET_NAME
echo -e 'Directory to the folder containing the image: \n(Example: if gs url is \033[0;35mgs://jrmyphlmn/images/dogs/ \033[0mthen your directory is \033[0;35mimages/dogs\033[0m)'
read FOLDER_NAME
sed -i '' 's/^BUCKET_NAME=.*/BUCKET_NAME="'${BUCKET_NAME}'"/g' main.py
sed -i '' 's/^FOLDER_NAME=.*/FOLDER_NAME="'${FOLDER_NAME}'\/"/g' main.py
gcloud app deploy app.yaml index.yaml
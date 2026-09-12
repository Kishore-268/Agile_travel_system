# Agile Travel System

## Run locally
pip install -r requirements.txt
python app.py

Open http://localhost:5000

## Docker
docker build -t agile-travel-system:latest .
docker rm -f agile-travel-container
docker run -d -p 5000:5000 --name agile-travel-container agile-travel-system:latest

## Jenkins
Use a Jenkins Pipeline with:
Pipeline script from SCM -> Git
Repository URL: your GitHub repository URL
Script Path: Jenkinsfile

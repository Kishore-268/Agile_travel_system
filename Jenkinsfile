pipeline {
    agent any

    stages {

        stage('Get Source Code') {
            steps {
                echo 'Getting Agile Travel System source code from GitHub'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Agile Travel System Docker Image'

                bat 'docker build -t agile-travel-system:latest .'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Starting Agile Travel System container'

                bat 'docker rm -f agile-travel-container 2>NUL || exit /B 0'

                bat 'docker run -d -p 5000:5000 --name agile-travel-container agile-travel-system:latest'
            }
        }
    }

    post {
        success {
            echo 'Agile Travel System CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}

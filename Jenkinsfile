pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials' // Ensure this ID matches your Jenkins credentials store
        IMAGE_NAME = 'jasminatm/lyrics-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/JasminaTM/Lyrics.git'
            }
        }

        stage('Build and Test') {
            steps {
                bat 'python -m venv venv && source venv/bin/activate'
                bat 'pip install --no-cache-dir -r requirements.txt'
                bat 'pytest'  // Ensure you have tests in your repo
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Login & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    bat 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5000:5000 --name lyrics-app $IMAGE_NAME'
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}

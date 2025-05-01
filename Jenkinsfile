pipeline {
    agent any

    environment {
        // Optional: you can define env variables here
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {

        stage('Git Clone') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/maze_runner_game']],
                    userRemoteConfigs: [[url: 'https://github.com/LazyCoderForU/docker-learning-only-python.git']]
                ])
            }
        }

        stage('Docker Teardown (if running)') {
            steps {
                script {
                    echo "Tearing down existing containers..."
                    bat "docker-compose down || exit 0"
                }
            }
        }

        stage('Build and Deploy Containers') {
            steps {
                script {
                    echo "Building and starting containers..."
                    bat "docker-compose up --build -d"
                }
            }
        }

    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}

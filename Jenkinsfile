pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'your-docker-registry' // TODO: Replace this with actual registry
        DOCKER_IMAGE_PREFIX = 'docker-learning-only-python'
    }

    stages {

        stage('Git Clone') {
            steps {
                git branch: 'maze_runner_game', url: 'https://github.com/LazyCoderForU/docker-learning-only-python.git'
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
                    bat 'docker-compose up -d'
                    // Add your test commands here
                    bat 'docker-compose down'
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

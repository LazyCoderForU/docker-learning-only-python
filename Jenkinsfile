pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'your-docker-registry' // Replace with your Docker registry
        DOCKER_IMAGE_PREFIX = 'docker-learning-only-python'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/LazyCoderForU/docker-learning-only-python.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    bat 'docker build -t %DOCKER_IMAGE_PREFIX%-game-logic -f Dockerfile.game_logic .'
                    bat 'docker build -t %DOCKER_IMAGE_PREFIX%-user-interaction -f Dockerfile.user_interaction .'
                    bat 'docker build -t %DOCKER_IMAGE_PREFIX%-real-time-updates -f Dockerfile.real_time_updates .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'docker-compose up -d'
                    // Add test commands here
                    bat 'docker-compose down'
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                script {
                    bat 'docker tag %DOCKER_IMAGE_PREFIX%-game-logic %DOCKER_REGISTRY%/%DOCKER_IMAGE_PREFIX%-game-logic'
                    bat 'docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE_PREFIX%-game-logic'

                    bat 'docker tag %DOCKER_IMAGE_PREFIX%-user-interaction %DOCKER_REGISTRY%/%DOCKER_IMAGE_PREFIX%-user-interaction'
                    bat 'docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE_PREFIX%-user-interaction'

                    bat 'docker tag %DOCKER_IMAGE_PREFIX%-real-time-updates %DOCKER_REGISTRY%/%DOCKER_IMAGE_PREFIX%-real-time-updates'
                    bat 'docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE_PREFIX%-real-time-updates'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            bat 'docker-compose down'
        }
    }
}

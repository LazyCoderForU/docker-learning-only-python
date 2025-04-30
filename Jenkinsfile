pipeline {
    agent any
    triggers {
        githubPush()
    }

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Explicitly specify the branch as 'main'
                git branch: 'maze_runner_game', url: 'https://github.com/LazyCoderForU/docker-learning-only-python.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install dependencies using pip
                bat 'python -m venv venv'
                bat './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Rebuild Docker Containers') {
            steps {
                bat 'docker compose down'
                bat 'docker compose up --build -d'
            }
        }

        stage('Test Application') {
            steps {
                // Add test commands here (e.g., curl to test endpoints)
                bat 'curl -f http://localhost:5100 || exit 1'
                bat 'curl -f http://localhost:5101 || exit 1'
                bat 'curl -f http://localhost:5102 || exit 1'
            }
        }
    }

    post {
        always {
            // Clean up Docker containers and resources
            bat 'docker compose down'
            bat 'docker system prune -f'
        }
    }
}

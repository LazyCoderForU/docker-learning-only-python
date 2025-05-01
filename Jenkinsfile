pipeline {
    agent any  // Use the appropriate agent, it could be a Windows node

    stages {
        stage('Git Checkout and Pull') {
            steps {
                // Ensure the correct branch is checked out and pull the latest changes
                bat 'git checkout maze_runner_game || git checkout -b maze_runner_game origin/maze_runner_game'
                bat 'git pull origin maze_runner_game'
            }
        }

        stage('Docker Compose Up') {
            steps {
                bat 'docker-compose up -d'  // Run Docker Compose to start services
            }
        }
    }
}

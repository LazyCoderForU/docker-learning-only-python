pipeline {
    agent any  // Use the appropriate agent, it could be a Windows node

    stages {
        stage('Git Checkout and Pull') {  // Stage to ensure the latest code is pulled from the repository
            steps {
                // Checkout the correct branch or create it if it doesn't exist, then pull the latest changes
                bat 'git checkout maze_runner_game || git checkout -b maze_runner_game origin/maze_runner_game'
                bat 'git pull origin maze_runner_game'
            } 
        }

        stage('Docker Compose Up') {  // Stage to build and start the Docker containers
            steps {
                // Run Docker Compose to start all services in detached mode
                bat 'docker-compose up -d'
            }
        }
    }
}

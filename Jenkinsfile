pipeline {
    agent any  // Use the appropriate agent, it could be a Windows node

    stages {
        stage('Git Pull') {
            steps {
                bat 'git pull'  // Using bat for Windows
            }
        }

        stage('Docker Compose Up') {
            steps {
                bat 'docker-compose up -d'  // Using bat for Windows
            }
        }
    }
}

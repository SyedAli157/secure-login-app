pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                // Use 'bat' instead of 'sh' for Windows Command Prompt execution
                bat 'docker build -t secure-app .'
            }
        }

        stage('Run Container') {
            steps {
                // Stops any previous container using port 5000 so the build doesn't crash
                bat 'docker rm -f secure-app-container || exit 0'
                // Spins up the new container cleanly
                bat 'docker run -d --name secure-app-container -p 5000:5000 secure-app'
            }
        }
    }
}
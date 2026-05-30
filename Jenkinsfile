pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t secure-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 secure-app'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Verify Docker Installation') {
            steps {
                script {
                    try {
                        sh 'docker --version'
                        sh 'docker info'
                    } catch (Exception e) {
                        error "Docker is not installed or not accessible."
                    }
                }
            }
        }
    }
}

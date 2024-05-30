pipeline {
    agent any

    stages {
        stage('Verify Docker Installation') {
            steps {
                script {
                    try {
                        sh 'which docker'
                        sh 'docker --version'
                        sh 'docker info'
                    } catch (Exception e) {
                        error "Docker is not installed or not accessible."
                    }
                }
            }
        }
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("alonaf800/worldofgames")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'docker-compose up -d'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python e2e.py'
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose down'
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

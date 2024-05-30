pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id') // Replace with your credentials ID
    }

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
                    // Remove existing container if it exists
                    sh '''
                    if [ "$(docker ps -aq -f name=worldofgames)" ]; then
                        docker rm -f worldofgames
                    fi
                    '''
                    // Run the new container
                    sh 'docker run -d -p 8777:8777 -v /Users/alonberger/.jenkins/workspace/world-of-games-pipeline/Scores.txt:/Scores.txt --name worldofgames worldofgames:latest'
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

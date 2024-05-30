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
                    // Stop and remove existing container if it exists
                    sh '''
                    if [ "$(docker ps -aq -f name=worldofgames)" ]; then
                        docker stop worldofgames || true
                        docker rm -f worldofgames || true
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
                    sh 'docker exec worldofgames python /app/e2e.py'
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop worldofgames || true'
                    sh 'docker rm -f worldofgames || true'
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        dockerImage.push()
                    }
                }
            }
        }
    }


pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "worldofgames:latest"
        DOCKER_HUB_REPO = "alonaf800/worldofgames"
    }

    stages {
        stage('Print Environment') {
            steps {
                sh 'printenv'
                sh 'which docker'
                sh 'docker --version'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker run -p 8777:8777 -v $WORKSPACE/Scores.txt:/Scores.txt --name worldofgames ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error "Tests failed"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop worldofgames'
                    sh 'docker rm worldofgames'
                    sh 'docker push ${DOCKER_HUB_REPO}'
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

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "worldofgames:latest"
        DOCKER_HUB_REPO = "alonaf800/worldofgames"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run("-p 8777:8777 -v $WORKSPACE/Scores.txt:/Scores.txt --name worldofgames")
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
                    docker.image(DOCKER_IMAGE).push(DOCKER_HUB_REPO)
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

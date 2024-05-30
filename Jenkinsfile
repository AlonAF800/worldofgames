pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("worldofgames:latest")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image("worldofgames:latest").run("-p 8777:8777 -v $PWD/Scores.txt:/Scores.txt --name worldofgames")
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
                    docker.image("worldofgames:latest").push("alonaf800/worldofgames:latest")
                }
            }
        }
    }
}

pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Verify Docker Installation') {
            steps {
                script {
                    sh 'which docker'
                    sh 'docker --version'
                    sh 'docker info'
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
                    sh 'docker build -t alonaf800/worldofgames .'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh 'docker ps -aq -f name=worldofgames | grep -q . && docker stop worldofgames && docker rm -f worldofgames || true'
                    sh 'docker run -d -p 8777:8777 -v /Users/alonberger/.jenkins/workspace/world-of-games-pipeline/Scores.txt:/Scores.txt --name worldofgames alonaf800/worldofgames:latest'
                    sleep 10 // Give the container some time to start
                    def status = sh(script: 'docker inspect --format={{.State.Status}} worldofgames', returnStdout: true).trim()
                    if (status != 'running') {
                        echo 'Container logs:'
                        sh 'docker logs worldofgames'
                        error('Container is not running')
                    }
                    // List the contents of /app directory
                    sh 'docker exec worldofgames ls -la /app'
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
    }
    post {
        always {
            script {
                sh 'docker stop worldofgames || true'
                sh 'docker rm -f worldofgames || true'
            }
        }
    }
}

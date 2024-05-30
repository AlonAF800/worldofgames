pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        def app = docker.build("alonaf800/worldofgames")
                    }
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh 'docker ps -aq -f name=worldofgames | grep -q . && docker stop worldofgames && docker rm -f worldofgames || true'
                    sh 'docker run -d -p 8777:8777 -v /Users/alonberger/.jenkins/workspace/world-of-games-pipeline/Scores.txt:/Scores.txt --name worldofgames alonaf800/worldofgames:latest'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'sleep 5' // Give container some time to start
                    sh 'docker exec worldofgames python /app/e2e.py'
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

pipeline {
    agent {
        label 'uat'
    }
    stages {
        stage('SCM Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'd3f1ace9-cc86-432d-a9e7-5c1b607ed1b9', url: 'https://github.com/omfystest/pythonapp.git']])
            }
        }
        stage('Clean Old Images') {
            steps {
                sh 'sudo docker-compose down'
                sh 'sudo docker image rm pythonsimple_action_server'
                sh 'sudo docker image rm pythonsimple_rasa'
            }
        }
        stage('Build Image') {
            steps {
                sh 'sudo docker-compose up -d --build'
            }
        }
    }
}

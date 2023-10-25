def pipelineStages = {
    stage('Checkout') {
        steps {
            checkout scm
        }
    }

    stage('Install Requirements') {
        steps {
            bat 'python --version'
            bat 'pip install --user -r requirements.txt'
        }
    }

    stage('Run Tests') {
        steps {
            bat 'python tests.py'
        }
    }
}

pipeline {
    agent any
    stages {
        script {
            pipelineStages()
        }
    }
}

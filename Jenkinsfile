pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {

                checkout scm
            }
        }
        
        stage('Install Requirements') {
            steps {
                sh "python3 --version"
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {

                sh 'python3 tests.py'
            }
        }
    }
    

}

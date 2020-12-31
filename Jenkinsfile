pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh '''
                    cd /
                    mkdir jenkins_test1
                    cd jenkins_test
                    echo "this is my first test" >> test1.txt
                '''
            }
        }
    }
}
pipeline {
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh '''
                    cd /
                    bash jenkins_test.sh
                '''
            }
        }
    }
}
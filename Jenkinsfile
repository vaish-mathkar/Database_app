pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python ../Flaskapp/app.py'
            }
        
            post {
                success {
                    echo 'python app running'
                }
           
            }
        }
    }
}

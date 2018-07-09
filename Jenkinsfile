pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 ../Flaskapp/app.py'
            }
        
            post {
                success {
                    echo 'python app running'
                }
           
            }
        }
    }
}

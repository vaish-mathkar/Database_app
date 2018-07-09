pipeline {
    agent { label 'docker' }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile Flaskapp/app.py'
            }
        
            post {
                success {
                    echo 'python app running'
                }
           
            }
        }
    }
}

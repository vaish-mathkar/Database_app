pipeline {
    agent all
    stages {
        stage('Build') {
            steps {
                sh 'sh app.sh'
            }
        
            post {
                success {
                    echo 'python app running'
                }
           
            }
        }
    }
}

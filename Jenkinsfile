pipeline {
    agent any

    environment {
        INPUT_DATE = "${env.INPUT_DATE}"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t first_job1 .'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    sh 'docker run -e INPUT_DATE="$INPUT_DATE" first_job1'
                }
            }
        }
    }
}

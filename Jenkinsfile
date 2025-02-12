pipeline {
    agent any

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
                    sh 'docker run -e INPUT_DATE="$INPUT_DATE" --rm  first_job1'
                }
            }
        }
    }
}

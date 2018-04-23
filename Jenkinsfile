pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'docker build --tag flask-application-image .'
                sh 'docker run -p 5000:5000 -d --name drumilflaskapplication:${env.BUILD_ID} flask-application-image:latest'
            }
        }

        stage('Testing'){
            steps{
                echo 'Testing...'
            }
        }

        stage('Deploy'){
            steps{
                echo 'Deploying...'
            }
        }
    }
}
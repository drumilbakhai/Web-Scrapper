pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'docker build --tag flask-application-image .'
                sh 'docker container rm -f flaskapplicationcontainer'
                sh "docker run -p 5000:5000 -d --name flaskapplicationcontainer flask-application-image:latest"
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
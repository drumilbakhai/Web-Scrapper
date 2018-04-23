pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'docker build --tag flask-application-image .'
                sh 'docker ps -f name=flaskapplicationcontainer -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=flaskapplicationcontainer -q | xargs -r docker container rm'
                sh "docker run -p 5000:5000 -d --name flaskapplicationcontainer flask-application-image:latest"
            }
        }

        stage('Testing'){

            agent{
                docker{
                    image 'qnib/pytest'
                }
            }

            steps{
                echo 'py.test --verbose unit_tests.py'
            }
            post{
                always{
                    echo 'Success in Testing'
                }
            }
        }

        stage('Deploy'){
            steps{
                echo 'Deploying...'
            }
        }
    }
}
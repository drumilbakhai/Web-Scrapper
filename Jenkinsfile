node{
    checkout scm
    def app

        stage('Build'){
            sh 'docker build --tag flask-application-image .'
            app = docker.build("flask-application-image:${env.BUILD_ID}", ".")
        }

        stage('Testing'){

            echo 'Success in Testing'

        }

        stage('Deploy'){

            echo 'Deploying...'
            sh 'docker ps -f name=flaskapplicationcontainer -q | xargs --no-run-if-empty docker container stop'
            sh 'docker container ls -a -fname=flaskapplicationcontainer -q | xargs -r docker container rm'
            sh "docker run -p 5000:5000 -d --name flaskapplicationcontainer flask-application-image:latest"

        }

}
pipeline {
    agent any
    
    stages {
        stage('Verify Tools') {
            steps {
                sh '''
                git --version
                docker --version
                docker-compose --version
                python3 --version
                pip --version
                '''
            }
        }
        stage('Start') {
            steps {
                echo 'Starting ... '
                // force stop docker and clean up
                sh "docker system prune -af"
                // re-download everything
                sh "docker build -t flask1 $WORKSPACE"
                // Run flask docker container.
                sh "docker-compose -f $WORKSPACE/Docker-Compose.yaml up -d"
            }
        }
//         stage('Finisehd') {
//             steps {
//                 echo 'Ending ... '
//             }
//         }
    }
    
    post {
        always {
            discordSend webhookURL: 'https://discord.com/api/webhooks/994018555341307966/V-Or2AnFnDNpfHa7slRrl2S0rhdybzYSnDNzKHVHgnKxJHCWG8iXWVQAPNjsa8hvHJ_q',
                        enableArtifactsList: false, scmWebUrl: '',
                        image: '', thumbnail: '',        
                        title: JOB_NAME, link: env.BUILD_URL,
                        description: 'The Current Build was a ${currentBuild.currentResult}',
                        footer: 'Jenkins Pipeline Build',
                        result: currentBuild.currentResult
        }
        success {
            mail to: 'Chris.Barnes.2000@me.com',
            subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A Success",
            body: "Please go to ${BUILD_URL} and verify the build"
        }
        failure {
            mail to: 'Chris.Barnes.2000@me.com',
            subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Failed",
            body: "Please go to ${BUILD_URL} and verify the build"
        }
    }
}

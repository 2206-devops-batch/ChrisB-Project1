pipeline {
    environment {
        registry = "chrisbarnes2000/project1"
        registrycredential = 'docker-hub-login'
        dockerimage = ''
    }
    agent any
    
    stages {
        stage("Verify Tools") {
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
        stage("Test") {
            when {
                expression {
                    BRANCH_NAME == "test"
                }
            }
            steps {
                sh "python3 -m pytest app-test.py"
            }
        }
        stage("Start") {
            steps {
                echo "Starting ... "
                sh "docker system prune -af"
                sh "docker-compose up --build -d -f $WORKSPACE/Docker-Compose.yaml"
                echo "Please Visit --> $JENKINS_URL:5000"
            }
        }
    }
    
    post {
        always {
//             emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n",
//                 recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
//                 subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            
            discordSend webhookURL: "https://discord.com/api/webhooks/994018555341307966/V-Or2AnFnDNpfHa7slRrl2S0rhdybzYSnDNzKHVHgnKxJHCWG8iXWVQAPNjsa8hvHJ_q",
                        enableArtifactsList: false, scmWebUrl: "",
                        image: "", thumbnail: "",        
                        title: JOB_NAME, link: env.BUILD_URL,
                        description: "Please Visit --> ${JENKINS_URL}:5000",
                        footer: "Jenkins Pipeline Build was a ${currentBuild.currentResult}",
                        result: currentBuild.currentResult
        }
        success {
            mail to: "Chris.Barnes.2000@me.com",
            subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A Success",
            body: "Please go to ${BUILD_URL} and verify the build"
            
             when {
                expression {
                    BRANCH_NAME == "main"
                }
            }
            steps {
                echo "Deploying ... "
                script {
                    // reference: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/
                    img = registry + ":${env.BUILD_ID}"
                    // reference: https://docs.cloudbees.com/docs/admin-resources/latest/plugins/docker-workflow
                    dockerImage = docker.build("${img}")
                    docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
                        // push image to registry
                        dockerImage.push()
                    }
                }
            }
        }
        failure {
            mail to: "Chris.Barnes.2000@me.com",
            subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Failed",
            body: "Please go to ${BUILD_URL} and verify the build"
        }
    }
}

pipeline {
  agent any
  stages {
    stage("Start Web Server") {
      steps {
        echo "Starting ... "
        sh "docker system prune -af"
        sh "docker build -t flask-image ."
        sh "docker run -d -p 5000:5000 --rm --name flask-container flask-image"
        echo "Please Visit --> $BASE_URL:5000"
      } // steps
    } // start
  } // stages
  post {
    always {
      
      mail to: "Chris.Barnes.2000@me.com",
           subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A ${currentBuild.currentResult}",
           body: "Please go to ${BUILD_URL} and verify the build"
      
      discordSend webhookURL: "https://discord.com/api/webhooks/994018555341307966/V-Or2AnFnDNpfHa7slRrl2S0rhdybzYSnDNzKHVHgnKxJHCWG8iXWVQAPNjsa8hvHJ_q",
                  enableArtifactsList: false, scmWebUrl: "",
                  image: "", thumbnail: "",        
                  title: JOB_NAME, link: env.BUILD_URL,
                  description: "Please Visit --> ${BASE_URL}:50000",
                  footer: "Jenkins Pipeline Build was a ${currentBuild.currentResult}",
                  result: currentBuild.currentResult
    } // always
    success {
      steps {
        docker push
      }
    } // success
  } // post
} // pipeline

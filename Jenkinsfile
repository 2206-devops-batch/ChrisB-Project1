pipeline {
  agent any
  stages {
    stage("Verify Tools") {
      steps {
        sh '''
          git --version
          pip --version
          docker --version
          python3 --version
          docker-compose --version
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
    stage("Start Web Server") {
      steps {
        echo "Starting ... "
        sh "docker system prune -af"
        sh "docker build -t flask-image ."
        sh "docker run -d -p 5000:5000 --rm --name flask-container flask-image"
        echo "Please Visit --> $BASE_URL:5000"
      } // steps
    } // start
    stage('Deploy Image') {
      steps{
        script {
          def customImage = docker.build("${JOB_NAME}:${BUILD_NUMBER}")
          customImage.push()
//           docker.withRegistry( '', registryCredential ) {
//             customImage.push()
//           }
        } // script
      } // steps
    } // deploy
    stage('Remove Unused Images') {
      steps{
        sh "docker rmi ${JOB_NAME}:${BUILD_NUMBER}"
      } // steps
    } // Remove
  } // stages
  post {
    always {
      
      mail to: "Chris.Barnes.2000@me.com",
           subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A ${currentBuild.currentResult}",
           body: "Please go to ${BUILD_URL} and verify the build"
      
      discordSend webhookURL: "https://discord.com/api/webhooks/994018555341307966/V-Or2AnFnDNpfHa7slRrl2S0rhdybzYSnDNzKHVHgnKxJHCWG8iXWVQAPNjsa8hvHJ_q",
                  enableArtifactsList: false, scmWebUrl: "",
                  image: "", thumbnail: "",        
                  title: JOB_NAME, link: BUILD_URL,
                  description: "Please Visit --> ${BASE_URL}:50000",
                  footer: "Jenkins Pipeline Build was a ${currentBuild.currentResult}",
                  result: currentBuild.currentResult
    } // always
  } // post
} // pipeline

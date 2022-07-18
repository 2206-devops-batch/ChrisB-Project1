pipeline {
  environment {
    DOCKERHUB_CREDENTIALS=credentials("DOCKER_AUTH_ID")
    registry = "chrisbarnes2000"
    repository = "project-1"

    container = "flask-container"
    version = "latest"

    path = "${registry}/${repository}"
    path_current_build = "${path}:${BUILD_NUMBER}"
  } // environment


  agent any


  stages {
    stage("Verify Devops-Setup") {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }


    stage("Prune Docker Data") {
      steps {
        sh "docker kill ${container}"
        sh "docker system prune -af --volumes"
      }
    }


    stage("Pytest Latest Changes (for NEW - Green Deployment)") {
      steps {
        sh "pytest app-test.py"
      }
    }


    stage("Rebuild & Push To Docker Hub") {
      steps {
        sh "docker build -t ${path_current_build} ." // chrisbarnes2000/project-1:35
        sh "docker push ${path_current_build}"
      }
    }


    stage("Start Web Server") {
      steps {
        echo "\n\nStarting Web Server... \n"
        sh "docker run -d -p 5000:5000 --rm --name ${container} ${path_current_build}"
        echo "Please Visit --> $BASE_URL:5000"
      } // steps
    } // start


    stage("Pull Latest Version From Docker Hub") {
      steps {
        sh "docker pull ${path_current_build}" // chrisbarnes2000/project-1:latest
      }
    }


    stage("Run Smoke Tests Against The Container") {
      steps {
        echo "Please Visit --> $BASE_URL:5000"
        sh "curl http://localhost:5000/ | jq"
      }
    }


  } // stages

  post {
    always {
      // Clean up docker / Everything
      sh "docker system prune -af && docker logout"


      // Send Status Report To Email & Discord
      mail to: "Chris.Barnes.2000@me.com",
           subject: "Job ${JOB_NAME} (${BUILD_NUMBER}) Was A ${currentBuild.currentResult}",
           body: "Please go to ${BUILD_URL} and verify the build"

      discordSend webhookURL: "https://discord.com/api/webhooks/998320738769588224/4akFNyQItbFvUKmbGxJ-qMCyzMefF3QP4GbyNk73wry4_WfGPuDOWUlael_WN4_Yh677",
                  enableArtifactsList: false, scmWebUrl: "",
                  image: "", thumbnail: "",
                  title: JOB_NAME, link: BUILD_URL,
                  description: "Please Visit --> ${BASE_URL}:50000",
                  footer: "Jenkins Pipeline Build was a ${currentBuild.currentResult}",
                  result: currentBuild.currentResult
    } // always
  } // post
} // pipeline

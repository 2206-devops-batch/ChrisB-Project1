pipeline {
  environment {
    DOCKERHUB_CREDENTIALS=credentials('DOCKER_AUTH_ID')
    DOCKERHUB_REPO='chrisbarnes2000/project-1'
    TAG="${BUILD_NUMBER}" // 'latest'
  } // environment

  agent any

  stages {
    stage('ENV CHECK'){
      steps{
        // Login To Docker
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

        // sh 'docker-compose down --remove-orphans -v'
        sh 'docker kill ${(docker ps -q)}'

        // Clean The Docker ENV
        sh 'docker rm   ${(docker ps -a -q)}'
        sh 'docker rmi  ${(docker images -q)}'
        // sh 'docker rmi  ${(path_current_build)}'
        sh 'docker system prune -af --volumes'

        // Check The ENV Is Clean
        sh 'docker-compose ps -a'
        sh 'docker ps -a'
      }
    }
    stage('Build'){
      steps {
        echo '\n\nBUILDING... \n'

      }
    }
    stage('Test'){
      steps {
        echo '\n\nTESTING... \n'

      }
    }
    stage('Push'){
      steps {
        echo '\n\nPUSHING... \n'

      }
    }
    stage('Pull'){
      steps {
        echo '\n\nPULLING... \n'

      }
    }
    stage('Deploy'){
      steps {
        echo '\n\nDEPLOYING... \n'

      }
    }
  } // stages


  post {
    always {
      sh 'docker system prune -af && docker logout'

      mail to: "Chris.Barnes.2000@me.com",
           subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A ${currentBuild.currentResult}",
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

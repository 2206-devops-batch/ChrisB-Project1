pipeline {
    // Dockhub information needed to push image.
    environment {
        registry = "ohshoe/project1"
        registrycredential = 'docker-hub-login'
        dockerimage = ''
    }
    agent any

    stages {
      stage('Install Environment') {
        steps {
          // Get some code from a GitHub repository
          // git 'https://github.com/2206-devops-batch/ChrisB-Project1'
          // Run venv
          sh 'python3 -m venv .venv'
          sh '. .venv/bin/activate'
          // Install Dependencies
          sh 'pip install -r requirements-dev.txt'
        }
      }
      // stage('Test') {
      //   steps {
      //     // Run pytest
      //     sh 'python3 -m pytest app-test.py'
      //   }
      // }
      // stage('Build & Push Image To Dockerhub') {
      //   steps {
      //     script {
      //       // reference: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/
      //       // reference: https://docs.cloudbees.com/docs/admin-resources/latest/plugins/docker-workflow
      //       dockerImage = docker.build(registry + ":${env.BUILD_ID}")
      //       docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
      //         dockerImage.push()
      //       }
      //     }
      //   }
      // }
      // stage ('Deploy') {
      //   steps {
      //     sh 'docker system prune -af'
      //     // sh "docker build -t Project1 $WORKSPACE"
      //     sh 'docker-compose up --build -d'
      //   }
      // }
      // stage ('Discord') {
      //   steps {
      //     discordSend webhookURL: 'https://discord.com/api/webhooks/994018555341307966/V-Or2AnFnDNpfHa7slRrl2S0rhdybzYSnDNzKHVHgnKxJHCWG8iXWVQAPNjsa8hvHJ_q',
      //                 enableArtifactsList: false, scmWebUrl: '',
      //                 image: '', thumbnail: '',
      //                 title: 'Project1-${JOB_NAME}', link: env.BUILD_URL,
      //                 description: 'Jenkins Pipeline Build',
      //                 footer: 'Footer Text',
      //                 result: currentBuild.currentResult
      //   }
      // }
    }

    // post {
    //     success {
    //         mail to: 'Chris.Barnes.2000@me.com',
    //         subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Was A Success",
    //         body: "Please go to ${BUILD_URL} and verify the build"
    //     }
    //     failure {
    //         mail to: 'Chris.Barnes.2000@me.com',
    //         subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) Failed",
    //         body: "Please go to ${BUILD_URL} and verify the build"
    //     }
    // }
}

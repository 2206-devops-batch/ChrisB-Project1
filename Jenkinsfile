pipeline {
  agent any
  stages {
    stage("Start") {
      steps {
        echo "Starting ... "
        sh "docker system prune -af"
        sh "docker-compose up --build -d"
      }
    }
  }
}

pipeline {
  agent any
  stages {
    stage("Start") {
      steps {
        echo "Starting ... "
        sh "docker system prune -af"
        sh "docker build -t flask-image ."
        sh "docker run -p 5000:5000 --rm --name flask-container flask-image"
//         sh "docker images -a | grep 'flask'"
      } // steps
    } // start
  } // stages
} // pipeline

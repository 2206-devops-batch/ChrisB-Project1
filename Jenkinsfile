pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/2206-devops-batch/ChrisB-Project1'
                // Set Up A Virtual Environment (.venv)
                sh 'python3 -m venv .venv && . .venv/bin/activate'
                // Install Pip & Requirements
                sh 'python3 install -U pip && pip install -r requirements.txt'
            }
        }
        // stage('Test'){
        //     steps {
        //         // Run pytest
        //         sh 'python3 -m pytest app_test.py'
        //     }
        // }
        stage ('Deploy') {
            // steps{
            //     sh 'cd ChirsB-Project1 && git pull'
            //     sh 'docker-compose up -d --build'
            // }
            steps {
                archiveArtifacts artifacts: "archiveArtifacts artifacts: '$WORKSPACE/*'", followSymlinks: false, onlyIfSuccessful: true
                // Force Stop Docker & Clean The Workspace
                sh "docker system prune -af"
                // re-download everything
                sh "docker build -t Project1 $WORKSPACE"
                // Run flask docker container.
                // sh "docker-compose -f $WORKSPACE/Docker-Compose.yaml up -d"
                sh "docker-compose up -d"
            }
        }
        stage ('Discord') {
            steps{
                discordSend description: '', enableArtifactsList: true, footer: '', image: '', link: 'env.BUILD_URL', result: 'SUCCESS', scmWebUrl: '', thumbnail: '', title: 'Project1', webhookURL: 'https://discord.com/api/webhooks/994018555341307966/V-Or2AnFnDNpfHa7slRrl2S0rhdybzYSnDNzKHVHgnKxJHCWG8iXWVQAPNjsa8hvHJ_q'
            }
        }
    }
}

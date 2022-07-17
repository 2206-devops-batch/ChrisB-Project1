- [x] create ec2
- [x] ssh into ec2
- [x] install git, docker

  ```bash
  sudo yum update -y
  sudo yum install git -y
  sudo yum sudo amazon-linux-extras install docker -y
  sudo service docker start
  sudo systemctl enable docker
  sudo chmod 666 /var/run/docker.sock
  sudo usermod -a -G docker ${USER}
  ```

- [x] verify git, docker, python, pip, & others are installed

  ```bash
  git --version
  docker info
  python3 --version
  pip3 --version
  ```

- [x] create Jenkins server from docker

  ```bash
  docker run --rm --name jenkins -u root -p 8080:8080 -p 50000:50000
  -v jenkins_home:/var/jenkins_home
  -v $(which docker):/usr/bin/docker
  -v /var/run/docker.sock:/var/run/docker.sock
  -v "$HOME":/home jenkins/jenkins:lts-jdk11
  ```

---

- [x] login into Jenkins - accept default plugins
- [x] add ec2, docker, github, discord
- [ ] configure system - credentials, email server, webhooks

  `GITHUB_AUTH_ID`, `GitHub Account` \
  `DOCKER_AUTH_ID`, `Docker Hub Account` \
  `GMAIL_AUTH_ID`, `Gmail Account` \
  `smtp.gmail.com`, `465`, `SSL`

- [x] create a new pipeline
- [x] link to github jenkinsfile
- [x] create a webhook & timed pull
- [x] run build
z
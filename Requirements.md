# Project 1

Automated CI pipeline for a web application (default: flask-demo)

- Example web applications:
  - flask-demo
  - any of your p0s (upgraded to a web app)
  - any public repo in any language (you should fork to your GitHub account)

A CI pipeline is a continuous integration tool and series of scripts which will be triggered upon a push to a GitHub repository, which will then begin a series of development lifecycle stages: build, test, deploy, etc. The trigger can be customized, so you may have more than a simple push to start your pipeline, but it must have a trigger for a push at least.

Presentation will be a simple demonstration of a change in a web application's code base which, when pushed to GitHub, will trigger an active pipeline you have deployed, and demonstrate the change after the automation process.

## Expected Tools:

- [ ] Docker & Docker Compose
- [x] GitHub or AWS CodeCommit
- [ ] Jenkins or AWS CodeBuild & CodeDeploy

## Nice to haves:

- [ ] Dockerized RDBMS
- [ ] Ansible script for setting up servers
- [ ] Quality gates (SonarQube/SonarCloud)
- [x] Issues tracker & Kanban board (GitHub Project Board, etc)
- [ ] Messaging system for the CI pipeline (email, Slack/Discord, etc)
- [ ] Separate and distinct build server, test server, and production server
- [ ] Vagrant or AWS CLI script for creating Virtualbox/AWS EC2 Cloud environments
- [ ] Fallback, when all else fails:
  - [ ] GitHub Actions or AWS CodePipeline

## Presentations

Give a simple demonstration of your automation process for reflecting the changes in a web application's code base; For example when pushed to GitHub, it will trigger an active pipeline and then deploy it to an AWS S3 Instance.

### Presentation day:

- Wednesday, July 6
- 5-10 minutes demonstration
- At least one visual aid, i.e. flow diagram of your pipeline

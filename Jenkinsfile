pipeline {
  agent none
  stages {
    stage('run') {
      agent {
        label 'executor-ubuntu20.04'
      }
      steps {
        sh 'systemctl --user restart uvicorn'
      }
    }

    stage('test') {
     agent {
        node {
          label 'centos7.9'
          customWorkspace '/root/jenkins'
        }
      }
      steps {
        sh 'curl http://${RUNNER}'
      }
    }

  }
  environment {
    RUNNER = '10.74.133.17:5000'
  }
}

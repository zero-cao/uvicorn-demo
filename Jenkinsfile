pipeline {
  agent none
  stages {
    stage('run') {
      steps {
        sh 'systemctl --user restart uvicorn'
      }
    }

    stage('test') {
      steps {
        sh 'curl http://${RUNNER}'
      }
    }

  }
  environment {
    RUNNER = '10.74.133.17:5000'
  }
}
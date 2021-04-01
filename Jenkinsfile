pipeline {
  agent none
  stages {
    stage('run') {
      agent {
        label 'executor-ubuntu20.04'
      }
      steps {
        sh 'cat /usr/lib/systemd/user/uvicorn.service'
        sh 'cat /home/dev/workspace/uvicorn-demo_main/uvicorn.conf'
        sh 'systemctl --user restart uvicorn'
        sh 'systemctl --user status uvicorn'
        sh 'ss -antp'
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

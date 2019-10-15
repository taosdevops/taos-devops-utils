pipeline {
  agent { docker { image 'python:3.7' } }
  stages {
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install --user -r devrequirements.txt'
          sh 'pytest'
        }
      }
    }
    stage('deploy'){
      when{
        branch 'master'
      }
      steps{
        withCredentials([
          file(credentialsId: 'devops-pypi-token', variable: 'API_KEY')
        ]) {
          withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'python -m pip install --user --upgrade setuptools wheel twine'
            sh 'python setup.py sdist bdist_wheel'
            sh 'python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose -u __token__ -p $API_KEY'
          }
        }
      }
    }
  }
}

pipeline {
    agent any
    stages {
        stage('拉取代码') {
            steps {
                echo '正在拉取代码...'
                checkout scm
            }
        }

        stage('执行脚本') {
            steps {
                echo '正在执行脚本...'
                sh 'bash hello.sh'
            }
        }

        stage('部署') {
            steps {
                echo '正在部署...'
                sh 'cp -r * /home/zhao/website/'
            }
        }
    }

    post {
        success {
            echo '构建成功！'
        }
        failure {
            echo '构建失败！'
        }
    }
}

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


        stage('安装依赖') {
            steps {
                echo '正在安装依赖...'
                sh 'pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --break-system-packages'

            }
        }

        stage('运行测试') {
            steps {
                echo '正在运行测试...'
                sh 'pytest'
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

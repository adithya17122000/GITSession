pipeline {
    agent any

    environment {
        // Define Python version
        PYTHON_VERSION = 'python3'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git url: 'https://github.com/adithya17122000/GITSession', branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Check if the environment is Unix-based or Windows
                    if (isUnix()) {
                        sh 'pytest test_main.py'  // Unix shell command
                    } else {
                        bat 'pytest test_main.py'  // Windows batch command
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add deployment commands here as needed
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed. Please check the errors.'
        }
    }
}

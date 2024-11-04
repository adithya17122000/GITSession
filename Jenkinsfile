pipeline {
    agent any

    environment {
        // Define Python version if using a specific one
        PYTHON_VERSION = 'python3'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git url: 'https://github.com/adithya17122000/GITSession', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary Python dependencies
                sh "${PYTHON_VERSION} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests, assuming there is a test script or test framework set up
                sh "${PYTHON_VERSION} -m unittest discover -s tests"
            }
        }

        stage('Deploy') {
            steps {
                // Dummy deploy step (replace with actual deployment commands)
                echo 'Deploying the application...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build succeeded!'
            // Send email notification on success
            mail to: 'adithyaan2000@gmail.com', 
                 subject: "Jenkins Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}", 
                 body: "The build completed successfully. Check the details at ${env.BUILD_URL}"
        }
        failure {
            echo 'Build failed. Please check the errors.'
            // Send email notification on failure
            mail to: 'adithyaan2000@gmail.com', 
                 subject: "Jenkins Build Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}", 
                 body: "The build has failed. Check the logs and details at ${env.BUILD_URL}"
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checking out from repo
                git 'https://github.com/Celio121/timelogdemo.git'
            }
        }

        stage('Setup') {
            steps {
                // Creating virtual environment and installing requirements
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                // Pytesting application
                sh '. venv/bin/activate && pytest'
            }
        }

        stage('Run Program') {
            steps {
                sh '. venv/bin/activate && python app.py'
                sh 'echo "Virtual environment is running and program is working"'
                // Add additional input data if needed
            }
        }

        stage('Post-Cleanup') {
            steps {
                // Perform any post-cleanup tasks, such as deleting temporary files, etc.
                sh 'rm -f timelogged.db'
                sh 'deactivate'
            }
        }
    }

    post {
        always {
            // Perform cleanup in case of job failure as well
            sh 'rm -f timelogged.db'
            sh 'deactivate'
        }
    }
}

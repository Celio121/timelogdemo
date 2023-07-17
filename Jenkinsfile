pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the repo'
                // Add additional build steps if needed
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                sh 'python3 test_app.py'
                // Add test report generation and post-processing steps if needed
                // input(id: "DeployGate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application'
                sh 'nohup python3 app.py > log.txt 2>&1 &'
                // Consider using a production-ready WSGI server like Gunicorn instead of the built-in Flask server
            }
        }
    }

    post {
        always {
            echo 'The pipeline completed'
            junit allowEmptyResults: true, testResults: '**/test_reports/*.xml'
            // Cleanup step to stop and clean up the Flask application
            sh 'kill $(ps aux | grep "python3 app.py" | grep -v grep | awk "{print $2}")'
            sh 'rm -f log.txt'
        }

        success {
            echo 'Flask Application Up and running!!'
        }

        failure {
            echo 'Build stage failed'
            error('Stopping early...')
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Set up virtual environment
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Run pytest for test_app.py and test_routes.py using the installed pytest
                sh '. venv/bin/activate && pytest test_app.py test_routes.py'
            }
        }

        stage('Run Application') {
            steps {
                // Start the Flask application as a background process
                sh '. venv/bin/activate && python3 app.py &'
            }
        }

        stage('Wait for Application to Start') {
            steps {
                // Wait for the application to start
                sh 'sleep 20'
            }
        }

        stage('Stop Application') {
            steps {
                // Send a request to gracefully shutdown the Flask application
                sh 'curl -X POST http://localhost:5000/shutdown'
            }
        }

        stage('Cleanup') {
            steps {
                // Deactivate the virtual environment and clean up
                sh 'rm -rf venv'
                sh 'rm timelogged.db'
            }
        }
    }
}
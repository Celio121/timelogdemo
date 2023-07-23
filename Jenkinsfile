pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Set up virtual environment
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt' // Make sure you have a requirements.txt file with the necessary dependencies.
            }
        }

        stage('Test') {
            steps {
                // Run pytest for test_app.py and test_routes.py
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
                sh 'deactivate'
                sh 'rm -rf venv'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Setup'){
            steps {
                // Install Python and required dependencies
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install -r requirements.txt'

                // Create and activate a virtual environment (optional)
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'pytest test_app.py' // Run pytest on the program
            }
        }

        stage('Run Program') {
            steps {
                script {
                    // Run the program
                    sh 'python app.py'

                    // Input data in the program (you can use 'echo' and 'python' commands)
                    sh 'echo "1" | python app.py' // Example input '1' for Sign-In
                    sh 'echo "testin" | python app.py' // input firstname in signin
                    sh 'echo "testinsur" | python app.py'// input lastname in signin
                    sh 'echo "2" | python app.py' // Example input '2' for Sign-Out
                    sh 'echo "testout" | python app.py' // input firstname in signout
                    sh 'echo "testoutsur" | python app.py' // input lastname in signout
                    sh 'echo "q" | python app.py' // Stop the program (if needed)

                }
            }
        }
    }

    post {
        always {
            // Perform any post-clean up tasks, such as deleting temporary files, etc.
            sh 'rm -f timelogged.db'
            sh 'deactivate' // exiting venv.
        }
    }
}

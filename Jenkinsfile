pipeline {
    agent any

    stages {
        stage('Setup'){
            steps {
                // Install Python and required dependencies
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'

                // Create and activate a virtual environment (optional)
                sh 'python3 -m venv venv'
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
                    sh 'python3 app.py'

                    // Input data in the program (you can use 'echo' and 'python3' commands)
                    sh 'echo "1" | python3 app.py' // Example input '1' for Sign-In
                    sh 'echo "testin" | python3 app.py' // input firstname in signin
                    sh 'echo "testinsur" | python3 app.py'// input lastname in signin
                    sh 'echo "2" | python3 app.py' // Example input '2' for Sign-Out
                    sh 'echo "testout" | python3 app.py' // input firstname in signout
                    sh 'echo "testoutsur" | python3 app.py' // input lastname in signout
                    sh 'echo "q" | python3 app.py' // Stop the program (if needed)

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

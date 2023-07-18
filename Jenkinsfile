pipeline {
    agent any

    environment {
        // Define environment variables for Python virtual environment
        VENV_HOME = "${WORKSPACE}/.venv"
        PATH = "${VENV_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Setup') {
            steps {
                // Create and activate a virtual environment
                sh 'python3 -m venv ${VENV_HOME}'
                sh '. ${VENV_HOME}/bin/activate && pip install --upgrade pip && pip install Flask'
                sh '. ${VENV_HOME}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Program') {
            steps {
                script {
                    // Run the program and provide input data (if needed)
                    sh '. ${VENV_HOME}/bin/activate && python app.py'
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

        stage('Unit Tests') {
            steps {
                sh '. ${VENV_HOME}/bin/activate && pytest test_app.py' // Run pytest on the program
            }
        }
    }

    post {
        always {
            // Perform any post-clean up tasks, such as deleting temporary files, etc.
            // Deactivate the virtual environment
            sh 'deactivate' // This may not be necessary
            sh "rm -rf ${VENV_HOME}" // Clean up the virtual environment
            sh 'rm -f timelogged.db'
        }
    }
}
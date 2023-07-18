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
                    sh ". ${VENV_HOME}/bin/activate && echo 1" // Example input '1' for Sign-In
                    sh ". ${VENV_HOME}/bin/activate && echo testin" // input firstname in signin
                    sh ". ${VENV_HOME}/bin/activate && echo testout"// input lastname in signin
                    sh ". ${VENV_HOME}/bin/activate && echo 2" // Example input '2' for Sign-Out
                    sh ". ${VENV_HOME}/bin/activate && echo testout" // input firstname in signout
                    sh ". ${VENV_HOME}/bin/activate && echo testoutsur" // input lastname in signout
                    sh ". ${VENV_HOME}/bin/activate && echo q" // Stop the program (if needed)



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
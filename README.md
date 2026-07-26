# Student Exam Score Predictor

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![ML Library](https://img.shields.io/badge/library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Docker Image](https://img.shields.io/badge/container-Docker-blue.svg)](https://www.docker.com/)

An end-to-end production-grade Machine Learning application that predicts a student's math exam score based on demographic characteristics, preparation levels, and related academic scores.

---

## Live Deployments

*   **Vercel Web App:** [Student Score Predictor App](https://vercel.com/shubhanshu3/student-score-predictor/deployments)
*   **Docker Image:** [Docker Hub Repository](https://hub.docker.com/repository/docker/dropper135/student-score-predictor)

---

## Key Features

*   **Modular ML Pipeline**: Standardized pipeline components for **Data Ingestion**, **Data Transformation** (imputation, scaling, one-hot encoding), and **Model Training**.
*   **Production Flask Server**: Lightweight and clean web API framework to serve prediction requests in real-time.
*   **Comprehensive Logging**: Complete activity tracking for every stage of the pipeline to facilitate easy debugging.
*   **Custom Exception Handling**: Custom system exception handling that traces detailed file names and line numbers for errors.
*   **Docker Containerization**: Portable Dockerfile configurations allowing fast deployment across any cloud platform.

---

## Tech Stack & Libraries

*   **Language:** Python 3.12
*   **Web Framework:** Flask
*   **Data Processing:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn
*   **Serialization:** Dill, Pickle
*   **Containerization:** Docker

---

## Project Structure

```text
├── .dockerignore
├── .ebextensions/           # AWS Elastic Beanstalk configurations
├── Dockerfile              # Docker container setup
├── requirements.txt        # Production dependencies
├── setup.py                # Package metadata and requirements installer
├── app.py                  # Flask Web application runner
├── application.py          # WSGI entry point
├── templates/              # HTML frontend layouts
│   ├── index.html          # Welcome portal
│   └── home.html           # Prediction input form and results
├── src/                    # Source code directory
│   ├── __init__.py
│   ├── logger.py           # Application log generator
│   ├── exception.py        # Custom exception handler
│   ├── utils.py            # Model serialization & utility helper functions
│   ├── components/         # Core pipeline steps
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   └── pipeline/           # Orchestration pipelines
│       ├── train_pipeline.py
│       └── predict_pipeline.py
└── artifacts/              # Serialized pipeline objects (Preprocessor & Models)
```

---

## Local Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Shubhanshu-G/Student_Score_Prediction
    cd MLProject
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application**
    ```bash
    python app.py
    ```
    Access the application locally at `http://127.0.0.1:5000/`.

---

## Docker Deployment

1.  **Build the Docker Image**
    ```bash
    docker build -t student-score-predictor .
    ```

2.  **Run the Container**
    ```bash
    docker run -p 5000:5000 student-score-predictor
    ```

3.  **Pull from Docker Hub**
    ```bash
    docker pull dropper135/student-score-predictor:latest
    ```

---

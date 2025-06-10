# Traffic Offloading Automation: 4G/5G ENDC to WiFi

This repository automates traffic offloading from 4G/5G ENDC to WiFi, using AWS services for scalable, resilient, and cost-efficient deployments.

## System Architecture

- **Cloud Infrastructure:**
  - **AWS EMR:** Distributed data processing via Apache Spark.
  - **S3-based Feature Store:** Scalable storage.
  - **MLflow:** Experiment tracking and model registry.
  - **Auto-scaling:** Handles variable workloads.

- **Data Pipeline:**
  - Real-time behavioral biometric and device fingerprint data collection.
  - Secure transmission and storage.
  - Distributed feature engineering.

- **Machine Learning:**
  - Ensemble model: Isolation Forest + Random Forest.
  - Real-time prediction serving.
  - Model performance monitoring.

---

## Prerequisites

- Python 3.7+
- AWS Account (with EMR, S3, IAM permissions)
- Docker (optional)
- Git

---

## Quick Start

1. **Clone the Repository**
    ```bash
    git clone https://github.com/payamdsp/traffic-offload-automation.git
    cd traffic-offload-automation
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Deploy Infrastructure**
    - Edit AWS credentials, then run EMR and S3 setup scripts in `infrastructure/`.

4. **Run Data Pipeline & Feature Engineering**
    - Use `data_pipeline/data_collection.py` and `feature_engineering/spark_job.py`.

5. **Train and Serve Models**
    - Use `ml/ensemble_model.py` for training.
    - Serve with `ml/model_serving.py`.

6. **Experiment Tracking**
    - MLflow setup via `infrastructure/mlflow_setup.py`.

---

## Directory Structure

- **infrastructure/**: AWS EMR, S3, MLflow, and scaling configs.
- **data_pipeline/**: Data collection and secure transmission scripts.
- **feature_engineering/**: Spark jobs and feature versioning.
- **ml/**: Model training, serving, and monitoring.
- **.github/**: CI/CD workflows.

---

## Cost Optimization Notes

- Uses AWS EMR Spot Instances and auto-termination for cost control.
- S3 lifecycle policies for feature storage.
- Lightweight, serverless components where possible.
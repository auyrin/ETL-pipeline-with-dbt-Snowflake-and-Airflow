# ETL Pipeline with Staging Area and Data Marts

## 📌 Overview
This project implements a robust **ETL pipeline** using **DBT**, **Snowflake**, and **Apache Airflow** to transform and load data into a **staging area** and structured **data marts** for analytics and reporting. The deployment is streamlined using **Astronomer Cosmos**, acting as the glue between Docker containers and Airflow.

## 🏗️ Architecture
The ETL pipeline follows a **modern data stack** approach:

1. **Extract**: Data is ingested from multiple sources into the **staging area** in Snowflake.
2. **Transform**: DBT applies transformations, business logic, and data modeling.
3. **Load**: Data is loaded into Snowflake's **data marts** for analysis.
4. **Orchestration**: Apache Airflow automates and schedules the ETL workflow.
5. **Deployment**: Astronomer Cosmos integrates Docker with Airflow for seamless execution.

## 🚀 Tech Stack
- **DBT** - Data transformation and modeling
- **Snowflake** - Cloud data warehouse
- **Apache Airflow** - Workflow orchestration
- **Astronomer Cosmos** - Integration of Docker and Airflow
- **Python** - Scripting and automation
- **Docker** - Containerized deployment

## 📂 Project Structure
```bash
├── dbt-dag/              # astronomer cosmos was initialized here
   ├── DockerFile            # our container image
   ├── dags/                 # Airflow DAGs for scheduling jobs
   |  ├── dbt_dag.py            # our Dag file
   ├── dbt/
   |  ├── data_pipeline/        # dbt project folder
   |  │   ├── models/           # DBT transformation models
   |  │   ├── seeds/            # Seed data files
   |  │   ├── snapshots/        # Historical tracking of data changes
   |  │   ├── dbt_project.yml   # DBT configuration
```

## ⚡ Quick Start
### Prerequisites
- Docker & Docker Compose
- Python 3.8+
- DBT installed (`pip install dbt-snowflake`)
- Snowflake account
- Airflow setup (`pip install apache-airflow`)
- Astronomer Cosmos installed (`pip install astronomer-cosmos`)

### Setup and Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/auyrin/etl-pipeline.git
   cd etl-pipeline
   ```

2. **Set up environment variables** (in your dbt initialization)
   ```bash
   dbt init
   project_name
   snowflake account details
   ```

3. **Run DBT transformations**
   ```bash
   dbt run
   ```

4. **initialize astronomer cosmos in a seperate folder**
   ```bash
   astro dev init
   ```

5. **Deploy and trigger Airflow DAGs with Astronomer Cosmos**
   ```bash
   astro dev start
   ```

## 📊 Data Flow
1. **Raw data ingestion** into Snowflake staging tables.
2. **Transformations using DBT**, applying business logic.
3. **Final tables** stored in Snowflake **data marts**.
4. **data quality tests** with generic and single tests
5. **Scheduled runs with Airflow** to automate the workflow.
6. **Deployment managed via Astronomer Cosmos**, ensuring smooth Airflow-Docker integration.

## 📌 Future Enhancements
- Integrate **CI/CD for DBT models**.
- Add **monitoring and alerting** for pipeline failures.

## 🤝 Contributing
Feel free to **fork** the repo, create a **branch**, and submit a **pull request**. Open issues if you find any bugs or have feature requests!

---
🔗 **Author:** Francis Egbuluka
📧 **Contact:** chinwutemegbuluka@gmail.com  
🚀 **GitHub:** [github.com/Auyrin](https://github.com/Auyrin)


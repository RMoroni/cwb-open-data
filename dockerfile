FROM apache/airflow:latest
EXPOSE 8080
COPY dags/* /opt/airflow/dags/
RUN airflow db init
RUN airflow users create \
    --username ryuk \
    --firstname Ryuk \
    --lastname Shinigami \
    --role Admin \
    --email rodrigomoroni@hotmail.com --password kira
# RUN airflow webserver --port 8080 -D && airflow scheduler -D
# CMD airflow scheduler
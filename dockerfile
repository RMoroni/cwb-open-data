FROM apache/airflow:latest
EXPOSE 8080
ARG PROJECT_HOME=/home/cwb_open_data
ENV AIRFLOW_HOME=$PROJECT_HOME/airflow

USER root
RUN echo "airflow:airflow" | chpasswd
RUN echo "root:root" | chpasswd

RUN mkdir -p $PROJECT_HOME
COPY . $PROJECT_HOME
RUN chmod 775 -R $PROJECT_HOME

USER airflow
WORKDIR $PROJECT_HOME
RUN pip install -e .
RUN airflow db init
RUN airflow users create \
    --username ryuk \
    --firstname Ryuk \
    --lastname Shinigami \
    --role Admin \
    --email rodrigomoroni@hotmail.com --password kira
RUN airflow webserver --port 8080 -D
# CMD airflow scheduler -D
FROM apache/airflow:latest
ARG PROJECT_HOME=/home/cwb_open_data
USER root
EXPOSE 8080
RUN echo "airflow:airflow" | chpasswd
RUN echo "root:root" | chpasswd

ENV AIRFLOW_HOME=$PROJECT_HOME/airflow
RUN mkdir -p $PROJECT_HOME
COPY . $PROJECT_HOME
RUN chmod 775 -R $PROJECT_HOME

USER airflow
WORKDIR $AIRFLOW_HOME
RUN airflow db init
RUN airflow users create \
    --username ryuk \
    --firstname Ryuk \
    --lastname Shinigami \
    --role Admin \
    --email rodrigomoroni@hotmail.com --password kira
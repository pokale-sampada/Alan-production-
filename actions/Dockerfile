FROM rasa/rasa-sdk:3.4.0
WORKDIR /app
USER root
RUN pip install requests
RUN pip install actions
COPY ./actions.py /home/ubuntu/app/actions
COPY requirements.txt requirements.txt
USER root
EXPOSE 5055
USER 1001

FROM python:3

EXPOSE 8050

WORKDIR /usr/src/app
COPY requirements.txt .
COPY assets assets
COPY app.py .
COPY custom_feet_component/dist/custom_feet_component-0.0.1.tar.gz custom_feet_component-0.0.1.tar.gz
COPY custom_people_component/dist/custom_people_component-0.0.1.tar.gz custom_people_component-0.0.1.tar.gz
COPY custom_play_component/dist/custom_play_component-0.0.1.tar.gz custom_play_component-0.0.1.tar.gz


RUN pip install --no-cache-dir -r requirements.txt
RUN pip install custom_feet_component-0.0.1.tar.gz
RUN pip install custom_people_component-0.0.1.tar.gz
RUN pip install custom_play_component-0.0.1.tar.gz


CMD [ "python", "app.py" ]
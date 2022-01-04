FROM python:3

EXPOSE 8050

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY custom_feet_component/dist/custom_feet_component-0.0.1.tar.gz custom_feet_component-0.0.1.tar.gz
RUN pip install --no-cache-dir custom_feet_component-0.0.1.tar.gz

COPY . .
CMD [ "python", "custom_feet_component/usage.py" ]
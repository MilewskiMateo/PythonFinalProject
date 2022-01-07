FROM python:3

EXPOSE 8050

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install lib/custom_feet_component-0.0.1.tar.gz

CMD [ "python", "app.py" ]
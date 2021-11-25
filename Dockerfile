FROM python:3.6

COPY . .


COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 8501:8501 

RUN pip install -r requirements.txt


CMD [ "streamlit run app.py ]
FROM python:3.8
RUN mkdir -p /app
RUN mkdir -p /app/python
COPY python/. /app/python

WORKDIR /app

RUN pip install fastapi==0.77.1
RUN pip install joblib==1.1.0
RUN pip install pandas==1.3.5
RUN pip install pydantic==1.8.2
RUN pip install uvicorn==0.17.6
RUN pip install scikit_learn==1.0.1
RUN pip install xgboost==1.6.1

EXPOSE 8000
CMD ["uvicorn", "python.run_server:app", "--host=0.0.0.0"]
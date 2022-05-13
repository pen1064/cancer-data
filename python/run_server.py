from unittest import result
from fastapi import FastAPI,Query
from typing import Optional
import pandas as pd
from python.model import MLModel
from python.ModelClass import ResultClass
import uvicorn



class ColumnDrop:
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return X.drop(self.columns, axis=1)
        
app = FastAPI()
@app.get('/')
def root(): return {'response':'go to predict'}

@app.post('/predict', response_model=ResultClass)
async def predict(q:Optional[str] = Query(None, max_length=100000)):
    query_in = {}
    if q:
        query_in.update({'q': q})
        query_in_dict = eval(query_in['q'])
        df = pd.DataFrame(query_in_dict, index=[0])
        pred, pred_p = MLModel.predict(df)
        print(pred)
        return {'y_pred': pred, 'y_pred_prob': pred_p} 
    else:
        return{'y_pred':1234, 'y_pred_prob': 1234}

if __name__ == '__main__':
    
    uvicorn.run('run_server:app')


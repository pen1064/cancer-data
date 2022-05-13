from pydantic import BaseModel

class ResultClass(BaseModel):
    y_pred: str
    y_pred_prob: str

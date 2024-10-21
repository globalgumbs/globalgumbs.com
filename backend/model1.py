import pickle
import pandas as pd
from typing import Tuple

class Model1:
    """ Model 1: Multi-Layer Perceptron ---------- Predicted Winner: 0 - Home Team | 1 - Away Team"""

    def __init__(self):
        model_path = "backend/model1.pkl"
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
    

    def make_preds(self, X_test: pd.DataFrame):
        COLS = [
        "AST", "DREB", "OREB", "3PM", "3PA", "FGM", "FGA",
        "FTM", "FTA", "BLK", "STL", "TO", "PF", "WIN%"
        ]
        for col in X_test:
            if col not in COLS:
                del(X_test[col])
        y: list[Tuple[float, float]] = self.model.predict_proba(X_test.values)
#        print(y)
        return y
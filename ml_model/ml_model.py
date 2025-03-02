from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.cluster import KMeans

app = FastAPI()

# Define request model
class SpendingData(BaseModel):
    spending: float

# Dummy data
data = np.array([[100], [500], [1200], [300], [800], [1500]])
kmeans = KMeans(n_clusters=3, n_init=10)  # Add `n_init` to avoid warning
kmeans.fit(data)

@app.post("/predict")
async def predict(data: SpendingData):  # Use Pydantic model to parse JSON
    category = kmeans.predict(np.array([[data.spending]]))
    return {"category": int(category[0])}

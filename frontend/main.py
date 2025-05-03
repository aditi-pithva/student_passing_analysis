import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import numpy as np
import os
from tensorflow.keras.models import load_model

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "models/neural_network_model.keras")
model = load_model(model_path)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@strawberry.type
class Prediction:
    result: int

@strawberry.type
class Query:
    hello: str = "Welcome to the Student Passing Prediction App!"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def predict(
        self,
        first_term_gpa: float,
        second_term_gpa: float,
        first_language: int,
        funding: int,
        fast_track: int,
        coop: int,
        residency: int,
        gender: int,
        prev_education: int,
        age_group: int,
        math_score: float,
        english_grade: int,
    ) -> Prediction:
        input_data = np.array([[first_term_gpa, second_term_gpa, first_language, funding,
                                fast_track, coop, residency, gender, prev_education,
                                age_group, math_score, english_grade]])

        prediction = model.predict(input_data)[0][0]
        predicted_class = int(prediction > 0.5)
        return Prediction(result=predicted_class)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/", response_class=HTMLResponse)
async def redirect_to_dashboard():
    return RedirectResponse(url="http://127.0.0.1:8051")

@app.get("/form", response_class=HTMLResponse)
async def form():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())
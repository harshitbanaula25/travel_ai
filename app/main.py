from app.agents.recommendation.graph import build_recommendation_graph
from app.state.travel_state import TravelState

graph = build_recommendation_graph()



from fastapi import FastAPI
from app.state.api_models import (
    RecommendationRequest,
    RecommendationResponse
)
from app.agents.recommendation.service import run_recommendation

app = FastAPI(title="Travel AI")

@app.post("/recommend", response_model=RecommendationResponse)
def recommend_travel(request: RecommendationRequest):
    result = run_recommendation(request)


    return RecommendationResponse(
    destinations=result.recommended_destinations,
    transport=result.recommended_transport,
    explanation=result.explanation,
    confidence_score=result.confidence_score
)


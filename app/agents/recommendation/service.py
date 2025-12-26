from app.state.travel_state import TravelState
from app.agents.recommendation.graph import build_recommendation_graph

graph = build_recommendation_graph()

def run_recommendation(request):
    initial_state = TravelState(
        user_id=request.user_id,
        source_location=request.source_location,
        budget=request.budget,
        preferences=request.preferences
    )

    result_dict = graph.invoke(initial_state)

    # Convert dict back to Pydantic model
    final_state = TravelState(**result_dict)

    return final_state

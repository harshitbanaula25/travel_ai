from app.state.travel_state import TravelState
from app.services.time_service import get_season

def collect_context(state: TravelState):
    state.season = get_season()
    return state

def apply_time_rules(state: TravelState):
    # Budget constraints
    if state.budget < 3000:
        state.recommended_transport = "ROAD"
        state.recommended_destinations = ["Nearby City"]
        return state

    # Season-based logic
    if state.season == "MONSOON":
        state.recommended_transport = "TRAIN"
        state.recommended_destinations = ["Jaipur", "Delhi"]
    elif state.season == "SUMMER":
        state.recommended_transport = "FLIGHT"
        state.recommended_destinations = ["Goa", "Bangalore"]
    else:
        state.recommended_transport = "FLIGHT"
        state.recommended_destinations = ["Pune", "Hyderabad"]

    return state

def calculate_confidence(state: TravelState):
    score = 0.5

    if state.budget > 10000:
        score += 0.2

    if state.season in ["SUMMER", "WINTER"]:
        score += 0.2

    state.confidence_score = min(score, 0.95)
    return state


def generate_explanation(state: TravelState):
    state.explanation = (
        f"Based on the {state.season} season and your budget, "
        f"{state.recommended_transport} is the most suitable option. "
        f"Confidence score: {state.confidence_score}"
    )
    return state




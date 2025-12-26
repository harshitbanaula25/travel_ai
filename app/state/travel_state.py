from typing import Optional, List
from pydantic import BaseModel

class TravelState(BaseModel):
    # User context
    user_id: Optional[str] = None
    source_location: Optional[str] = None
    budget: Optional[int] = None
    preferences: Optional[List[str]] = []

    # Travel context
    journey_phase: str = "PRE_TRAVEL"
    travel_date: Optional[str] = None
    season: Optional[str] = None

    # Recommendation output
    recommended_destinations: Optional[List[str]] = []
    recommended_transport: Optional[str] = None
    explanation: Optional[str] = None
    confidence_score: Optional[float] = None

    # Booking preparation (future)
    selected_destination: Optional[str] = None
    selected_transport_option: Optional[str] = None

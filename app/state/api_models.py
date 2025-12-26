from pydantic import BaseModel
from typing import List, Optional

class RecommendationRequest(BaseModel):
    user_id: str
    source_location: str
    budget: int
    preferences: Optional[List[str]] = []

class RecommendationResponse(BaseModel):
    destinations: List[str]
    transport: str
    explanation: str
    confidence_score:float

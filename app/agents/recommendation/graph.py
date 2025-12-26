from langgraph.graph import StateGraph, END
from app.state.travel_state import TravelState
from app.agents.recommendation.nodes import (
    collect_context,
    apply_time_rules,
    calculate_confidence,
    generate_explanation
   
)

def build_recommendation_graph():
    graph = StateGraph(TravelState)

    # ADD ALL NODES
    graph.add_node("collect_context", collect_context)
    graph.add_node("apply_time_rules", apply_time_rules)
    graph.add_node("calculate_confidence", calculate_confidence)
    graph.add_node("generate_explanation", generate_explanation)

    # ENTRY POINT
    graph.set_entry_point("collect_context")

    # EDGES
    graph.add_edge("collect_context", "apply_time_rules")
    graph.add_edge("apply_time_rules", "calculate_confidence")
    graph.add_edge("calculate_confidence", "generate_explanation")
    graph.add_edge("generate_explanation", END)

    return graph.compile()

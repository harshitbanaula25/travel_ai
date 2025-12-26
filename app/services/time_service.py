from datetime import datetime

def get_season():
    month = datetime.now().month

    if month in [3, 4, 5]:
        return "SUMMER"
    if month in [6, 7, 8, 9]:
        return "MONSOON"
    if month in [10, 11]:
        return "AUTUMN"
    return "WINTER"

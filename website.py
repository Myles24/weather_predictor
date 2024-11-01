from drafter import *
from bakery import assert_equal
from dataclasses import dataclass
from bakery_weather import *

    

@dataclass
class State:
    """ The state """
    current_day: str
    accuracy: float
    latitude: float
    longitude: float
    date: str
    name: str
    

# ------------------------ PREDICTION MODELING -------------------------------------

def weather_predictor(state: State, hours: int) -> Forecast:
    """ Predict the wind speed after x hours.
        1. Note the current conditions at some location 
        2. Take some radius around a location (dependent on # of hours)
        3. Choose an arbitrary number of locations in that radius in different directions
        4. Note the elevation at each location
        5. Note the wind direction at each location
        6. Weight locations with the lowest |difference of elevation| in reference to the target location higher
        7. Weight those locations with the highest |difference of pressure| higher
        8. 
        9. Test to see if those sample locations have  
    
    
    
    
    
    return [Forecast("tonight", False, 43, 45, "","","")]


def weather_accuracy(state: State, predicted : list[Forecast]) -> float:
    
    
    #return 100 - abs((get_weather(state.latitude, state.longitude).forecast[1].temperature - predicted[0].temperature)) / predicted[0].temperature * 100



@route
def index(state: State) -> Page:
    """ The main page """
    state.accuracy = weather_accuracy(state, weather_predictor(state))
    return Page(state, [
        "The main page",
        "Your model accuracy: " + str(state.accuracy) + "%"
    ])


# @route
# def begin() -> Page:
#     """ Updates the state """
#     return Page(state, [
#     
#     ])


hide_debug_information()
start_server(State("", 0.0, 39.6782, -75.7616, "", ""))


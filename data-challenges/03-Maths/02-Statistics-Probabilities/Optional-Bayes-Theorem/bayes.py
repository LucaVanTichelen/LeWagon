# pylint: disable=missing-docstring

weather_data_example = ['Sunny', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Sunny',
'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']

play_data_example = ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']

def prior_probability(play, play_data):
    '''TO DO: return P(data)'''
    pass

def likelihood(weather, play, weather_data, play_data):
    '''TO DO: return P(weather|play)'''
    pass

def posterior_probability(play, weather, weather_data, play_data):
    '''TO DO: returns P(play|weather)'''
    pass

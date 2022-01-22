## Bayes Theorem - a manual proof

In this challenge, we have a dataset of 'Weather' conditions (Rain, Sunny, Overcast), and their corresponding ‘Play’ conditions (Yes or No), suggesting whether or not a sport should be played based on the weather conditions.

```python
weather_data= ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play_data   =['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
```
Where the index `i` in `weather` corresponds to the index `i` in `play`. For example, for the 2nd game, the weather was 'Overcast' and the game was played.

Our goal is to understand the probability of playing a match or not.

More precisely, we want to compute the probability **$P(play \mid weather)$** in order to anticipate if a new match will be allowed to take place on the next day given a new weather condition.

By doing so, we will also demonstrate the **Bayes Theorem** by calculating each of these 4 probabilities ourselves:

<img src='https://github.com/lewagon/data-images/blob/master/math/bayes-theorem.png?raw=true'>


Where :
- $P(play)$ is our **prior** belief on the probability of the class (Play = Yes or No) given all data we have seen so far
- $P(weather \mid play)$ is the **likelihood** of observing this type of weather, given whether or not the match was played
- $P(play \mid weather)$ is the **posterior** probability of actually playing or not, given the weather condition
- $P(weather)$ is a constant, from the point of view of our problem: it does not depends on the choice of playing or not

Let's start!

### 0. Frequency Table
To see things clearly, start by constructing **manually** the frequency table (use a sheet of paper!). It should look like this:

| Weather  | Play  | Pause |
| ---------| ----- | ----- |
| Overcast |       |       |
| Sunny    |       |       |
| Rain     |       |       |
| Total    |       |       |


### 1. Calculate the prior probability $P(play)$
The idea is to compute the probability with python logic, in case you have a much longer dataset!
Implement the function, `prior_probability(play, play_data)`. This should return the probability that the match happened.
for example :
```python
play = "Yes"
play_data = ["Yes", "No", "Yes"]
prior_probability(event, list_events)
==> 0.66666
```

### 2. Likelihood $P(weather \mid play)$

Well done, now we will implement a function to calculate the likelihood of observing a given weather, knowing whether or not the match was played. Basically, that means that we want to calculate the probability of an event (ex: weather = 'Sunny') being `True` given that the other event (ex: play=Yes) was `True`

Implement the function `likelihood(weather, play, weather_data, play_data)`. This function should return the probability that `event_condition` takes a given value, knowing `event_occur` value.

For example, given the following array, you should get this result :
```python
weather_data = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play_data   = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
likelihood("Sunny", "Yes", weather_data, play_data) = 3/9 = 0.33333
```

### 3. Posterior Probability $P(play \mid weather)$

Congratulations, it's almost finished.

❓ Using Bayes Theorem and the two function coded before, implement the function `posterior_probability(play, weather, weather_data, play_data)` which gives you P(play|weather)

❓ Compare the result you found with a direct counting of $P(play \mid weather)$ using the likelihood function with the arguments reversed:
`likelihood(play, weather, play_data, weather_data)`

### 4. Step back and understand

Thanks to what you've learned in this challenge, could you answer these questions :
- Matches will always be played if the weather is sunny. Is this statement correct?
- If you know for sure that it will be raining during the next game, Do you think the game will be cancelled?

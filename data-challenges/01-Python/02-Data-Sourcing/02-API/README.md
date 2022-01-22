## Intro

A common way of collecting data is through APIs. Those can be [public APIs](https://github.com/public-apis/public-apis) with authentication or not, free or paying, internal APIs at your company, etc.

When it comes to APIs, there are some keywords that you should understand:

- [SOAP](https://en.wikipedia.org/wiki/SOAP) (old)
- [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) (current)
- [GraphQL](https://en.wikipedia.org/wiki/GraphQL) (very new, less frequent)
- [XML](https://en.wikipedia.org/wiki/XML) (long-established)
- [JSON](https://en.wikipedia.org/wiki/JSON) (currently very widespread)

The first three keywords refer to an architecture or a protocol on top of HTTP(s) and it is really important to figure out which one you are using when you want to **consume** data from an API.

The last two keywords refer to a **data format** that would usually be sent back to you when performing an API call.

ℹ️ Most modern APIs are RESTful and send back JSON. In this challenge, we are going to use such an API.

## Reading the documentation

When presented with a new API to use, your first reflex should be to go straight to the documentation, and figure out the following:

1. Is this a REST API?
1. Does it serve JSON?
1. Does this API require authentication? (do I need to sign up to get an API key? Do I need to pay?)
1. What is the base URI?
1. Which endpoints can I call? What data does it return?

👯‍♂️ Buddy time! Go to [metaweather.com](https://www.metaweather.com/), find the documentation, read it, and try answering those questions. When you are comfortable with what this API is about, you can start working on the challenge

## Making a test call to the API

Before building something fancy, we need to first make sure that we can run an API call successfully. This is a sanity check to make sure we don't start coding too much before realizing that the API we intended to use is not a good fit.

So how can we make our first call? There are several options:

### Using the browser

The browser _is_ an HTTP client! If there is no complex request `Header` to set and the verb to use is `GET`, then it's just as easy as typing the URL in the address bar. Try it!

Open a new browser tab, and copy/paste the following URL:

```bash
https://www.metaweather.com/api/location/search/?query=london
```

What do you see? If you are on Chrome, you should install the [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) extension for a neater look. In the end, JSON is just text that needs to be **parsed**, that's what the extension will do.

### Optional - Using Postman

[Postman](https://www.getpostman.com/) is an app that many developers download on their laptop to use when building software consuming APIs. It provides a more advanced experience where you need to have more control over:

- HTTP verb (`GET`, `POST`, `PATCH`, `DELETE`, etc.)
- Request headers (`Content-Type`, `Authorization`, etc.)
- Request body (`application/x-www-form-urlencoded` or `raw`)

This application allows us to **save** some requests, create tabs with different requests and offers more advanced features. Go ahead and try it!

### Using Python

Finally, we want to use this API in _our code_. Python's standard library comes with an [`http.client`](https://docs.python.org/3/library/http.client.html) built-in module, but we are not going to use it. Instead, we are going to use the [`requests`](https://requests.readthedocs.io) library, an 'elegant and simple HTTP library for Python, built for human beings'.

Open the `test_api.py` file and paste the following code:

```python
import requests

url = "https://www.metaweather.com/api/location/search/?query=london"
response = requests.get(url).json()
city = response[0]
print(f"{city['title']}: {city['woeid']} ({city['latt_long']})")
```

Save the file and run the following command:

```bash
python test_api.py
```

Is it working? Did you successfully grab London's `woeid`? Some questions for you to answer with your buddy before moving forward:

- Line `4`, why are we chaining a `.json()` after `.get()`? Does it still work without that call? You can `print()` intermediate steps to convince yourself. (💡 [Doc](https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content))
- Line `5`, why do we use `[0]`? What's the type of `response`?
- Line `6`, what's the type of `city['woeid']`, `str` or `int`? Why?

To answer those questions, don't hesitate to `print()` or **even better**, [debug](https://pypi.org/project/ipdb/). This first week is a good time to sharpen your debugging skills before diving into more advanced topics. Don't remember how to do it? Remember yesterday's challenge in which you had to insert this line in your code:
```python
import ipdb; ipdb.set_trace()
```

And run the file with:

```bash
python test_api.py
```

It will stop execution at the line where you added the `ipdb.set_trace()` and open a command line. From there you can check the `url`, `response`, `city` or any other variable you defined in the code!


## Let the challenge begin!

### Weather CLI

Let's build a weather [CLI](https://en.wikipedia.org/wiki/Command-line_interface) using the API. Here's the flow for a user (pseudo-code!):

1. Launch the app with `python weather.py`
2. Get asked to type a city name
3. If city is unknown to the API, display an error message and go back to step 2.
4. Fetch the weather forecast for the next 5 days and display it (Date, Weather and max temperature in °C)
5. Go back to step 2 (loop to ask for a new city).
6. At any point, `Ctrl`-`C` can be used to quit the program

In action, it should look like this:

```bash
python weather.py
```

```text
City?
> london
Here's the weather in London
2020-09-30: Heavy Rain 16.4°C
2020-10-01: Light Rain 15.1°C
2020-10-02: Heavy Rain 13.4°C
2020-10-03: Heavy Rain 14.3°C
2020-10-04: Heavy Rain 14.6°C
City?
>
```

Open the `weather.py` file. You will be greeted by three empty functions:

- `search_city(query)`
- `weather_forecast(woeid)`
- `main()`

You need to implement them **in that order**. `make` will assist you for the first two functions, and for the last one you will need to run the Python program directly with `python weather.py`.

1. Start with the `search_city` function which should return a `dictionary` with all the information about the city. Not just `woeid`!
2. Continue to `weather_forecast` which takes the city `woeid` as an argument and returns the forecast for five days (make sure that the method returns a `list`).
3. Finish off by coding the `main` function. It will be called when you run the `weather.py` file from the terminal. Which functions should be called from within `main`? In what order?

💡 By the way, did you check the content of the `Makefile`? It runs `pylint` for every Python file in your project, and `pytest` for the whole project. You can only launch the tests for the weather CLI with:

```bash
pytest -v tests/test_weather.py
```

## Optional - you can come back to it once you're done with the Scraping challenge.

### List of cities

After `step 3`: if the user input is ambiguous (i.e. several cities come back from the search), display them and ask the user to pick one. (💡 Hint: there's a built-in [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) function that might be useful)

### History

If you read carefully the documentation of the API, you may have noticed there is a third endpoint that we did not use yet, the **Location Day**:

```bash
URL: /api/location/(woeid)/(date)/
Arguments
  woeid: Where On Earth ID.
  date: Date in the format yyyy/mm/dd. Most locations have data from early 2013.
```

Some examples:

- [/api/location/44418/2013/4/27/](https://www.metaweather.com/api/location/44418/2013/4/27/) - London on 27th April 2013
- [/api/location/2487956/2013/4/30/](https://www.metaweather.com/api/location/2487956/2013/4/30/) - San Francisco on 30th April 2013

If you look closely at those examples, you can notice that it contains a list of datapoints for the **same `applicable_date`**, but the `created` shows either the same day _or_ days before. Which means you get a history of prediction + the _actual_ weather on the given day. This kind of data is exactly what we will want when working with Machine Learning, week 3 of the program.

In the meantime, let's do some **data engineering**, by gathering data from this API and storing it into a CSV for now. In real life, we would like to write directly to a **data warehouse** like [Google BigQuery](https://cloud.google.com/bigquery/), but for this first week, let's [KISS](https://en.wikipedia.org/wiki/KISS_principle) and store the data to a file. That's actually not such a bad idea, as we could write a Python script later to read that CSV and feed the data warehouse.

In this second part of the challenge, the goal is to create a CLI tool to retrieve historical weather information and store it into CSV files:

```bash
python history.py paris 2019 2
ls -lh ./data
# -rw-r--r--  344K  2019_02_615702_paris.csv
```

Your job is to complete the `history.py` file so that when ran with three arguments (the `CITY`, the `YEAR` and the `MONTH` (1 to 12)), it calls the historical API for every day of the month and dumps the forecasts into a _single_ csv file inside the `data` folder, named `YEAR_MONTH_WOEID_CITY.csv`

In the file given to you, you will need to implement three functions:

- `daily_forecast(woeid, year, month, day)`
- `monthly_forecast(woeid, year, month)`
- `write_csv(woeid, year, month, city, forecasts)`

The `main()` function is already implemented at the bottom of the file and reuses the `search_city(query)` from the first part of the challenge thanks to this line at the beginning of the file:

```python
from weather import search_city
```

The first two functions are tested, the last one (`write_csv`) is not, which means you will need to run the Python code directly (with 3 arguments, explained above) and look inside the `data` folder to manually check if it worked. If you run it with `paris 2019 2`, it should generate the following file:

```csv
# 2019_02_615702_paris.csv
id,weather_state_name,weather_state_abbr,wind_direction_compass,created,applicable_date,min_temp,max_temp,the_temp,wind_speed,wind_direction,air_pressure,humidity,visibility,predictability
5585764381360128,Light Rain,lr,SSE,2019-02-01T20:52:04.720014Z,2019-02-01,3.16,6.56,6.4399999999999995,2.9178008375467273,147.71871718547607,987.51,94,4.730498886502824,75
5957939957334016,Showers,s,SSE,2019-02-01T17:50:05.124112Z,2019-02-01,2.75,7.8566666666666665,8.355,3.7857594591962935,167.56996734323022,987.38,93,4.730498886502824,73
5183146429513728,Light Rain,lr,SSE,2019-02-01T14:48:06.412621Z,2019-02-01,2.75,7.8566666666666665,8.355,3.7857594591962935,167.56996734323022,987.38,93,4.730498886502824,75
# [...]
```

💡 **Hint**: Here are some methods you might find useful:

- [`urllib.parse.urljoin`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin)
- [`datetime.date`](https://docs.python.org/3/library/datetime.html#available-types)
- [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta)
- [`csv.DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter)

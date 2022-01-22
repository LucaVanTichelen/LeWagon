Web scraping is the last solution one needs to use to automate data retrieval (i.e. when there is _no API_ available). This technique is actually the one used by Google to build its index for the famous search engine. The Google bot performing this action is called a [crawler](https://www.google.com/search/howsearchworks/crawling-indexing/).

In the Python world, scraping means importing. [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a library used to pull data out of HTML.

## Example

We are going to scrape the Recipe directory [recipes.lewagon.com](https://recipes.lewagon.com/)

Open the `test_scraping.py` file in a text editor and paste the following code:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("pages/carrot.html"), "html.parser")

for recipe in soup.find_all('p', class_= 'recipe-name'):
    print(recipe.text)
```

In your terminal, run:

```bash
python test_scraping.py
```

💣 OK, you got an error. Can you read it? What are you missing?

What we want to do here is called **offline scraping**. While developing the scraper, we don't want to send HTTP requests to the server every time we run the code, taking the risk of spamming the site and being _banned_ from it.

Let's download the search results for the keyword `carrot`:

```bash
curl -g "https://recipes.lewagon.com/?search[query]=carrot" > pages/carrot.html
```

Now, run the Python script once again:

```bash
python test_scraping.py
```

✨ Congrats! You've just scraped your first page.

## Challenge

The goal of this challenge is to write a Python script that will parse the first 30 recipes for a given keyword and store them into the `recipes` folder. It should work like this:

```bash
python recipe.py chocolate

ls -lh recipes
# -rw-r--r--  12K  chocolate.csv

head -n 3 recipes/chocolate.csv

# name,difficulty,prep_time
# Ultimate chocolate cake,Easy,2 hours 10 mins
# Best ever chocolate brownies recipe,More effort,1 hour
```

In order to get to this final result, there are a few functions to implement in `recipe.py`

- `parse(html)`: this is the most important function. It needs to locate every recipe on the page, and dive into the `<div />` of a given recipe to locate its name, difficulty level and preparation time. After exploring the DOM, it will return a `list` of `dict` containing 3 keys (`name`, `difficulty`, `prep_time`).
- `write_csv(ingredient, recipes)`: this method takes two parameters. The first one is a `str`, the second one a `list` of `dict`. It will create a CSV file `{ingredient}.csv` and store the recipes from the list in the `recipes` directory.
- `scrape_from_internet(ingredient, start)`: this method will work on the website and search for the given `ingredient`. Ignore the `start` parameter to begin with. It should return the HTML from the page (to be fed to the `parse` method).
- `main()` Update the method so that `scrape_from_internet` is called instead of `scrape_from_file`. Run a few tests like `python recipe.py chocolate` or `python recipe.py strawberry`. After each run, check the `recipes` folder and open the created CSV file. Does it look OK to you?
- `main()` with **pagination**: you now need to update the `main` and the `scrape_from_internet` functions so that the program does not stop at the first page of search results but downloads the first 5 pages of recipes if available!

<details>
<summary> 💡 Hint </summary>
  Check-out [`requests.history`](https://2.python-requests.org/en/master/user/quickstart/#redirection-and-history).  How might you use this to stop your scrape early if there aren't 5 pages?
</details>

🙌 Have fun scraping!

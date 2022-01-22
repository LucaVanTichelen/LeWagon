In this challenge, we will learn how to load data from a CSV file with pure Python.

## 🔥 Warm-up

⚠️ For this warm-up, there is no `make` to run, so please read & follow the instructions closely!

Before we use a proper dataset, let's practise on something very simple.
Open the `data/phone_book.csv` file and add some lines to it. Keep the header!

As an example, it should look like this:

```csv
first_name,last_name,phone_number
John,Lennon,123
George,Harrisson,456
Ringo,Starr,789
```

The goal now is to load that data into a Python script, to use it. We are going to use the [`csv`](https://docs.python.org/3/library/csv.html) built-in module.

Open the `phone_book.py` file and copy/paste the following code:

```python
import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(row)
        line_count += 1
```

In your terminal, run the file:

```bash
python phone_book.py
```

Does that seem correct to you? What is the type of the `row` variable line 7 in the `print(row)` statement? Compare your guess with your buddy, and check the actual result with `type()` as well.

Try updating the code of `phone_book.py` to ignore the header (first line) and only print last name + phone number. This is the output you should get:

```bash
Lennon: 123
Harrisson: 456
Saunier: 123
```

## Optional

Now try refactoring the code using the [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader) class. You should no longer need the `line_count` variable. Also, what is the type of `row` now? Is it still the same as before? As usual, discuss the code with your buddy and check your understanding with `type()`.

After each question is solved please `add`/`commit`/`push` your code.

Have fun!

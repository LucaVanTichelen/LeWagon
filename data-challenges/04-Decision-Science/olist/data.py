import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Do not hardcode your path as it only works on your machine ('Users/username/code...')
        # Use __file__ instead as an absolute path anchor independant of your usename
        # Make extensive use of `import ipdb; ipdb.set_trace()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        # $CHALLENGIFY_BEGIN
        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "data", "csv")

        file_names = [f for f in os.listdir(csv_path) if f.endswith(".csv")]

        key_names = [
            key_name.replace("olist_", "").replace("_dataset",
                                                   "").replace(".csv", "")
            for key_name in file_names
        ]

        # Create the dictionary
        data = {}
        for k, f in zip(key_names, file_names):
            data[k] = pd.read_csv(os.path.join(csv_path, f))
        return data
        # $CHALLENGIFY_END

    def get_matching_table(self):
        """
        This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        # $CHALLENGIFY_BEGIN
        data = self.get_data()

        # Select only the columns of interest
        orders = data["orders"][["customer_id", "order_id"]]
        reviews = data["order_reviews"][["order_id", "review_id"]]
        items = data["order_items"][["order_id", "product_id", "seller_id"]]

        # Merge DataFrame
        matching_table = orders\
        .merge(reviews, on="order_id", how="outer")\
        .merge(items, on="order_id", how="outer")

        # Remove duplicates from the matching_table
        matching_table = matching_table.drop_duplicates()

        return matching_table
        # $CHALLENGIFY_END

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")

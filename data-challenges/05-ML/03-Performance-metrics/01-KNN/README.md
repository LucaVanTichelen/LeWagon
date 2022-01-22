# K-Nearest-Neighbors

## Download the dataset

The dataset is available [here](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Houses_clean.csv). Let's download it and store it in the `data` folder in the `01-KNN` directory with the following commands:

```bash
cd ~/code/<user.github_nickname>/data-challenges/05-ML/03-Performance-metrics/01-KNN
curl https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Houses_clean.csv > data/houses_clean.csv
```

## The dataset

- The dataset is a selection of features of the Houses dataset.
- The features are already preprocessed
- The target is the sale price of the houses

## Exercise

The exercise decomposes the KNN algorithm and its mechanics. You will:

- Discover it's sensitivity to scale
- Voluntarily make it overfit
- Fine tune it's parameter K

Finally, you will compare it's performance to the one of a Logistic Regression, and chose the model most suited for the task.

To start the exercise, open `KNN.ipynb` in `jupyter notebook` and follow the instructions.

🚀 Your turn!

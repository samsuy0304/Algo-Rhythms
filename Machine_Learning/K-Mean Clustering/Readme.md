# Mixture Model and K-means Clustering

This Google Colab notebook contains an implementation of a mixture model to generate data and the K-means clustering algorithm to cluster the data into groups.

## Dependencies
* Python 3.x
* NumPy
* Matplotlib
* Scikit-learn

## Usage
To generate data from a mixture of Gaussian distributions, open the generate_data.ipynb notebook in Google Colab and run the cells.

This will generate a dataset of 1000 observations from a mixture of three 2D Gaussian distributions with different means, covariances, and mixing proportions, and save it as a CSV file (data.csv).

To apply K-means clustering to the generated data, open the kmeans_clustering.ipynb notebook in Google Colab and run the cells.

This will cluster the data into three groups using K-means clustering and save the resulting cluster assignments as a CSV file (labels.csv).

To visualize the generated data and K-means clustering, open the visualization.ipynb notebook in Google Colab and run the cells.

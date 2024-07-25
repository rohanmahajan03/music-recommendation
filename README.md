# Music Recommendation Project Using KMeans by Rohan Mahajan

## Introduction

This project uses KMeans clustering to recommend music tracks based on their audio features and genres. It involves data preprocessing, clustering, and visualization. The code is written in Python, using libraries such as Pandas, NumPy, Matplotlib, Seaborn, Plotly, and scikit-learn.

## Getting Started

To run this project, make sure you have the necessary Python libraries installed. You can install them using `pip`:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn plotly
```

## Data

The dataset used in this project is stored in a CSV file named `dataset 2.csv`. It contains information about various music tracks, including attributes like popularity, duration, danceability, and more.

## Data Preprocessing

1. Import the necessary libraries for data analysis.
2. Read the dataset using Pandas.
3. Check for missing values and remove them.
4. Drop duplicate tracks to ensure unique data points.
5. Convert the 'explicit' column from categorical to numerical values.

## Exploratory Data Analysis (EDA)

Visualize the correlation between different audio features to understand the relationships in the data. This helps in feature selection and understanding which attributes are correlated.

## Scaling Data

Standardize the data using the StandardScaler to prepare it for clustering.

## Clustering

Use KMeans clustering to group tracks into clusters based on their audio features. Determine the optimal number of clusters using both the Silhouette Method and the Elbow Method.

## Visualizing Clusters

Visualize the clustered data using PCA for dimensionality reduction. Plot the clusters on a 2D graph.

## Genre-Based Clustering

Cluster music genres based on their average audio feature values. Analyze the genres' characteristics and how they relate to each other.

## Conclusion

This project provides a music recommendation system that clusters tracks based on their audio features and genres. By exploring the clusters, you can discover similar tracks and genres that match your music preferences.

## P.S. I have also integrated this into a web app via streamlit and deployed using AWS EC2.
Here is a screenshot of how the app looks:
<img width="1447" alt="Screen Shot 2024-07-24 at 9 33 47 PM" src="https://github.com/user-attachments/assets/d120bddf-4586-4318-8f54-b4c35a15cfbe">


Thank you for viewing my project!

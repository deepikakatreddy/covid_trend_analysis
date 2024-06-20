import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def perform_clustering_analysis(data):
    clustering_data = data[['total_cases', 'total_deaths', 'total_vaccinations']].dropna()
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(clustering_data)

    kmeans = KMeans(n_clusters=3, random_state=0)
    clusters = kmeans.fit_predict(scaled_data)

    clustering_data['cluster'] = clusters

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='total_cases', y='total_deaths', hue='cluster', data=clustering_data, palette='Set1', s=100)
    plt.title('Clustering of COVID-19 Data')
    plt.xlabel('Total Cases')
    plt.ylabel('Total Deaths')
    plt.legend(title='Cluster')
    plt.grid(True)
    plt.show()

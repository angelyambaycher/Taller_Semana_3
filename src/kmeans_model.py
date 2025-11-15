from sklearn.cluster import KMeans

def apply_kmeans(X, n_clusters=4):
    km = KMeans(n_clusters=n_clusters, random_state=42)
    labels = km.fit_predict(X)
    return labels, km

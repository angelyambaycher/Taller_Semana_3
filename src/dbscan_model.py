from sklearn.cluster import DBSCAN

def apply_dbscan(X, eps=0.6, min_samples=5):
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(X)
    return labels, db

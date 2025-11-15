from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def apply_pca(X, n_components=2):
    return PCA(n_components=n_components).fit_transform(X)

def apply_tsne(X, n_components=2):
    return TSNE(n_components=n_components, random_state=42).fit_transform(X)

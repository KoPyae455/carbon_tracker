import math
import random

class SimpleScaler:
    def fit(self, X):
        n = len(X)
        dim = len(X[0])
        self.mean_ = [sum(row[i] for row in X) / n for i in range(dim)]
        self.scale_ = []
        for i in range(dim):
            var = sum((row[i] - self.mean_[i]) ** 2 for row in X) / n
            self.scale_.append(math.sqrt(var) or 1)
        return self

    def transform(self, X):
        return [[(row[i] - self.mean_[i]) / self.scale_[i] for i in range(len(self.mean_))] for row in X]

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

class SimpleKMeans:
    def __init__(self, n_clusters=3, max_iter=100, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state

    def fit(self, X):
        random.seed(self.random_state)
        self.cluster_centers_ = [list(x) for x in random.sample(X, self.n_clusters)]
        for _ in range(self.max_iter):
            labels = [self._closest(x) for x in X]
            new_centers = []
            for k in range(self.n_clusters):
                members = [X[i] for i, l in enumerate(labels) if l == k]
                if members:
                    new_centers.append([sum(vals)/len(vals) for vals in zip(*members)])
                else:
                    new_centers.append(list(random.choice(X)))
            if new_centers == self.cluster_centers_:
                break
            self.cluster_centers_ = new_centers
        return self

    def predict(self, X):
        return [self._closest(x) for x in X]

    def _closest(self, x):
        distances = [self._dist_sq(x, c) for c in self.cluster_centers_]
        return distances.index(min(distances))

    @staticmethod
    def _dist_sq(a, b):
        return sum((ai - bi) ** 2 for ai, bi in zip(a, b))

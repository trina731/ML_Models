import numpy as np

class NaiveBayes:

    def fit(self, X, y):
        # X = feature vector(# rows = # samples, # cols = # features)
        # shape returns dimensions of array
        n_samples, n_features = X.shape
        #yes/no classification
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        #init mean, var(iance), priors
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros((n_classes), dtype=np.float64)

        for i in self._classes:
            X_i = X[i==y]
            self._mean[i,:] = X_i.mean(axis=0)
            self._var[i,:] = X_i.var(axis=0)
            # probability that this classification will occur
            # X_i.shape[0] = # samples with this label (# rows)
            self._priors[i] = X_i.shape[0] / float(n_samples)

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return y_pred

    def _predict(self, x):
        posteriors = []

        for idx, i in enumerate(self._classes):
            # get the prior
            prior = np.log(self._priors[idx])
            class_conditional = np.sum(np.log(self._pdf(idx, x)))
            posterior = prior + class_conditional
            posteriors.append(posterior)

        return self._classes[np.argmax(posteriors)]
    
    #gaussian probability density formula
    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        
        #gaussian dist formula
        numerator = np.exp(-(x-mean) ** 2 / (2 * var))
        denominator = np.sqrt(2*np.pi * var)
        return numerator/denominator


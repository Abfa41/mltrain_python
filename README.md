# mltrain

**mltrain** is a comprehensive machine learning package that provides easy-to-use implementations of popular algorithms. This toolkit is designed to help developers and researchers quickly prototype and deploy machine learning models. The package includes various supervised and unsupervised learning algorithms, each built from scratch for maximum flexibility and understanding.

## Features

- **Linear Regression:** Implementation of linear regression using gradient descent.
- **Logistic Regression:** Includes logistic regression with binary classification only.
- **Decision Tree:** A flexible decision tree implementation for Classification only.
- **Random Forest:** An ensemble method using multiple decision trees for improved accuracy.
- **Support Vector Machine (SVM):** Includes both linear and kernel-based SVMs with support for soft margins.
- **k-Nearest Neighbors (k-NN):** A simple and intuitive classification algorithm.
- **Naive Bayes:** Supports for Gaussian Naive Bayes for continuous Data.
- **KMeans Clustering:** A clustering algorithm.
- **DBSCAN:** A density-based clustering algorithm for discovering clusters of arbitrary shape.
- **PCA:** Dimensionality Reduction Model to reduce dimensions of dataset.

## Installation

You can install the package using `pip`:

```bash
pip install mltrain
```

## Usage
## Supervised Learning Models
### Linear Regression
It is Built from scratch. It can be applied to Multiple Weights...
```python
from mltrain.supervised.LinearRegression import LinearRegression

# Initialize the model
model = LinearRegression(learning_rate=0.01, epochs=1000)

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```
### Logistic Regression
Implemented only Binary Classification.
```python
from mltrain.supervised.LogisticRegression import LogisticRegression

# Initialize the model
model = LogisticRegression(learning_rate=0.01, epochs=1000)

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```
### KNN Model
You can use for both Regression and Classification. Default is given below:-
```python
from mltrain.supervised.KNN import KNN

# Initialize the model
model = KNN(k=3,distance='euclidean',purpose='classification')

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```

### Naive Bayes Model
Implemented only Gaussian Naive Bayes.
```python
from mltrain.supervised.NaiveBayes import NaiveBayes

# Initialize the model
model = NaiveBayes()

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```

### Naive Bayes Model
Implemented only Gaussian Naive Bayes.
```python
from mltrain.supervised.NaiveBayes import NaiveBayes

# Initialize the model
model = NaiveBayes()

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```
### Decision Tree
Implemented only for Classification Purpose only. Default Params are shown below:- 
```python
from mltrain.supervised.DecisionTree import DecisionTree

# Initialize the model
model = DecisionTree(max_depth=10, min_samples_split=2, criteria='gini')

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```
### Random Forest
Implemented only for Classification Purpose only. Default Params are shown below:- 
```python
from mltrain.supervised.RandomForest import RandomForest

# Initialize the model
model = RandomForest(n_trees=100, max_depth=10, min_samples_split=2, criteria='gini')

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```
### KernelSVM Model
Implemented only for Classification Purpose only. Default Params are shown below:- 
```python
from mltrain.supervised.KernelSVM import KernelSVM

# Initialize the model
model = KernelSVM(C=1.0, kernel_type='rbf', epochs=1000, learning_rate=0.01, gamma=0.5, coef0=0, degree=3)

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

```
## Unsupervised Learning Models
### K-Means Clustering Model
```python
from mltrain.unsupervised.KMeans import KMeans

# Initialize the model
model = KMeans(k=3, epochs=100)

# Train the model which Returns Cluster Labels
cluster_labels = model.train(X_train, y_train)
print(cluster_labels)

```
### DBSCAN Clustering Model
```python
from mltrain.unsupervised.DBSCAN import DBSCAN

# Initialize the model
model = DBSCAN(epsilon=0.5, min_points=5)

# Train the model which Returns Cluster Labels
cluster_labels = model.train(X_train, y_train)
print(cluster_labels)

```

### PCA
```python
from mltrain.unsupervised.PCA import PCA

# Initiliaze the Model
pca = PCA(n_components=2)

# Fit the Data and plot Graph
X_pca = pca.train_transform(X,plot_graph=True)

# Printing PC values
print(X_pca)

```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT License](LICENSE)



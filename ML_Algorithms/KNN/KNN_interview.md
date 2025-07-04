# 🎯 K-Nearest Neighbors (KNN) Interview Prep

---

## 🧠 Flashcards – Quick Q\&A

### Q1: What is K-Nearest Neighbors (KNN)?

> KNN is a non-parametric, instance-based learning algorithm used for classification and regression. It classifies data based on the majority vote of its 'k' nearest neighbors.

### Q2: What are the key hyperparameters in KNN?

> * **k**: number of neighbors
> * **Distance metric** (e.g., Euclidean, Manhattan)
> * **Weighting scheme** (uniform or distance-based)

### Q3: What type of algorithm is KNN?

> It is a **lazy learner** — no model is trained until a query is made. All computation is deferred until prediction time.

### Q4: How does KNN make predictions?

> For a given test point, it finds the 'k' nearest points in the training set and assigns the majority label (classification) or average value (regression).

### Q5: What are the pros and cons of KNN?

> **Pros:** Simple, interpretable, effective for small datasets
> **Cons:** Slow on large datasets, sensitive to irrelevant features and feature scaling

---

## 📐 KNN Formulas & Concepts

### 1. Distance Metrics

#### Euclidean Distance (default):

$d(p, q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$

#### Manhattan Distance:

$d(p, q) = \sum_{i=1}^n |p_i - q_i|$

### 2. Voting (Classification)

* Majority vote among the `k` nearest neighbors

### 3. Averaging (Regression)

* Average target value of the `k` nearest neighbors

---

## 🧭 Mind Map – Concept Breakdown

```mermaid
graph TD
    A[K-Nearest Neighbors (KNN)]
    A --> B[Lazy Learner]
    A --> C[No Training Phase]
    A --> D[Distance Metrics]
    A --> E[Hyperparameters]
    A --> F[Classification or Regression]
    A --> G[Scalability Challenges]
    A --> H[Feature Scaling Required]

    D --> D1[Euclidean]
    D --> D2[Manhattan]
    E --> E1[k value]
    E --> E2[Distance Weighting]
    F --> F1[Majority Vote [Class]]
    F --> F2[Average Value [Reg]]
```

---

## 🎤 Mock Interview Q\&A Sheet

### 🧩 Q1: How does KNN work?

**You:** KNN stores all training data. When a query point is given, it calculates the distance to all training points, picks the top k closest, and uses majority vote (classification) or mean (regression).

### 🧩 Q2: What happens if you choose a very small or large value of k?

**You:**

* Small k (e.g., 1): model is sensitive to noise (overfitting)
* Large k: too smooth, may underfit

### 🧩 Q3: How does feature scaling affect KNN?

**You:** KNN is distance-based, so features with larger scales dominate. Always apply normalization (MinMaxScaler or StandardScaler).

### 🧩 Q4: Is KNN good for high-dimensional data?

**You:** No. Distance measures lose effectiveness in high dimensions (curse of dimensionality). Dimensionality reduction is recommended.

### 🧩 Q5: How do you choose the best value for k?

**You:** Use cross-validation to find the k with lowest error. Plot accuracy vs. k to find the elbow point.

### 🧩 Q6: What's the time complexity of KNN?

**You:** O(n) per query, where n = number of training points. Can be improved using KD-Trees or Ball Trees.

### 🧩 Q7: How would you implement KNN from scratch?

**You:** Store training points in memory. For each test point, calculate distances to all training points, sort them, and return the majority label from the top k.

---

## 🧪 Python Code – KNN (From Scratch)

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from collections import Counter

# ---------------------- KNN Implementation ------------------------
# Function to compute Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Define the K-Nearest Neighbors classifier class
class KNN:
    def __init__(self, k=3):
        self.k = k  # Number of nearest neighbors to consider

    def fit(self, X, y):
        # Store the training data (no training happens in KNN)
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        # Predict the class for each sample in X
        return [self._predict(x) for x in X]

    def _predict(self, x):
        # Compute distances from x to all training samples
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # Get the indices of the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]

        # Fetch the labels of the k nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Majority vote: get the most common label
        most_common = Counter(k_nearest_labels).most_common(1)

        # Return the predicted class label
        return most_common[0][0]


# ---------------------- Load and Prepare Data ------------------------
# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features (very important for KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------------------- Train and Evaluate Model ------------------------
model = KNN(k=5)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

```

---

## ⚙️ Python Code – KNN Using scikit-learn

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load sample data
iris = load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 🌍 Real-World Applications of KNN

* 🛍️ **Recommender Systems**: Suggesting products based on similar user profiles
* 🧬 **Medical Diagnosis**: Predicting disease types using patient data
* ✍️ **Handwriting Recognition**: Classifying digits using pixel similarity (like MNIST)
* 💳 **Finance**: Credit scoring and fraud detection using historical patterns

---

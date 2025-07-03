# 📘 Logistic Regression – Math Formulas & Intuition

---

## 🧠 1. Linear Combination (Logit)

\[
z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b = \mathbf{w}^T \mathbf{x} + b
\]

- \( \mathbf{x} \): feature vector  
- \( \mathbf{w} \): weight vector  
- \( b \): bias (intercept)  
- \( z \): linear score (logit)

---

## 📈 2. Sigmoid Function (Logistic Function)

\[
\sigma(z) = \frac{1}{1 + e^{-z}} = \hat{y}
\]

- Maps \( z \) to a value in (0, 1)  
- Represents the **predicted probability** of class 1

---

## ✅ 3. Prediction Rule

\[
\text{Predict } y =
\begin{cases}
1 & \text{if } \hat{y} \geq 0.5 \\
0 & \text{if } \hat{y} < 0.5
\end{cases}
\]

---

## ❌ 4. Loss Function: Binary Cross-Entropy

\[
\mathcal{L}(\hat{y}, y) = - \left[ y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}) \right]
\]

- Penalizes wrong predictions more when they're confident but wrong  
- Works best for binary classification tasks

### Average Loss Over All Samples:

\[
J(w, b) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)})
\]

---

## 🔁 5. Gradient Descent (Optimization)

### Partial Derivatives:

\[
\frac{\partial J}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)}
\]

\[
\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})
\]

### Update Rule:

\[
w_j := w_j - \alpha \cdot \frac{\partial J}{\partial w_j}
\]
\[
b := b - \alpha \cdot \frac{\partial J}{\partial b}
\]

- \( \alpha \): learning rate  
- \( m \): number of training examples

---

## 📦 6. Regularization (Optional)

### L2 Regularization (Ridge):

\[
J_{\text{reg}}(w, b) = J(w, b) + \frac{\lambda}{2m} \sum_{j=1}^{n} w_j^2
\]

- Helps prevent overfitting  
- \( \lambda \): regularization strength (tunable hyperparameter)

---

## 🧮 Summary Table

| Component | Formula | Description |
|----------|---------|-------------|
| Logit | \( z = w^T x + b \) | Linear combination |
| Sigmoid | \( \hat{y} = \frac{1}{1 + e^{-z}} \) | Converts logit to probability |
| Prediction | \( y = 1 \text{ if } \hat{y} \geq 0.5 \) | Binary threshold |
| Loss | \( -[y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})] \) | Binary cross-entropy |
| Gradients | \( \nabla_w = \frac{1}{m} X^T(\hat{y} - y) \) | Used to update weights |
| Regularized Loss | \( J + \frac{\lambda}{2m} \sum w^2 \) | Adds penalty for large weights |

---

> 🧠 **Tip for interviews**: Practice walking through each formula **intuitively**, not just mathematically. For example:
> “We use sigmoid to squash the logit into a probability between 0 and 1 — this allows us to interpret it as a classification confidence.”


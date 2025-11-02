import matplotlib.pyplot as plt
import numpy as np

# Machine Learning Models
models = ['Logistic Regression', 'SVM', 'Naive Bayes', 'Random Forest', 'Decision Tree', 'KNN', 'CyberShield (Hybrid)']

# Performance Metrics
accuracy = [0.86, 0.89, 0.82, 0.91, 0.84, 0.83, 0.95]
precision = [0.85, 0.88, 0.80, 0.90, 0.83, 0.81, 0.94]
recall = [0.84, 0.87, 0.79, 0.89, 0.82, 0.80, 0.93]
f1_score = [0.84, 0.87, 0.80, 0.89, 0.82, 0.81, 0.94]

# X-axis positions
x = np.arange(len(models))
width = 0.2  # Bar width

# Plot setup
plt.figure(figsize=(12, 7))
plt.bar(x - 1.5*width, accuracy, width, label='Accuracy', color='#4C72B0')
plt.bar(x - 0.5*width, precision, width, label='Precision', color='#55A868')
plt.bar(x + 0.5*width, recall, width, label='Recall', color='#C44E52')
plt.bar(x + 1.5*width, f1_score, width, label='F1-Score', color='#8172B2')

# Grid customization
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Labels and title
plt.xlabel('Machine Learning Models', fontsize=12)
plt.ylabel('Performance Metrics', fontsize=12)
plt.title('Comparison of ML Algorithms vs CyberShield (Hybrid Model)', fontsize=14, weight='bold')
plt.xticks(x, models, rotation=25)
plt.legend()
plt.tight_layout()

# Show chart
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Machine Learning Models
models = ['Logistic Regression', 'SVM', 'Naive Bayes', 'Random Forest', 'Decision Tree', 'KNN', 'CyberShield (Hybrid)']

# Performance Metrics
accuracy = [0.86, 0.89, 0.82, 0.91, 0.84, 0.83, 0.95]
precision = [0.85, 0.88, 0.80, 0.90, 0.83, 0.81, 0.94]
recall = [0.84, 0.87, 0.79, 0.89, 0.82, 0.80, 0.93]
f1_score = [0.84, 0.87, 0.80, 0.89, 0.82, 0.81, 0.94]

# X-axis positions
x = np.arange(len(models))
width = 0.2  # Bar width

# Plot setup
plt.figure(figsize=(12, 7))
plt.bar(x - 1.5*width, accuracy, width, label='Accuracy', color='#4C72B0')
plt.bar(x - 0.5*width, precision, width, label='Precision', color='#55A868')
plt.bar(x + 0.5*width, recall, width, label='Recall', color='#C44E52')
plt.bar(x + 1.5*width, f1_score, width, label='F1-Score', color='#8172B2')

# Grid customization
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Labels and title
plt.xlabel('Machine Learning Models', fontsize=12)
plt.ylabel('Performance Metrics', fontsize=12)
plt.title('Comparison of ML Algorithms vs CyberShield (Hybrid Model)', fontsize=14, weight='bold')
plt.xticks(x, models, rotation=25)
plt.legend()
plt.tight_layout()

# Show chart
plt.show()

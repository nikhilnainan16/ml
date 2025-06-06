# -*- coding: utf-8 -*-
"""lab9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UCFENnxTtAPWOSV9izXY38ddN_HKHNDO
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def main():
    X, y = datasets.fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc * 100:.2f}%")

    plt.figure(figsize=(10, 5))
    for i in range(5):
        plt.subplot(1, 5, i + 1)
        plt.imshow(X_test[i].reshape(64, 64), cmap='gray')
        plt.title(f"Pred: {y_pred[i]}")
        plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()


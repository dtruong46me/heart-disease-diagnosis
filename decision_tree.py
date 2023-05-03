import os
from time import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

t1 = time()
filename = 'heart_disease.csv'
# filepath = os.path.join(os.path.dirname(__file__),'..',filename)

df = pd.read_csv(filename)

X = df.drop(['target'],axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

dc_classifier = DecisionTreeClassifier(criterion='entropy',max_depth=None, min_samples_split=2, min_samples_leaf=1)

dc_classifier.fit(X_train, y_train)

y_pred = dc_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cfus_matrix = confusion_matrix(y_test, y_pred)
t2 = time()

print('Accuracy Score = {:.2f}'.format(accuracy))
print('Confusion Matrix = {}'.format(cfus_matrix))
print('Time = {:.2f}'.format(t2-t1))

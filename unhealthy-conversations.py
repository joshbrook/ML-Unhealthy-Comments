# general imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import save_fig

# sklearn
from sklearn.metrics import accuracy_score
from sklearn.ensemble import ( GradientBoostingClassifier, 
                               VotingClassifier, 
                               RandomForestClassifier )
from sklearn.neighbors import KNeighborsClassifier


data = pd.read_csv("corpus/train.csv")
testdata = pd.read_csv("corpus/test.csv")

attributes = ['antagonize' , 'condescending', 'dismissive',
              'generalisation', 'generalisation_unfair', 
              'hostile', 'sarcastic']

confidences = [ 'antagonize:confidence' , 'condescending:confidence', 'dismissive:confidence', 
              'generalisation:confidence', 'generalisation_unfair:confidence', 
              'hostile:confidence', 'sarcastic:confidence' ]


X = data[["antagonize", "hostile"]]
y = data["healthy"]

Xtest = testdata[["antagonize", "hostile"]]
ytest = testdata["healthy"]


gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
rfc = RandomForestClassifier(n_estimators=200, random_state=42)
knn = KNeighborsClassifier(n_neighbors=10)

vote = VotingClassifier(estimators=[("gbc", gbc), 
                                    ("rfc", rfc),
                                    ("knn", knn) ], 
                        voting='hard')

clf = vote

clf.fit(X, y)
ypred = clf.predict(Xtest)
acc = accuracy_score(ytest, ypred)

print("Accuracy Score:", acc,
      "\ntrue healthy values:\n", ytest.value_counts(), 
      "\n\nhealthy predictions:\n", pd.Series(ypred).value_counts())

comp = ytest.compare(pd.Series(ypred))

pd.Series(ypred).hist(bins=3)
save_fig("comp")




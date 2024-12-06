#Patrick Loeber code base
#install streamlit matplotlib  scikit-learn(framework)


#try to write 'streamlit hello" for fire up the demo

import streamlit as st

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier, KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

import numpy as np
import matplotlib.pyplot as plt


st.title("Wiki Datasets")

st.write("""
#Explore the dataset basics
*With a streamlit and scikit-learn
""")


dataset_name = st.sidebar.selectbox("Select Dataset", ["Iris", "Breast Cancer", "Wine Dataset"])
#st.write(dataset_name) #getting update here since script updating


#little cases of machine learning
classifier_list = st.sidebar.selectbox("Select Classifier", ["KNN", "SVM", "Random Forest"])
#dataset loading

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()

    x= data.data
    y = data.target
    return x,y

x,y = get_dataset(dataset_name)
st.write("shape of the dataset", x.shape)
st.write("Number of classes", len(np.unique(y)))

#machine learning params:
def add_parameter_ui(classifier_list):
    parameters = dict()
    if classifier_list == "KNN":
        K = st.sidebar.slider("K", 1,15)
        parameters["K"] = K
    elif classifier_list == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        parameters["C"] = C
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 2, 15)
        parameters["max_depth"] = max_depth
        parameters["n_estimators"] = n_estimators
    return parameters

parameters = add_parameter_ui(classifier_list)

def get_classifier(clasifier_list, parameters):
    clf = None
    if classifier_list == "KNN":
        clf = KNeighborsClassifier(n_neighbors=parameters["K"])
    elif classifier_list == "SVM":
        clf = SVC(C=parameters['C'])
    else:
        clf = RandomForestClassifier(n_estimators=parameters["n_estimators"],
                                                max_depth = parameters["max_depth"], random_state=1234)
    return clf

clf = get_classifier(classifier_list, parameters)

#Classification
#split data into two paths -import tests

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=1234)

clf.fit(X_train, y_train) #fitting
#call predict method
y_pred = clf.predict(X_test)

#accuracy metrics
acc = accuracy_score(y_test, y_pred)
st.write(f"Classifier = {classifier_list}")
st.write(f"Accuracy = {acc:.2f}")



# PLOT
pca = PCA(n_components=2)
X_projected = pca.fit_transform(x)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1,x2, c=y, alpha=0.8, cmap='viridis')
plt.xlabel("Principal component 1")
plt.ylabel("Principal component 2")
plt.colorbar()


# Display plot using Streamlit - analogue from st.show
st.pyplot(fig)
#Y_projected = pca.fit_transform(y)


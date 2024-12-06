# TODO list - DONE:
# - Add more parameters [sklearn]
# - Add other classifiers
# - Add feature scaling


import streamlit as st
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

st.title("Wiki Datasets")

st.write("""
# Explore the dataset basics
* With a Streamlit and scikit-learn
""")

# Dataset selection
dataset_name = st.sidebar.selectbox("Select Dataset", ["Iris", "Breast Cancer", "Wine Dataset"])
classifier_list = st.sidebar.selectbox("Select Classifier", ["KNN", "SVM", "Random Forest", "Logistic Regression", "Decision Tree"])

# Loading datasets
def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()

    x = data.data
    y = data.target
    return x, y

x, y = get_dataset(dataset_name)
st.write("Shape of the dataset:", x.shape)
st.write("Number of classes:", len(np.unique(y)))


# Function to add some much parameters for the classiffiers...
##Kernel, gamma,  min_samples_split (TODO LIST)

def add_parameter_ui(classifier_list):
    parameters = dict()
    if classifier_list == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        algorithm = st.sidebar.selectbox("Algorithm", ["auto", "ball_tree", "kd_tree", "brute"])
        parameters["K"] = K
        parameters["algorithm"] = algorithm
    elif classifier_list == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        kernel = st.sidebar.selectbox("Kernel", ["linear", "poly", "rbf", "sigmoid"])
        gamma = st.sidebar.selectbox("Gamma", ["scale", "auto"])
        parameters["C"] = C
        parameters["kernel"] = kernel
        parameters["gamma"] = gamma
    elif classifier_list == "Logistic Regression":
        C = st.sidebar.slider("C", 0.01, 10.0)
        parameters["C"] = C
    elif classifier_list == "Decision Tree":
        max_depth = st.sidebar.slider("Max Depth", 1, 15)
        parameters["max_depth"] = max_depth
    else:  # Random Forest
        max_depth = st.sidebar.slider("Max Depth", 2, 15)
        n_estimators = st.sidebar.slider("Number of Estimators", 2, 100)
        min_samples_split = st.sidebar.slider("Min Samples Split", 2, 20)
        parameters["max_depth"] = max_depth
        parameters["n_estimators"] = n_estimators
        parameters["min_samples_split"] = min_samples_split
    return parameters

parameters = add_parameter_ui(classifier_list)

# Function to get classifiers based on user input..
def get_classifier(classifier_list, parameters):
    clf = None
    if classifier_list == "KNN":
        clf = KNeighborsClassifier(n_neighbors=parameters["K"], algorithm=parameters["algorithm"])
    elif classifier_list == "SVM":
        clf = SVC(C=parameters['C'], kernel=parameters['kernel'], gamma=parameters['gamma'])
    elif classifier_list == "Logistic Regression":
        clf = LogisticRegression(C=parameters['C'], max_iter=1000)
    elif classifier_list == "Decision Tree":
        clf = DecisionTreeClassifier(max_depth=parameters["max_depth"], random_state=1234)
    else:  # Random Forest
        clf = RandomForestClassifier(n_estimators=parameters["n_estimators"],
                                     max_depth=parameters["max_depth"],
                                     min_samples_split=parameters["min_samples_split"],
                                     random_state=1234)
    return clf

# Feature Scaling (TODO list)
scaler_option = st.sidebar.selectbox("Feature Scaling", ["None", "Standard Scaler", "Min-Max Scaler"])
if scaler_option == "Standard Scaler":
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
elif scaler_option == "Min-Max Scaler":
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)

clf = get_classifier(classifier_list, parameters)

# Classification basics
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

clf.fit(X_train, y_train)  # Fitting
y_pred = clf.predict(X_test)  # Prediction

# Accuracy metrics
acc = accuracy_score(y_test, y_pred)
st.write(f"Classifier: {classifier_list}")
st.write(f"Accuracy: {acc:.2f}")

# PCA for project visualization
pca = PCA(n_components=2)
X_projected = pca.fit_transform(x)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()

# Display plot using Streamlit feature:
st.pyplot(fig)


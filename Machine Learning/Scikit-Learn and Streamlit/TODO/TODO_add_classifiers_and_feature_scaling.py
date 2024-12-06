"""for TODO:
- Add other classifiers
- Add feature scaling"""

##Changes are made:
#Additional classifiers: Added an Logistic Regression and Decision Tree Classifier(range become to be wider)
#Feature scaling: Added StandardScaler&MinMaxScaler from sklearn.preprocessing(SVM and KNN algorithms are available 
##for being scaled in their features by user).

#import
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#Classifier
elif classifier_list == "Logistic Regression":
        clf = LogisticRegression(C=parameters['C'], max_iter=1000)
    elif classifier_list == "Decision Tree":
        clf = DecisionTreeClassifier(max_depth=parameters["max_depth"], random_state=1234)

# Feature Scaling
scaler_option = st.sidebar.selectbox("Feature Scaling", ["None", "Standard Scaler", "Min-Max Scaler"])
if scaler_option == "Standard Scaler":
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
elif scaler_option == "Min-Max Scaler":
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)


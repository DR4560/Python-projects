"""for TODO:
- Add more parameters [sklearn]"""

##Changes are made:
#KNN: Added an option for selecting the algorithm used to compute the nearest neighbors.
#SVM: Added options for the kernel type and gamma.
#Random Forest: Added an option for min_samples_split.
#Updated the respective classifier instantiation to include newly added parameters.

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
        gamma = st.sidebar.selectbox("Gamma", ["scale", "auto"])  # Using default options for gamma
        parameters["C"] = C
        parameters["kernel"] = kernel
        parameters["gamma"] = gamma
    else:
        max_depth = st.sidebar.slider("Max Depth", 2, 15)
        n_estimators = st.sidebar.slider("Number of Estimators", 2, 100)
        min_samples_split = st.sidebar.slider("Min Samples Split", 2, 20)
        parameters["max_depth"] = max_depth
        parameters["n_estimators"] = n_estimators
        parameters["min_samples_split"] = min_samples_split
    return parameters

parameters = add_parameter_ui(classifier_list)

import pandas as pd
from os.path import join, dirname, realpath
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model


import matplotlib
import matplotlib.pyplot as plt
import lime
import lime.lime_tabular
plt.switch_backend('Agg')
print("Using:",matplotlib.get_backend())

from tensorflow import keras

# load data and arrange into Pandas dataframe
df = pd.read_csv('./data/dataset_shade_2.csv')
# Instantiate LabelEncoder
le = LabelEncoder()
# Encode single column status
df.shade = le.fit_transform(df.shade)
# Print df.head for checking the transformation
df.head()


#Split into features and target (Price)
X = df.drop('stitch_length', axis = 1)
y = df['stitch_length']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 20)
#Scale dataset
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled  = scaler.transform(X_test)



def predict(scale_input):

    saved_model = load_model('data/model_stitch_length.h5')
    #Predict on test data
    predictions = saved_model.predict(scale_input)
    #y_real      = y_test[:10]
    print("Predicted values are: ", predictions)

    #revert to df for lime
    df = pd.DataFrame(scale_input)
    a  =  df.iloc[0]
    print('------------ df reconvert----------')
    print(a)

    feature_names = ['count', 'density', 'width','shade', 'diameter', 'gauge', 'needles', 'feeders', 'rpm', 'shrinkage_length', 'shrinkage_width','stitch_length']
    
    explainer = lime.lime_tabular.LimeTabularExplainer(X_test_scaled, feature_names=feature_names, verbose=True, mode='regression')
    explain_data_point = explainer.explain_instance(a,saved_model.predict, num_features=11)
    fig = explain_data_point.as_pyplot_figure()
    #fig.savefig('./assets/images/lime_report.jpg', bbox_inches="tight")
    #explain_data_point.save_to_file('./assets/images/explainer.html')


    return predictions
    # print("Real values are: ", y_real)



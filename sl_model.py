import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from keras.models import Sequential
from keras.layers import Dense


print('Training - Train Model(Stitch Length Prediction)')
# load data and arrange into Pandas dataframe
df = pd.read_csv('./data/dataset_shade_2.csv')
# Instantiate LabelEncoder
le = LabelEncoder()
# Encode single column status
df.shade = le.fit_transform(df.shade)
# Print df.head for checking the transformation
df.head()

print(df.head())

print(df.describe())

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
# print('-----X_test_scaled------')
print(X_test_scaled[:1])
print(type(X_test_scaled))



def Training():
    model = Sequential()
    model.add(Dense(90, input_dim=11, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(80, activation='sigmoid'))
    model.add(Dense(60, activation='sigmoid'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))

    import tensorflow as tf
    tf.keras.optimizers.Adam(learning_rate=0.0001, beta_1=0.9, beta_2=0.999, amsgrad=False)
    model.compile(loss='mean_squared_error', optimizer='Adam', metrics=['mean_absolute_percentage_error'])

    

    from keras import callbacks
    earlystopping = callbacks.EarlyStopping(monitor ="val_loss", 
                                            mode ="min", patience = 5, 
                                            restore_best_weights = True)
    
    history = model.fit(X_train_scaled, y_train, batch_size = 128, 
                        epochs = 100, validation_split=0.2, 
                        callbacks =[earlystopping])


    model.save('data/modelStitchLength.h5',history)

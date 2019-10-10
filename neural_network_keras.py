from keras import Sequential
from keras.layers import Dense
from Normalization import normalize_dataframe
import seaborn as sns
import matplotlib.pyplot as plt
    


def create_neural_network():
    X_train, Y_train, dataset = normalize_dataframe()
    # # print("LOL1")
    # classifier = Sequential()
    # classifier.add(Dense(8, activation='relu', kernel_initializer='random_normal', input_dim=15))
    # classifier.add(Dense(8, activation='relu', kernel_initializer='random_normal'))
    # # print("LOL2")
    # classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    # classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])
    # classifier.fit(X_train,Y_train, batch_size=10, epochs=50)
    # # print("LOL3")
    # eval_model=classifier.evaluate(X_train, Y_train)
    # print(eval_model)
    plt.figure(figsize=(20,10))
    sns.heatmap(dataset.corr(), annot=True)
    plt.show()

create_neural_network()
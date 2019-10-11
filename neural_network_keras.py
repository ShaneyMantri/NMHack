from keras import Sequential
from keras.layers import Dense
from Normalization import normalize_dataframe
import seaborn as sns
from keras.models import load_model
    


def create_neural_network():
    X_train, Y_train, dataset = normalize_dataframe("Train Data")

    x = dataset.iloc[:,0:14]
    y = dataset.iloc[:,-1]
    
    # print("LOL1")
    classifier = Sequential()
    classifier.add(Dense(8, activation='relu', kernel_initializer='random_normal', input_dim=15))
    classifier.add(Dense(8, activation='relu', kernel_initializer='random_normal'))
    # print("LOL2")
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])
    classifier.fit(X_train,Y_train, batch_size=10, epochs=50)
    # print("LOL3")
    eval_model=classifier.evaluate(X_train, Y_train)


    classifier.save("model.h5")

    for i in range(10):
        print("#")

    model = load_model('model.h5')
    model.summary()
    X_CV, Y_CV, CVDataset = normalize_dataframe("Validate Data")
    score = model.evaluate(X_CV, Y_CV)
    print(score)

    # plt.figure(figsize=(20,10))
    # sns.heatmap(dataset.corr(), annot=True)
    # plt.show()
    # predictions = model.predict_classes(X_CV)
    # # summarize the first 5 cases
    # for i in range(20):
    #     print('%s => %d (expected %d)' % (X_CV[i].tolist(), predictions[i], Y_CV[i]))



create_neural_network()
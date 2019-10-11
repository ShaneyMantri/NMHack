from keras import Sequential
from keras.layers import Dense
from Normalization import normalize_dataframe
import seaborn as sns
from keras.models import load_model
import matplotlib.pyplot as plt
    
def show_heat_map(data):
    #set plot size
    plt.figure(figsize=(20,10))
    #create and show heatmap
    sns.heatmap(data.corr(), annot=True)
    plt.show()

def create_neural_network():
    X_train, Y_train, dataset = normalize_dataframe("Train Data")
    X_CV, Y_CV, CVDataset = normalize_dataframe("Validate Data")

    # print("LOL1")
    classifier = Sequential()
    classifier.add(Dense(11, activation='relu', kernel_initializer='random_normal', input_dim=15))
    classifier.add(Dense(11, activation='relu', kernel_initializer='random_normal'))
    classifier.add(Dense(11, activation='relu', kernel_initializer='random_normal'))


    # print("LOL2")
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])
    classifier.fit(X_train,Y_train, batch_size=10, epochs=50)
    # print("LOL3")
    eval_model=classifier.evaluate(X_train, Y_train)
    cv_model=classifier.evaluate(X_CV, Y_CV)
    print("Eval model",eval_model)
    print("CV model",cv_model)



    classifier.save("model.h5")

    for i in range(10):
        print("#")

    classifier = load_model('model.h5')
    classifier.summary()
    score = classifier.evaluate(X_CV, Y_CV)
    print("CV Score",score)
    
    show_heat_map(dataset)
    
    # predictions = classifier.predict_classes(X_CV)
    # # summarize the first 5 cases
    # for i in range(4500):
    #     print('%d (expected %d)' % (predictions[i], Y_CV.iloc[i]))


create_neural_network()
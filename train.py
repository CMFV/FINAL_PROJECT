import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import metrics
import pickle
import textdistance
import itertools
import cv2
from sklearn.metrics import confusion_matrix

def import_data(df):
    df_me_data0=pd.read_csv(df)
    return df_me_data0

def cleaning_final(df_me_data0):
    df_me_data=df_me_data0.drop(columns=['Unnamed: 0', 'Name'])
    return df_me_data

def labeling(df_me_data):
    labels= df_me_data['Group']
    encoder=preprocessing.LabelEncoder()
    df_me_data['Group']=encoder.fit_transform(labels)
    numeric_dict={'GOOD':1,'NEUTRALS':0,'BAD':-1}
    df_me_data['ME_CLASSIFIED']=df_me_data['ME_CLASSIFIED'].map(numeric_dict)
    return df_me_data

def defining_data_supervised(df_me_data):
    X=df_me_data[['Group', 'Calories', 'Water', 'Protein', 'Carbohydrates', 'Fat',
       'Sugar', 'Sucrose', 'Glucose', 'Fructose', 'Lactose', 'Maletose',
       'Starch', 'Fiber', 'Polyols', 'Ash', 'Alcohol', 'Organic_Acids',
       'Saturated_Fat', 'Fat_Mono.', 'Fat_Poly.', 'DHA', 'Cholesterol', 'Salt',
       'Calcium', 'Choline', 'Cupper', 'Iron', 'Iodine', 'Magnesium',
       'Manganese', 'Phosphorus', 'Potassium', 'Selenium', 'Sodium', 'Zinc',
       'Retinol', 'Alpha_Carotene', 'Beta_Carotene', 'Caffeine', 'Theobromine',
       'Galactose', 'Fluoride', 'Beta_Cryptoxanthin', 'Lycopene',
       'Lutein&Zeaxathin', 'Vitamin A', 'Vitamin_B1', 'Vitamin_B2',
       'Vitamin_B3', 'Vitamin_B5', 'Vitamin_B6', 'Vitamin_B9', 'Vitamin_B12',
       'Vitamin_C', 'Vitamin_D2', 'Vitamin_D3', 'Vitamin_D', 'Vitamin_E',
       'Vitamin_K1', 'Vitamin_K2']]
    y=df_me_data['ME_CLASSIFIED']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test


def training_save_model(X_train, X_test, y_train, y_test):
    randomforest = RandomForestClassifier(n_estimators = 1000, criterion = 'entropy', random_state = 42)
    randomforest.fit(X_train, y_train)
    y_pred=randomforest.predict(X_test)
    y_prueba=[np.argmax(y)-1 for y in y_pred]
    score=randomforest.score(X_test, y_test)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred, pos_label=1)
    error=metrics.auc(fpr, tpr)
    pickle_out = open('FOOD_PREDICTED.sav','wb')
    pickle.dump(randomforest, pickle_out)
    pickle_out.close()
    return error, score, fpr, tpr, y_prueba

def plot_confusion_matrix (cm, keys, normalize=False, title='CONFUSION MATRIX', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.show(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=25)
    plt.colorbar()
    tick_marks = np.arange(len(keys))
    plt.xticks(tick_marks, keys, fontsize=15)
    plt.yticks(tick_marks, keys, fontsize=15)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout(pad=0.6,w_pad=0.6,h_pad=1)
    plt.ylabel('True label', fontsize=15)
    plt.xlabel('Predicted label', fontsize=15)
    grafico_modelo=plt.show()
    #img = cv2.imread("/confusion_matrix.png")
    return grafico_modelo

def reading_model (directorio, df_me_data0):
    modelo=pickle.load(open ('FOOD_PREDICTED.sav','rb'))
    df_no_clas0=pd.read_csv(directorio)
    df_no_clas=df_no_clas0.drop(columns=['Unnamed: 0', 'Name'])
    labels= df_no_clas['Group']
    encoder=preprocessing.LabelEncoder()
    df_no_clas['Group']=encoder.fit_transform(labels)
    prediccion=modelo.predict(df_no_clas)
    df_no_clas0['ME_CLASSIFIED']=prediccion
    frames = [df_me_data0, df_no_clas0]
    result = pd.concat(frames)
    category_dict={1:'GOOD',0:'NEUTRALS',-1:'BAD', 'GOOD':'GOOD', 'BAD':'BAD', 'NEUTRALS':'NEUTRALS'}
    result['ME_CLASSIFIED']=result['ME_CLASSIFIED'].map(category_dict)
    result=result.reset_index(drop=True)
    result=result.drop(columns=['Unnamed: 0'])
    return result

def filtro(inputo, column):
    rdo=[]
    for i in column:
        if inputo in i:
            rdo.append(i)
    return rdo


def consulta(inputo, lista):
    metric = textdistance.cosine.distance
    scores = enumerate(map(lambda x :metric(inputo,x), lista)) 
    scores = sorted(scores, key=lambda x:x[1])
    mejor=list(map(lambda x: (lista[x[0]], x[1]), scores))[:5]
    return mejor



def plotter_selected (dish_selection, result, column):
    row=result[column==dish_selection]
    row.reset_index(inplace=True,drop=True)
    lst=[]
    keys=[]
    for i in range(len(row.columns)-3):
        if float(row[row.columns[i+2]])>1:
            lst.append((row[row.columns[i+2]][0]))
            keys.append(row.columns[i+2])

    f, ax = plt.subplots(figsize=(20,6))
    plt.bar(keys,lst, edgecolor= '#008B8B', color='#20B2AA', linewidth='4')
    plt.rcParams['font.sans-serif'] = "Courier New"
    plt.rcParams['font.family'] = "monospace"
    ax.tick_params(axis='x', rotation=50, length=6, width=4, labelsize=10)
    a = [row.Name[0].upper(), row.ME_CLASSIFIED[0]]
    plt.title(' >>>  '.join(map(str,a)), fontsize=30, color='#008080')
    plt.subplots_adjust(bottom=0.2)
    grafico_resultado=plt.show()

    return grafico_resultado




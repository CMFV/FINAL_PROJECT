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
import os
import train
import textdistance

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_name=dir_path+'/me_diet_data.csv'
    df=csv_name
    df_me_data0=train.import_data(df)
    df_me_data=train.cleaning_final(df_me_data0)
    df_me_data=train.labeling(df_me_data)
    X_train, X_test, y_train, y_test=train.defining_data_supervised(df_me_data)
    error, score=train.training_save_model(X_train, X_test, y_train, y_test)
    directorio=dir_path+'/me_diet_EMPTY.csv'
    result=train.reading_model (directorio, df_me_data0)
    column=result['Name']
    inputo='tuna'
    rdo=train.filtro(inputo, column)
    lista = rdo
    mejor=train.consulta(inputo, lista)
    resultado = mejor
    res = [alimento for alimento, score in resultado][0]
    print(res)
    grafico_resultado=train.plotter_selected (res, result, column)



if __name__=="__main__":
    main()    
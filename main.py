 #-*- coding: utf-8 -*-
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
import argparse
import itertools
from sklearn.metrics import confusion_matrix
import cv2

def parse():
    parser = argparse.ArgumentParser()  # analizador de argumentos

    parser.add_argument('-m', '--model', help='Muestra un resumen del modelo generado.')  # action guarda el argumento
    parser.add_argument('-f', '--food', help='Muestra una lista de los alimentos que más se parecen a la busqueda introducida y su proximidad', type=str)
    parser.add_argument('-d', '--dish', help='Muestra la clasificación del argumento y sus propiedades', type=str)

    return parser.parse_args()

def main():
    pars=parse()
    if pars.model:
        a=pars.model
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csv_name=dir_path+'/me_diet_data.csv'
        df=csv_name
        df_me_data0=train.import_data(df)
        df_me_data=train.cleaning_final(df_me_data0)
        df_me_data=train.labeling(df_me_data)
        X_train, X_test, y_train, y_test=train.defining_data_supervised(df_me_data)
        error, score, fpr, tpr, y_prueba=train.training_save_model(X_train, X_test, y_train, y_test)
        #cm = confusion_matrix(y_prueba,y_test)
        #keys = [-1,0,1]
        #plt.figure(figsize=(10,10), linewidth='4')
        #plt.rcParams['font.sans-serif'] = "Courier New"
        #plt.rcParams['font.family'] = "monospace"
        img=train.plot_confusion_matrix()

    elif pars.food:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csv_name=dir_path+'/me_diet_data.csv'
        df=csv_name
        df_me_data0=train.import_data(df)
        df_me_data=train.cleaning_final(df_me_data0)
        df_me_data=train.labeling(df_me_data)
        X_train, X_test, y_train, y_test=train.defining_data_supervised(df_me_data)
        error, score, fpr, tpr, y_prueba=train.training_save_model(X_train, X_test, y_train, y_test)
        directorio=dir_path+'/me_diet_EMPTY.csv'
        result=train.reading_model (directorio, df_me_data0)
        column=result['Name']
        inputo=pars.food
        rdo=train.filtro(inputo, column)
        lista = rdo
        mejor=train.consulta(inputo, lista)
        print(mejor)
    elif pars.dish:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        csv_name=dir_path+'/me_diet_data.csv'
        df=csv_name
        df_me_data0=train.import_data(df)
        df_me_data=train.cleaning_final(df_me_data0)
        df_me_data=train.labeling(df_me_data)
        X_train, X_test, y_train, y_test=train.defining_data_supervised(df_me_data)
        error, score, fpr, tpr, y_prueba=train.training_save_model(X_train, X_test, y_train, y_test)
        directorio=dir_path+'/me_diet_EMPTY.csv'
        result=train.reading_model (directorio, df_me_data0)
        column=result['Name']
        resultado = pars.dish
        grafico_resultado=train.plotter_selected (resultado, result, column)



if __name__=="__main__":
    main()    

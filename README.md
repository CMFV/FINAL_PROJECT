# FEEDER

FEEDER is a program to make it easier for people with autoimmune and degenerative diseases to use food as a complementary therapy to medications in order to improve their quality of life and curb the side effects of medications as well as the evolution of the disease.

For the development of the program we have taken into account the diet prepared by Dr. Terry Wahls called "Wahls Protocol" given its proven effectiveness in multiple patients. All the diet info: https://terrywahls.com/

The basis of this diet is represented in the following pyramid:

![Wahls Protocol Pyramid](https://github.com/CMFV/FINAL_PROJECT/blob/master/Wahls%20Pyramid.png)



## USED TECHNOLOGY:

- Pandas
- Numpy
- Scikit-Learn
- Matplotlib


## HOW IT HAS BEEN CREATED:

For the creation of FEEDER we have used two datasets with a total record of 9000 meals and their properties. After cleaning and normalizing them, it has been left with a total of 6229 food records.

Subsequently we have prepared a dataset with the foods that the "Wahls Protocol" diet classifies as:

**Good:** Those who by their properties bring benefits to people with these kind of diseases.

**Bad:** Foods that harm patients and therefore have a negative effect on them.

**Neutral:** Foods that are allowed in moderate quantities since they are neither beneficial nor harmful.

Once the dataset has been prepared, the 6229 foods have been classified according to the coincidences with the diet records. The criteria for classifying meals have been as follows:

1st --> If the meal contains a food considered bad, even containing good and neutral foods, it is considered bad.

2nd --> If the meal contains good food, even containing neutral food and if it does not contain bad food, it will be considered good.

3th --> If the meal has neutral foods, but does not contain good or bad foods, it is considered neutral food.

With this criteria we managed to classify more than 3000 meals. To classify the rest of the foods with their properties, we have trained the Random Forest Classifier supervised learning model with almost 90% of accuracy, so we have already classified all the meals in our dataset.


## HOW DOES THE PROGRAM WORKS:

We developed the program in Python 3 so the computer must have the program installed. To know how to download it, please follow the following link: https://realpython.com/installing-python/ 

To run the program we use the computer terminal, it has two simple commands:

***python main.py -f <food>***: In which we introduced the food to be consulted. The result will be a list of closest foods to the search entered.
    
***python main.py -d <dish>***: One of the results of the previous command is entered and the program will return a graph in which the food will appear, is good, neutral or bad classification for the disease and a graphic of the propierties it has.

# FEEDER

FEEDER is a program to make it easier for people with autoimmune and degenerative diseases to use food as a complementary therapy to medications in order to improve their quality of life and curb the side effects of medications as well as the evolution of the disease.

For the development of the program we have taken into account the diet prepared by Dr. Terry Wahls called "Wahls Protocol" given its proven effectiveness in multiple patients. All the diet info: https://terrywahls.com/

The basis of this diet is represented in the following pyramid:



## USED TECHNOLOGY:
- Pandas
- Numpy
- Scikit-Learn
- Matplotlib

## HOW IT HAS BEEN CREATED:

For the creation of FEEDER we have used two datasets with a total record of 9000 meals that after cleaning and normalizing them, it has been left with a total of 6229 food records with their properties.

Subsequently we have prepared a dataset with the foods that the "Wahls Protocol" diet classifies as:

Good: Those who by their properties bring benefits to people with these types of diseases.

Bad: Foods that harm patients and therefore have a negative effect on a day-to-day basis.

Neutral: Foods that are allowed in moderate quantities since they are neither beneficial nor harmful.

Once the dataset has been prepared, the 6229 foods have been classified according to the coincidences with the diet records. The criteria for classifying meals have been as follows:
-1st If the food contains a food considered bad, even containing good and neutral foods, it is considered bad.
- 2nd If the food contains good food, even containing neutral food and if it does not contain bad food, it will be considered good.
- 3th If the food has neutral foods, but does not contain good or bad foods, it is considered neutral food.

With this system we managed to classify more than 3000 meals so the rest was left to classify. To classify the rest of the foods with their properties, we have trained the Random Forest Classifier supervised learning model with a accuracy of almost 90% accuracy, so we have already classified all the meals in our dataset.


## HOW DOES THE PROGRAM WORK:

It is used with the computer terminal, it has two simple commands:
 -f <food>: in which the food to be consulted is introduced.
The result will be a list of foods that are closest to the search entered.
-d <plate>: one of the results is entered in the previous command and the program will return a graph in which the food will appear, if it is good, neutral or bad for the disease.

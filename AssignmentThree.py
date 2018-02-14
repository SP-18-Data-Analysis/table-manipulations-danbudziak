import re
import pandas as pd

file = open("wine-data.txt","r")

for line in file :
	values = re.split(', |\n| ',line)

dataFrame = pd.io.parsers.read_csv('wine-data.txt',header=None, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12])

dataFrame.columns = [ 'Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5','Feature6','Feature7','Feature8','Feature9','Feature10','Feature11','Feature12','Feature13']

print("***********MAXIMUM AND MINIMUM VALUES************")
print "The Alcohol Feature Max is",dataFrame['Feature1'].max(), "and the Minimum is",dataFrame['Feature1'].min()
print "The Malic Acid Max is",dataFrame['Feature2'].max(), "and the Minimum is",dataFrame['Feature2'].min()
print "The Ash Max is",dataFrame['Feature3'].max(), "and the Minimum is",dataFrame['Feature3'].min()
print "The Alcalinity of Ash Max is",dataFrame['Feature4'].max(), "and the Minimum is",dataFrame['Feature4'].min()
print "The Magnesium Max is",dataFrame['Feature5'].max(), "and the Minimum is",dataFrame['Feature5'].min()
print "The Total Phenols Max is",dataFrame['Feature6'].max(), "and the Minimum is",dataFrame['Feature6'].min()
print "The Flavanoids Max is",dataFrame['Feature7'].max(), "and the Minimum is",dataFrame['Feature7'].min()
print "The Nonflavanoid Phenols Max is",dataFrame['Feature8'].max(), "and the Minimum is",dataFrame['Feature8'].min()
print "The Proanthocyanins Max is",dataFrame['Feature9'].max(), "and the Minimum is",dataFrame['Feature9'].min()
print "The Color Intensity Max is",dataFrame['Feature10'].max(), "and the Minimum is",dataFrame['Feature10'].min()
print "The Hue Max is",dataFrame['Feature11'].max(), "and the Minimum is",dataFrame['Feature11'].min()
print "The OD280/OD315 of diluted wines Max is",dataFrame['Feature12'].max(), "and the Minimum is",dataFrame['Feature12'].min()
print "The Proline Max is",dataFrame['Feature13'].max(), "and the Minimum is",dataFrame['Feature13'].min()
print

print ("**********STANDARD DEVIATIONS OF EACH COLUMN**********")
print "The Standard Deviation of the Alcohol Feature is",dataFrame.loc[:,"Feature1"].std()
print "The Standard Deviation of the Malic Acid is ",dataFrame.loc[:,"Feature2"].std()
print "The Standard Deviation of the Ash is ",dataFrame.loc[:,"Feature3"].std()
print "The Standard Deviation of the Alcalinity is ",dataFrame.loc[:,"Feature4"].std()
print "The Standard Deviation of Megnesium is",dataFrame.loc[:,"Feature5"].std()
print "The Standard Deviation of Total Phenols is ",dataFrame.loc[:,"Feature6"].std()
print "The Standard Deviation of Total Flavanoid is ",dataFrame.loc[:,"Feature7"].std()
print "The Standard Deviation of Nonflavanoid Phenols is ",dataFrame.loc[:,"Feature8"].std()
print "The Standard Deviation of Proanthocyanis is ",dataFrame.loc[:,"Feature9"].std()
print "The Standard Deviation of Color Intensity is ",dataFrame.loc[:,"Feature10"].std()
print "The Standard Deviation of Hue is ",dataFrame.loc[:,"Feature11"].std()
print "The Standard Deviation of OD280/OD315 of diluted wines is ",dataFrame.loc[:,"Feature12"].std()
print "The Standard Deviation of Proline is ",dataFrame.loc[:,"Feature13"].std()

#Applying the Lambda Function
#Declaring a new data frame and initializing new column identifiers for the lambda function
multiplierOfScalar = .5
lambdaDataFrame = pd.io.parsers.read_csv('wine-data.txt',header=None, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12])
lambdaDataFrame.columns = [ 'F1', 'F2', 'F3', 'F4', 'F5','F6','F7','F8','F9','F10','F11','F12','F13']

lambdaDataFrame['F1'] = lambdaDataFrame['F1'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F2'] = lambdaDataFrame['F2'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F3'] = lambdaDataFrame['F3'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F4'] = lambdaDataFrame['F4'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F5'] = lambdaDataFrame['F5'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F6'] = lambdaDataFrame['F6'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F7'] = lambdaDataFrame['F7'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F8'] = lambdaDataFrame['F8'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F9'] = lambdaDataFrame['F9'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F10'] = lambdaDataFrame['F10'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F11'] = lambdaDataFrame['F11'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F12'] = lambdaDataFrame['F12'].apply(lambda x: x * multiplierOfScalar)
lambdaDataFrame['F13'] = lambdaDataFrame['F13'].apply(lambda x: x * multiplierOfScalar)

print"**********MULTIPLYING ALL THE ROWS BY A SCALAR WITH LAMBDA*********\n",lambdaDataFrame


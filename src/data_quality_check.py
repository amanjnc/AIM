import pandas as pd

def checkEmpty(dataset):


    #since the comments column is totally empty lets drop it
    data= dataset.drop('Comments',axis=1)

    for column in data.columns:
        missing_values = data[column].isnull().sum()
        print(f"Missing values  in selected columns:  {missing_values} ")
        
   
data = pd.read_csv('data/benin-malanville.csv')        
checkEmpty(data)

# def checkOutliers(dataset):
    

import pandas as pd

def checkIncorrectEntry(dataset):
    column_to_check = 'DHI'

    negative_values_count = (dataset[column_to_check] < 0).sum()

    if negative_values_count > 0:
        print("Number of negative values in the column:", negative_values_count)
    else:
        print("No negative values found in the column.")


data = pd.read_csv('data/benin-malanville.csv')        


checkIncorrectEntry(data)
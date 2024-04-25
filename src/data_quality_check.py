import pandas as pd
from scipy import stats

def checkEmpty(dataset):


    #since the comments column is totally empty lets drop it
    data= dataset.drop('Comments',axis=1)

    for column in data.columns:
        missing_values = data[column].isnull().sum()
        print(f"Missing values  in selected columns:  {missing_values} ")
        
   
data = pd.read_csv('data/benin-malanville.csv')        
checkEmpty(data)

    
    
def checkIncorrectEntry(dataset):
    column_to_check = 'DHI'

    negative_values_count = (dataset[column_to_check] < 0).sum()

    if negative_values_count > 0:
        print("count -ve values in the column:", negative_values_count)
    else:
        print("No -ve values in the column.")


data = pd.read_csv('data/benin-malanville.csv')        


checkIncorrectEntry(data)

# I used  z-scores for GHI column
def checkOutlier(dataset):
        
    
    data= dataset.drop('Comments',axis=1)
    data= data.iloc[:,1:]
    for column in data.columns:
        z_scores = stats.zscore(data[column])
        outliers = (z_scores > 3) | (z_scores < -3)
        print(f"Outliers in {column} column:", outliers.sum())

checkOutlier(data)
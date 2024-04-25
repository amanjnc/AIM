import pandas as pd
data = pd.read_csv('data/benin-malanville.csv')

def summaryStatistics(loaded_data):

        data_without_comment = data.iloc[:, :-2]
        numeric_columns = data_without_comment.select_dtypes(include=['float64', 'int64'])

        statistics_table = numeric_columns.describe()
        print(statistics_table)



summaryStatistics(data)
    
import pandas as pd
data = pd.read_csv('data/benin-malanville.csv')        


missing_values = data.isnull().sum()
missing_percentage = (missing_values / len(data)) * 100

print("Columns with missing values:")
print(missing_values[missing_values > 0])
print("\nMissing value percentages:")
print(missing_percentage[missing_percentage > 0])

data = data.drop('Comments', axis=1)

numeric_columns = data.select_dtypes(include=[float, int]).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
categorical_columns = data.select_dtypes(include=[object]).columns
data[categorical_columns] = data[categorical_columns].fillna('Unknown')

data.to_csv('data/cleaned_dataset.csv', index=False)
import pandas as pd


#QUESTION4
def unroll_distance_matrix(df)->pd.DataFrame():
    data = pd.read_csv(df)
    for val in range(len(data)):
        data['moto'] = 0.8*data['distance']
        data['car'] = 1.2*data['distance'] 
        data['rv'] = 1.5*data['distance'] 
        data['bus'] = 2.2*data['distance'] 
        data['truck'] = 3.6*data['distance'] 
    return data

mydata2 = r"C:\Users\julee\Desktop\test\dataset-3.csv"
result = unroll_distance_matrix(mydata2)
print(result)

import pandas as pd
#QUESTION1
def generate_car_matrix(df):
    data = pd.read_csv(df)
    car_matrix = data.describe().iloc[:, :8]
    car_matrix.set_index(pd.Index(data.id_1[1:9]), inplace=True)
    new_column_names = data['id_2'].tolist()
    car_matrix.columns = new_column_names[1:9]
    for i in range(len(car_matrix)):
        for j in range(len(car_matrix.columns)):
            if i == j:
                car_matrix.iat[i,j] = 0

    return car_matrix

#QUESTION 2
mydata = r"C:\Users\julee\Desktop\test\dataset-1.csv"  
result_matrix = generate_car_matrix(mydata)
print(result_matrix)

import numpy as np
def get_type_count(df):
    data = pd.read_csv(df)
    # for val in data.car:
    #     if val<=float(15):
    #         data['car_type'] = "low"
    #     elif val>float(15) and val<=float(25):
    #         data['car_type'] = "medium"
    #     elif val>float(25):
    #         data['car_type'] = "high"
    data['car_type'] = np.where(data['car'] <= 15, 'low',
                                np.where((data['car'] > 15) & (data['car'] <= 25), 'medium', 'high'))

    type_count = data['car_type'].value_counts()
    return type_count

mydata = r"C:\Users\julee\Desktop\test\dataset-1.csv"  
result = get_type_count(mydata)
print(result)

#QUESTION3
def get_bus_indexes(df)->list:
    data = pd.read_csv(df)
    mean_column_bus = data['bus'].mean()
    index_list = []
    for val in data.bus:
        if val > 2*mean_column_bus:
            index_list.append(val)
            
    index_list.sort()
    return index_list

mydata = r"C:\Users\julee\Desktop\test\dataset-1.csv"  
result = get_bus_indexes(mydata)
print(result)



#QUESTION4
def filter_routes(df)->list:
    data = pd.read_csv(df)
    avg_column_truck = data['bus'].mean()
    index_list = []
    for val in data.route:
        if val > 7*avg_column_truck:
            index_list.append(val)
            
    index_list.sort()
    return index_list

mydata = r"C:\Users\julee\Desktop\test\dataset-1.csv"  
result = filter_routes(mydata)
#print(result)

#QUESTION 5
def modify_matrix(input_matrix):
    modified_matrix = input_matrix.copy()
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j] > 20:
                modified_matrix[i][j] = input_matrix[i][j] * 0.75
            else:
                modified_matrix[i][j] = input_matrix[i][j] * 1.25

    return modified_matrix

mydata = r"C:\Users\julee\Desktop\test\dataset-1.csv" 
result_matrix = generate_car_matrix(mydata)
modify_matrix(result_matrix)
for row in result_matrix:
    print(row)



#6th ONE UNABLE TO SOLVE







    

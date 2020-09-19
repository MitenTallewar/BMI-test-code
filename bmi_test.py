import csv
from collections import Counter
file_path = 'C:\\Miten\\Python Preparation\\Interview Questions\\comp_test\\'
def read_contents():
    list_of_row = []
    with open(file_path+'Data_for_BMI_Calculator_Height_Weight.csv') as file:
        alllines = csv.reader(file)
        for row in alllines:
            list_of_row.append(row)
        return list_of_row

def finaldata_with_bmi(alldata):
    line_count = 0
    notValidData = []
    validData = []
    for row in alldata:
        if line_count == 0:
            line_count = 1
        elif row[0].isalpha() == True and row[1].isnumeric() == True and row[2].isnumeric() == True :
            bmi = calculate_bmi(row)
            validData.append(row+bmi)
            # validData.extend(bmi)
            line_count +=1
        else:
            notValidData.append(row)
            line_count +=1
    # print('this data is not valid-->',notValidData)
    # print('total_rows-->',line_count)
    return validData

def calculate_bmi(data):
    BMI_categoty= None
    Health_risk= None
    BMI_range = None
    x =int(data[1])
    y = int(data[2])
    bmi = y/((x/100)**2)
    if bmi <= 18.4 :
        BMI_categoty = "UnderWeight"
        BMI_range = bmi
        Health_risk = 'Malnutrition risk'
    elif bmi >=18.5 and bmi <= 24.9:
        BMI_categoty = "Normal weight"
        BMI_range = bmi
        Health_risk = 'Low risk'
    elif bmi >=25 and bmi <= 29.9:
        BMI_categoty = "Over weight"
        BMI_range = bmi
        Health_risk = 'Enhanced risk'
    elif bmi >=30 and bmi <= 34.9:
        BMI_categoty = "Moderately obese"
        BMI_range = bmi
        Health_risk = 'Medium risk'
    elif bmi >= 35 and bmi <= 39.9:
        BMI_categoty = "Severely obese"
        BMI_range = bmi
        Health_risk = 'High risk'
    elif bmi > 40:
        BMI_categoty = " Very Severely obese"
        BMI_range = bmi
        Health_risk = 'Very High risk'
    bmi_list =[BMI_categoty,BMI_range,Health_risk]
    return bmi_list

def write_csv(data):
    with open('output_for_BMI_Calculator_Height_Weight.csv', 'w',newline='') as file:
        csv_data = csv.writer(file, delimiter=',')
        csv_data.writerow(['Gender', 'Height', 'Weight', 'BMI_categoty', 'BMI_range', 'Health_risk'])
        for row in data:
            print(row)
            csv_data.writerows([row])
    return 'csv file added successfully..'

if __name__ == '__main__':

    contents = read_contents()
    # print(result)
    finaldata = finaldata_with_bmi(contents)
    # print('final data with BMI-->',finaldata)
    result = write_csv(finaldata)
    print(result)
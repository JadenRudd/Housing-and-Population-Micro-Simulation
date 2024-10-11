import random
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#%% Initial population function

def initial_population(Area_Of_Interest, Num_People):

    #Setting the area of interest for the model(Getting indexes to extract correct data)
    Index_mapping = {'Derby': 0, 'Derbyshire': 1, 'Leicester': 2, 'Leicestershire': 3, 'Lincolnshire': 4,
                      'North Northamptonshire': 5, 'Nottingham': 6, 'Nottinghamshire': 7, 'Rutland': 8,
                      'West Northamptonshire': 9, 'East Midlands': 10}
    
    if Area_Of_Interest in Index_mapping:
        Index_value = Index_mapping[Area_Of_Interest]
    Area_Of_Interest = Area_Of_Interest + '%'
    
    #File path for file with all data
    file_path = r"Group Project Statistics - East Midlands.xlsx"
    
    #Extracting all needed data from the file
    Gender_Distribution_Data = pd.read_excel(file_path, sheet_name='Gender Distribution')
    Age_Distribution_Data = pd.read_excel(file_path, sheet_name='Age Distribution')
    Household_Composition_Data = pd.read_excel(file_path, sheet_name='Household Composition')
    Housing_Occupancy_Rating_Data = pd.read_excel(file_path, sheet_name='Housing Occupancy rating')
    Bedrooms_Distribution_Data = pd.read_excel(file_path, sheet_name='Bedrooms Distribution')
    Number_Of_Households_Data = pd.read_excel(file_path, sheet_name='Number of Households')
    Household_Size_Distribution_Data = pd.read_excel(file_path, sheet_name='Housing Distribution')
    Marriage_Gap_Data = pd.read_excel(file_path, sheet_name='Marriage Gap')
    Age_Of_Birth_Data = pd.read_excel(file_path, sheet_name='Age of Birth')
    Marriage_Distribution = pd.read_excel(file_path, sheet_name='Percentage each age married')
    Living_At_Home_Age_Distribution = pd.read_excel(file_path, sheet_name='Percentage each age living home')
    
    #Age distribution of people in the chosen area for simulation
    Age_Distribution = Age_Distribution_Data[Area_Of_Interest].values
    Age_Distribution = Age_Distribution[1:]
    Ages=numpy.linspace(0,100, num=101)
    
    #Gender distribution of people in the chosen area for simulation
    Gender_Data = Gender_Distribution_Data.iloc[Index_value]
    Gender_Distribution = Gender_Data[['Male', 'Female']]
    Gender = ('Male', 'Female')
    
    #Marriage gap distribution
    Marriage_Gap_Distribution = Marriage_Gap_Data['Percentage%']
    Marriage_Gaps = Marriage_Gap_Data['Gap']
    
    #Age of Birth Distribution
    Age_of_Birth_Distribution = Age_Of_Birth_Data['Chance Mother gives birth at this age given birth'].values
    Ages_of_Birth = Age_Of_Birth_Data['Age of Mother']
    
    #House size distibution in chosen area
    Household_Size_Distribution = Household_Size_Distribution_Data.iloc[Index_value]
    Household_Size_Distribution = Household_Size_Distribution[['1 Person%', '2 Person%', '3 Person%', '4 Person%', '5 Person%', '6 Person%', '7 Person%', '8+ Person%']]
    Household_Size_Distribution = Household_Size_Distribution.astype(float)
    House_Sizes = (1,2,3,4,5,6,7,8)
    
    #Chances each person is married depending on gender
    Male_Marriage_Distribution = Marriage_Distribution['Males 2019%'].values
    Marriage_Ages = Marriage_Distribution['Ages'].values
    Female_Marriage_Distribution = Marriage_Distribution['Females 2019%'].values
    
    #Composition of single households from data in file
    Single_House_Composition = Household_Composition_Data[Area_Of_Interest].values
    Single_House_Composition = Single_House_Composition[2:4]
    Young_Ages = numpy.linspace(18,65, num=48)
    Old_Age_Distribution = Age_Distribution[66:]
    Old_Ages = numpy.linspace(66,100, num=35)
    Young_Age_Distribution =Age_Distribution[17:65]
    Total_Single_House_Percentage = Single_House_Composition[0]+Single_House_Composition[1]
    
    #Proportion of houses being students or 55+ Cohabiting
    Students_and_55plus_household_proportion = Household_Composition_Data[Area_Of_Interest].values[21]
    Student_Proportion = (Students_and_55plus_household_proportion - 3)/100
    Student_Distribution = Age_Distribution_Data[Area_Of_Interest].values
    Student_Distribution = Student_Distribution[19:24]
    Student_Ages = (18,19,20,21,22)
    Older_Age_Distribution = Age_Distribution[55:]
    Older_Ages = numpy.linspace(55,100, num=46)
    Older_Household_proportion = 0.03
    
    # Initialize dictionaries to store lists of people in each household size
    House = []
    household_lists = {size: [] for size in House_Sizes}
    People_Processed = 0
    
    #Keeping count of different household types
    Single_house_count = 0 
    Couples_with_kids_count = 0
    Couple_count = 0
    Couple_only_house_count = 0
    Single_with_kids_count = 0
    Student_House_Count = 0  
    Cohabiting_House_Count = 0
    People_Processed = 0
    
    #Keeps sorting people into houses till it meets the population
    while People_Processed < Num_People:
        House = []
        Random_House_Size = random.choices(House_Sizes, weights=Household_Size_Distribution, k=1)[0]
        random_number = random.random()
        #Creates a student house if its in this proportion
        if random_number < Student_Proportion:
            #Assuming students dont live in 1 bed houses
            while Random_House_Size == 1:
                Random_House_Size = random.choices(House_Sizes, weights=Household_Size_Distribution, k=1)[0]
            #Fills house with students according to distributions
            for i in range(Random_House_Size):
                Random_Age = random.choices(Student_Ages, weights=Student_Distribution, k=1)[0]
                Random_Gender = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                Marriage_Status = 'Student'
                person = (Random_Age, Random_Gender, Marriage_Status)
                #People_Processed+=1
                House.append(person)
            Student_House_Count +=1
        # Creates cohabiting house if its in this proportion
        elif random_number < Student_Proportion + Older_Household_proportion:
            #Can't have a single cohabiting house
            while Random_House_Size == 1:
                Random_House_Size = random.choices(House_Sizes, weights=Household_Size_Distribution, k=1)[0]
            #Fills house with people that are able to cohabit according to distributions
            for i in range(Random_House_Size):
                Random_Age = random.choices(Older_Ages, weights=Older_Age_Distribution, k=1)[0]
                Random_Gender = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                Marriage_Status = 'Cohabiting'
                person = (Random_Age, Random_Gender, Marriage_Status)
                #People_Processed+=1
                House.append(person)
            Cohabiting_House_Count +=1
        else:
            #If house for 1, makes sure they're 18+ and assigns a person to the house according to the distributions
            if Random_House_Size == 1:  
                Random_Number = random.random()
                if Random_Number >0.8:
                    continue
                person = None
                while person is None or person[0] <= 17:
                    Random_number  = random.uniform(0, Total_Single_House_Percentage)
                    if Random_number < Single_House_Composition[0]:
                        Random_Age = random.choices(Old_Ages, weights=Old_Age_Distribution, k=1)[0]
                    else:
                        Random_Age = random.choices(Young_Ages, weights=Young_Age_Distribution, k=1)[0]
                    Random_Gender = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                    Marriage_Status = 'Single'
                    person = (Random_Age, Random_Gender, Marriage_Status)
                House.append(person)
                #People_Processed +=1
                Single_house_count +=1
            #If house size is 2,finds a head of the house according to distributions    
            elif Random_House_Size >= 2:
                person = None
                while person is None or person[0] <= 17:
                    Random_Age = random.choices(Ages, weights=Age_Distribution, k=1)[0]
                    Random_Gender = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                    person = (Random_Age, Random_Gender)
                #Finds the marriage chance for the head of the house depending on age and gender
                if Random_Gender == 'Male':
                    marriage_Distribution = Male_Marriage_Distribution
                if Random_Gender == 'Female':
                    marriage_Distribution = Female_Marriage_Distribution
                marriage_age_index = int(Random_Age - 18)
                marriage_percentage = marriage_Distribution[marriage_age_index]
                # Determines marriage status then adds them to the house list
                random_number = random.uniform(0, 100)
                if random_number <= marriage_percentage:
                    Marriage_Status = 'Married'
                else:
                    Marriage_Status = 'Single'
                person = (Random_Age, Random_Gender, Marriage_Status)
                House.append(person)
                #People_Processed +=1 
                Age_of_head = person[0]
                Gender_of_head = person[1]
                #If the head is married,finds age of partner from marriage gap distribution( Makes sure 18+ and less than 100)
                if Marriage_Status == 'Married':
                    Random_Marriage_Gap = random.choices(Marriage_Gaps, weights=Marriage_Gap_Distribution, k=1)[0]
                    if Gender_of_head == 'Male':
                        Gender_of_partner = 'Female'
                        Age_of_partner = Age_of_head + Random_Marriage_Gap
                        while Age_of_partner > 100 or Age_of_partner < 18:
                            Random_Marriage_Gap = random.choices(Marriage_Gaps, weights=Marriage_Gap_Distribution, k=1)[0]
                            Age_of_partner = Age_of_head + Random_Marriage_Gap
                        partner = (Age_of_partner, Gender_of_partner, Marriage_Status)               
                        House.append(partner)
                        #People_Processed +=1
                        Couple_count +=1
                        Age_Of_Mother = partner[0] 
                        Age_Of_Father = person[0]
                    elif Gender_of_head == 'Female':
                        Gender_of_partner = 'Male'
                        Age_of_partner = Age_of_head - Random_Marriage_Gap
                        while Age_of_partner > 100 or Age_of_partner < 18:
                            Random_Marriage_Gap = random.choices(Marriage_Gaps, weights=Marriage_Gap_Distribution, k=1)[0]
                            Age_of_partner = Age_of_head + Random_Marriage_Gap
                        partner = (Age_of_partner, Gender_of_partner, Marriage_Status)
                        House.append(partner)
                        #People_Processed +=1
                        Couple_count+=1
                        Age_Of_Mother = person[0]
                        Age_Of_Father = partner[0]
                #If head isn't married, assign the parent a kid making sure age gap is more than 16 and the kid is 0+ years old
                else:
                    Age_Of_Mother = Age_of_head
                    Age_Of_Father = Age_of_head
                    Age_Of_First_Pregnancy = random.choices(Ages_of_Birth, weights=Age_of_Birth_Distribution, k=1)[0]
                    Age_Of_First_Child = Age_Of_Mother - Age_Of_First_Pregnancy
                    Age_Of_Father_At_Birth = Age_Of_Father - Age_Of_First_Child
                    Marriage_Status = 'Child'
                    #Regulatory conditions to make sure the age of the kid follows correct distribution
                    if Age_Of_First_Child > -1 and Age_Of_Father_At_Birth > 16 and Age_Of_First_Child <26:
                        Gender_Of_First_Child = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                        House.append((Age_Of_First_Child, Gender_Of_First_Child, Marriage_Status))
                        #People_Processed +=1
                        Single_with_kids_count +=1
                    elif 24 < Age_Of_First_Child < 36 and Age_Of_Father_At_Birth > 16:
                        Random_Number = random.random()
                        if Random_Number >0.6:
                            House.pop()
                            #People_Processed -=1
                            continue
                        else:
                            Gender_Of_First_Child = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                            House.append((Age_Of_First_Child, Gender_Of_First_Child, Marriage_Status))
                            #People_Processed +=1
                            Single_with_kids_count +=1
                    else:
                        House.pop()
                        #People_Processed-=1
                        continue
            #If house size 3+,assigns more children to the houses depending on the house size according to same process as above
            if Random_House_Size >= 3:
                repeats = Random_House_Size - 2
                for i in range (repeats):
                    Age_Of_First_Pregnancy = random.choices(Ages_of_Birth, weights=Age_of_Birth_Distribution, k=1)[0]
                    Age_Of_First_Child = Age_Of_Mother - Age_Of_First_Pregnancy
                    Age_Of_Father_At_Birth = Age_Of_Father - Age_Of_First_Child
                    if Age_Of_First_Child >35:
                        #People_Processed -=len(House)
                        House.clear()
                        continue
                    if 24< Age_Of_First_Child <36:
                        Random_Number = random.random()
                        if Random_Number >0.6:
                            #People_Processed -=len(House)
                            House.clear()
                            continue
                    Marriage_Status = 'Child'
                    while Age_Of_First_Child < 0 or Age_Of_Father_At_Birth < 16:
                        Age_Of_First_Pregnancy = random.choices(Ages_of_Birth, weights=Age_of_Birth_Distribution, k=1)[0]
                        Age_Of_First_Child = Age_Of_Mother - Age_Of_First_Pregnancy
                        Age_Of_Father_At_Birth = Age_Of_Father - Age_Of_First_Child
                    Gender_Of_First_Child = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                    House.append((Age_Of_First_Child, Gender_Of_First_Child, Marriage_Status))
                    #People_Processed +=1
                Couples_with_kids_count +=1
        #Adds the house to the list of the correct house size
        if len(House)==Random_House_Size:
            People_Processed += len(House)
            household_lists[Random_House_Size].append(House)
        else:
            continue
                
    # The lists for each household size
    one_person_houses = household_lists[1]
    two_person_houses = household_lists[2]
    three_person_houses = household_lists[3]
    four_person_houses = household_lists[4]
    five_person_houses = household_lists[5]
    six_person_houses = household_lists[6]
    seven_person_houses = household_lists[7]
    eight_person_houses = household_lists[8]
    
    Couple_only_house_count = Couple_count - Couples_with_kids_count 
    # Calculate the total number of households
    total_households = Single_house_count + Couples_with_kids_count + Single_with_kids_count + Couple_only_house_count + Student_House_Count + Cohabiting_House_Count
    
    # Calculate the percentage of each household type
    single_house_percentage = (Single_house_count / total_households) * 100
    couples_with_kids_percentage = (Couples_with_kids_count / total_households) * 100
    one_parent_with_kids_percentage = (Single_with_kids_count / total_households) * 100
    couple_only_house_percentage = (Couple_only_house_count / total_households) * 100
    student_house_percentage = (Student_House_Count / total_households) *100
    cohabiting_house_percentage = (Cohabiting_House_Count/ total_households)*100
    
    # Creating labels for the bar chart and plotting it
    percentages = [single_house_percentage, couples_with_kids_percentage, one_parent_with_kids_percentage, couple_only_house_percentage, student_house_percentage, cohabiting_house_percentage]
    
    # Variables to store counts for genders and ages
    gender_counts = {'Male': 0, 'Female': 0}
    age_counts = {}
    
    # Iterate through each household list and count genders and ages
    for household_list in household_lists.values():
        for household in household_list:
            for person in household:
                age, gender, marriage_status = person
                gender_counts[gender] += 1
                if age in age_counts:
                    age_counts[age] += 1
                else:
                    age_counts[age] = 1
    
    total_individuals = sum(gender_counts.values())
    
    # Calculate percentages for genders
    gender_percentages = {gender: (count / total_individuals) * 100 for gender, count in gender_counts.items()}
    
    # Calculate percentages for ages
    age_percentages = {age:(count / total_individuals) * 100 for age, count in age_counts.items()}
    age_percentages_array = numpy.zeros(101)  # 101 is the number of ages from 0 to 100
    
    # Assign the calculated percentages to their respective ages in the array
    for age, percentage in age_percentages.items():
        age_percentages_array[int(age)] = percentage
    
    gender_values = [gender_percentages['Male'], gender_percentages['Female']]
    
    # Calculate the total number of households
    total_households = sum(len(household_lists[size]) for size in House_Sizes)
    
    # Calculate the proportion of each house type
    proportions = [len(household_lists[size]) / total_households * 100 for size in House_Sizes]
    
    return one_person_houses, two_person_houses, three_person_houses, four_person_houses, five_person_houses, six_person_houses, seven_person_houses, eight_person_houses, \
        percentages, age_percentages_array, Age_Distribution, gender_values, Gender_Distribution, House_Sizes, proportions, Household_Size_Distribution

#%% Migration

def net_migration(Area_Of_Interest, Num_People):

    #Setting the area of interest for the model(Getting indexes to extract correct data)
    Index_mapping = {'Derby': 0, 'Derbyshire': 1, 'Leicester': 2, 'Leicestershire': 3, 'Lincolnshire': 4,
                      'North Northamptonshire': 5, 'Nottingham': 6, 'Nottinghamshire': 7, 'Rutland': 8,
                      'West Northamptonshire': 9, 'East Midlands': 10}
    if Area_Of_Interest in Index_mapping:
        Index_value = Index_mapping[Area_Of_Interest]
    Area_Of_Interest = Area_Of_Interest + '%'
    
    #File path for file with all data
    file_path = r"Group Project Statistics - East Midlands.xlsx"
    
    #Extracting all needed data from the file
    Gender_Distribution_Data = pd.read_excel(file_path, sheet_name='Gender Distribution')
    Age_Distribution_Data = pd.read_excel(file_path, sheet_name='Age Distribution')
    Household_Composition_Data = pd.read_excel(file_path, sheet_name='Household Composition')
    Housing_Occupancy_Rating_Data = pd.read_excel(file_path, sheet_name='Housing Occupancy rating')
    Bedrooms_Distribution_Data = pd.read_excel(file_path, sheet_name='Bedrooms Distribution')
    Number_Of_Households_Data = pd.read_excel(file_path, sheet_name='Number of Households')
    Household_Size_Distribution_Data = pd.read_excel(file_path, sheet_name='Housing Distribution')
    Marriage_Gap_Data = pd.read_excel(file_path, sheet_name='Marriage Gap')
    Age_Of_Birth_Data = pd.read_excel(file_path, sheet_name='Age of Birth')
    Marriage_Distribution = pd.read_excel(file_path, sheet_name='Percentage each age married')
    Living_At_Home_Age_Distribution = pd.read_excel(file_path, sheet_name='Percentage each age living home')
    
    #Age distribution of people in the chosen area for simulation
    Age_Distribution = Age_Distribution_Data[Area_Of_Interest].values
    Age_Distribution = Age_Distribution[1:]
    Ages=numpy.linspace(0,100, num=101)
    
    #Gender distribution of people in the chosen area for simulation
    Gender_Data = Gender_Distribution_Data.iloc[Index_value]
    Gender_Distribution = Gender_Data[['Male', 'Female']]
    Gender = ('Male', 'Female')
    
    #Marriage gap distribution
    Marriage_Gap_Distribution = Marriage_Gap_Data['Percentage%']
    Marriage_Gaps = Marriage_Gap_Data['Gap']
    
    #Age of Birth Distribution
    Age_of_Birth_Distribution = Age_Of_Birth_Data['Chance Mother gives birth at this age given birth'].values
    Ages_of_Birth = Age_Of_Birth_Data['Age of Mother']
    
    #House size distibution in chosen area
    Household_Size_Distribution = Household_Size_Distribution_Data.iloc[Index_value]
    Household_Size_Distribution = Household_Size_Distribution[['1 Person%', '2 Person%', '3 Person%', '4 Person%', '5 Person%', '6 Person%', '7 Person%', '8+ Person%']]
    Household_Size_Distribution = Household_Size_Distribution.astype(float)
    House_Sizes = (1,2,3,4,5,6,7,8)
    
    #Chances each person is married depending on gender
    Male_Marriage_Distribution = Marriage_Distribution['Males 2019%'].values
    Marriage_Ages = Marriage_Distribution['Ages'].values
    Female_Marriage_Distribution = Marriage_Distribution['Females 2019%'].values
    
    #Composition of single households from data in file
    Single_House_Composition = Household_Composition_Data[Area_Of_Interest].values
    Single_House_Composition = Single_House_Composition[2:4]
    Young_Ages = numpy.linspace(18,65, num=48)
    Old_Age_Distribution = Age_Distribution[66:]
    Old_Ages = numpy.linspace(66,100, num=35)
    Young_Age_Distribution =Age_Distribution[17:65]
    Total_Single_House_Percentage = Single_House_Composition[0]+Single_House_Composition[1]
    
    # Initialize dictionaries to store lists of people in each household size
    House = []
    household_lists = {size: [] for size in House_Sizes}
    People_Processed = 0
    
    #Keeping count of different household types
    Single_house_count = 0 
    Couples_with_kids_count = 0
    Couple_count = 0
    Couple_only_house_count = 0
    Single_with_kids_count = 0
    People_Processed = 0
    
    #Keeps sorting people into houses till it meets the population
    while People_Processed < Num_People:
        House = []
        Random_House_Size = random.choices(House_Sizes, weights=Household_Size_Distribution, k=1)[0]
        random_number = random.random()

        #If house for 1, makes sure they're 18+ and assigns a person to the house according to the distributions
        if Random_House_Size == 1:  
            Random_Number = random.random()
            if Random_Number >0.8:
                continue
            person = None
            while person is None or person[0] <= 17:
                Random_number  = random.uniform(0, Total_Single_House_Percentage)
                if Random_number < Single_House_Composition[0]:
                    Random_Age = random.choices(Old_Ages, weights=Old_Age_Distribution, k=1)[0]
                else:
                    Random_Age = random.choices(Young_Ages, weights=Young_Age_Distribution, k=1)[0]
                Random_Gender = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                Marriage_Status = 'Single'
                person = (Random_Age, Random_Gender, Marriage_Status)
            House.append(person)
            #People_Processed +=1
            Single_house_count +=1
        #If house size is 2,finds a head of the house according to distributions    
        elif Random_House_Size >= 2:
            person = None
            while person is None or person[0] <= 17:
                Random_Age = random.choices(Ages, weights=Age_Distribution, k=1)[0]
                Random_Gender = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                person = (Random_Age, Random_Gender)
            #Finds the marriage chance for the head of the house depending on age and gender
            if Random_Gender == 'Male':
                marriage_Distribution = Male_Marriage_Distribution
            if Random_Gender == 'Female':
                marriage_Distribution = Female_Marriage_Distribution
            marriage_age_index = int(Random_Age - 18)
            marriage_percentage = marriage_Distribution[marriage_age_index]
            # Determines marriage status then adds them to the house list
            random_number = random.uniform(0, 100)
            if random_number <= marriage_percentage:
                Marriage_Status = 'Married'
            else:
                Marriage_Status = 'Single'
            person = (Random_Age, Random_Gender, Marriage_Status)
            House.append(person)
            #People_Processed +=1 
            Age_of_head = person[0]
            Gender_of_head = person[1]
            #If the head is married,finds age of partner from marriage gap distribution( Makes sure 18+ and less than 100)
            if Marriage_Status == 'Married':
                Random_Marriage_Gap = random.choices(Marriage_Gaps, weights=Marriage_Gap_Distribution, k=1)[0]
                if Gender_of_head == 'Male':
                    Gender_of_partner = 'Female'
                    Age_of_partner = Age_of_head + Random_Marriage_Gap
                    while Age_of_partner > 100 or Age_of_partner < 18:
                        Random_Marriage_Gap = random.choices(Marriage_Gaps, weights=Marriage_Gap_Distribution, k=1)[0]
                        Age_of_partner = Age_of_head + Random_Marriage_Gap
                    partner = (Age_of_partner, Gender_of_partner, Marriage_Status)               
                    House.append(partner)
                    #People_Processed +=1
                    Couple_count +=1
                    Age_Of_Mother = partner[0] 
                    Age_Of_Father = person[0]
                elif Gender_of_head == 'Female':
                    Gender_of_partner = 'Male'
                    Age_of_partner = Age_of_head - Random_Marriage_Gap
                    while Age_of_partner > 100 or Age_of_partner < 18:
                        Random_Marriage_Gap = random.choices(Marriage_Gaps, weights=Marriage_Gap_Distribution, k=1)[0]
                        Age_of_partner = Age_of_head + Random_Marriage_Gap
                    partner = (Age_of_partner, Gender_of_partner, Marriage_Status)
                    House.append(partner)
                    #People_Processed +=1
                    Couple_count+=1
                    Age_Of_Mother = person[0]
                    Age_Of_Father = partner[0]
            #If head isn't married, assign the parent a kid making sure age gap is more than 16 and the kid is 0+ years old
            else:
                Age_Of_Mother = Age_of_head
                Age_Of_Father = Age_of_head
                Age_Of_First_Pregnancy = random.choices(Ages_of_Birth, weights=Age_of_Birth_Distribution, k=1)[0]
                Age_Of_First_Child = Age_Of_Mother - Age_Of_First_Pregnancy
                Age_Of_Father_At_Birth = Age_Of_Father - Age_Of_First_Child
                Marriage_Status = 'Child'
                #Regulatory conditions to make sure the age of the kid follows correct distribution
                if Age_Of_First_Child > -1 and Age_Of_Father_At_Birth > 16 and Age_Of_First_Child <26:
                    Gender_Of_First_Child = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                    House.append((Age_Of_First_Child, Gender_Of_First_Child, Marriage_Status))
                    #People_Processed +=1
                    Single_with_kids_count +=1
                elif 24 < Age_Of_First_Child < 36 and Age_Of_Father_At_Birth > 16:
                    Random_Number = random.random()
                    if Random_Number >0.6:
                        House.pop()
                        #People_Processed -=1
                        continue
                    else:
                        Gender_Of_First_Child = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                        House.append((Age_Of_First_Child, Gender_Of_First_Child, Marriage_Status))
                        #People_Processed +=1
                        Single_with_kids_count +=1
                else:
                    House.pop()
                    #People_Processed-=1
                    continue
        #If house size 3+,assigns more children to the houses depending on the house size according to same process as above
        if Random_House_Size >= 3:
            repeats = Random_House_Size - 2
            for i in range (repeats):
                Age_Of_First_Pregnancy = random.choices(Ages_of_Birth, weights=Age_of_Birth_Distribution, k=1)[0]
                Age_Of_First_Child = Age_Of_Mother - Age_Of_First_Pregnancy
                Age_Of_Father_At_Birth = Age_Of_Father - Age_Of_First_Child
                if Age_Of_First_Child >35:
                    #People_Processed -=len(House)
                    House.clear()
                    continue
                if 24< Age_Of_First_Child <36:
                    Random_Number = random.random()
                    if Random_Number >0.6:
                        #People_Processed -=len(House)
                        House.clear()
                        continue
                Marriage_Status = 'Child'
                while Age_Of_First_Child < 0 or Age_Of_Father_At_Birth < 16:
                    Age_Of_First_Pregnancy = random.choices(Ages_of_Birth, weights=Age_of_Birth_Distribution, k=1)[0]
                    Age_Of_First_Child = Age_Of_Mother - Age_Of_First_Pregnancy
                    Age_Of_Father_At_Birth = Age_Of_Father - Age_Of_First_Child
                Gender_Of_First_Child = random.choices(Gender, weights=Gender_Distribution, k=1)[0]
                House.append((Age_Of_First_Child, Gender_Of_First_Child, Marriage_Status))
                #People_Processed +=1
            Couples_with_kids_count +=1
            
        #Adds the house to the list of the correct house size
        if len(House)==Random_House_Size:
            People_Processed += len(House)
            household_lists[Random_House_Size].append(House)
        else:
            continue
                
    # The lists for each household size
    one_person_houses = household_lists[1]
    two_person_houses = household_lists[2]
    three_person_houses = household_lists[3]
    four_person_houses = household_lists[4]
    five_person_houses = household_lists[5]
    six_person_houses = household_lists[6]
    seven_person_houses = household_lists[7]
    eight_person_houses = household_lists[8]
    
    return one_person_houses, two_person_houses, three_person_houses, four_person_houses, five_person_houses, six_person_houses, seven_person_houses, eight_person_houses

#%% Uniform sampler

def uniform(prob):
    
    sample = numpy.random.uniform(0,1)
    if sample <= prob:
        return True
    else:
        return False 


#%% Death event function

def death_event(house_array, death_prob_m, death_prob_f):
    
    death_prob_m[-1] = 1
    death_prob_f[-1] = 1
    
    counter_house_removed = 0
    Num_deaths = 0
    
    for i in range(len(house_array)):
        occupants = house_array[i-counter_house_removed]
        counter_death2 = 0
        check_for_partner = 0
        for j in range(len(occupants)):
            person = occupants[j-counter_death2]
            
            if person[2] == 'Student':
                continue
            
            elif person[1] == 'Male':
                age = int(person[0])
                death_prob = death_prob_m[age]
                if uniform(death_prob) == True:
                    house_array[i-counter_house_removed].remove(person)
                    counter_death2 += 1
                    check_for_partner = 1
                    Num_deaths += 1
                    
            elif person[1] == 'Female':
                age = int(person[0])
                death_prob = death_prob_f[age]
                if uniform(death_prob) == True:
                    house_array[i-counter_house_removed].remove(person)
                    counter_death2 += 1
                    check_for_partner = 1
                    Num_deaths += 1
         
        if len(occupants) == 0:
            house_array.remove(occupants)
            counter_house_removed += 1

        else:
            if check_for_partner == 1:
                for f in range(len(occupants)):
                    person = occupants[f]
                    if person[2] == 'Married':
                        house_array[i-counter_house_removed].remove(person)
                        house_array[i-counter_house_removed].append((person[0],person[1],'Single'))
                
    return house_array, Num_deaths

#%% Birth event function

def birth_event(house_array,birth_prob):
    
    Num_Births = 0
    for i in range(len(house_array)):
        occupants = house_array[i]
        for j in range(len(occupants)):
            if occupants[j][1] == 'Female' and occupants[j][2] == 'Married':
                number_of_children = len(occupants) - 2
                mother = occupants[j]
                
                age = int(mother[0])
                prob = birth_prob[age-16]
                if uniform(prob) == True:
                    if uniform(0.5) == True:
                        sex = 'Female'
                    else:
                        sex = 'Male'
                    house_array[i].append((0.0,sex,'Child'))
                    Num_Births += 1
                
    return house_array, Num_Births

#%% Leaving home event function

def leaving_home_event(one_person_houses,house_array,leaving_home_prob):
    
    Num_leave = 0
    for i in range(len(house_array)):
        occupants = house_array[i]
        leaving_count = 0
        for j in range(len(occupants)):
            if occupants[j-leaving_count][0] >= 18 and occupants[j-leaving_count][2] == 'Child':
                child = occupants[j-leaving_count]
                age = int(child[0])

                prob = leaving_home_prob[age-18]
                if uniform(prob) == True:
                    house_array[i].remove(child)
                    one_person_houses.append([(child[0],child[1],'Single')])
                    leaving_count += 1
                    Num_leave += 1
                
    return one_person_houses, house_array, Num_leave

#%% Dissolution event function

def dissolution_event(one_person_houses,house_array, dissolution_prob):
    
    Num_Divorce = 0
    dissolution_count = 0
    for i in range(len(house_array)):
        occupants = house_array[i-dissolution_count]
        male = 0
        female = 0
        got_a_married_male = 0
        got_a_married_female = 0
        
        for j in range(len(occupants)):
            
            if occupants[j][1] == 'Male' and occupants[j][2] == 'Married':
                male = occupants[j]
                index_m = j
                got_a_married_male = 1
                
            if occupants[j][1] == 'Female' and occupants[j][2] == 'Married':
                female = occupants[j]
                index_f = j
                got_a_married_female = 1
        
        if got_a_married_male == 1 and got_a_married_female == 1:
                
            male_age = male[0]
            female_age = female[0]
            
            avg_age = 0.5*(male_age + female_age)
            avg_age = numpy.round(avg_age)
            avg_age = int(avg_age)
            
            prob = dissolution_prob[avg_age - 18]
            if uniform(prob) == True:
                Num_Divorce += 1
                if uniform(0.5) == True:
                    leaver = 'Male'
                else:
                    leaver = 'Female'
                
                if leaver == 'Male':
                    house_array[i-dissolution_count][index_f] = (female[0],female[1],'Single')
                    house_array[i-dissolution_count].remove(male)
                    one_person_houses.append([(male[0],male[1],'Single')])
                
                if leaver == 'Female':
                    house_array[i-dissolution_count][index_m] = (male[0],male[1],'Single')
                    house_array[i-dissolution_count].remove(female)
                    one_person_houses.append([(female[0],female[1],'Single')])
                    
    return one_person_houses, house_array, Num_Divorce

#%% Marriage event function

def marriage_event(one_person_houses,two_person_houses,three_person_houses,
                   four_person_houses,five_person_houses,six_person_houses,
                   seven_person_houses,eight_person_houses,marriage_male,marriage_female):
    
    eligible_males =[]
    eligible_females =[]
    
    houses_to_remove = []
    all_new_houses = []
    new_house_twos = []
    
    house_arrays = [one_person_houses,two_person_houses,three_person_houses,
                   four_person_houses,five_person_houses,six_person_houses,
                   seven_person_houses,eight_person_houses]
    
    for a in range(len(house_arrays)):
        houses = house_arrays[a]
        for i in range(len(houses)):
            occupants = houses[i]
            one_marriage_only = 0
            for j in range(len(occupants)):
                person = occupants[j]
                if one_marriage_only == 1:
                    continue
                
                if person[2] != 'Student' and person[2] != 'Married' and person[2] != 'Cohabiting' and person[0] >= 18:
                    age = int(person[0])
                    if person[1] == 'Male':
                        prob = marriage_male[age-18]
                        if uniform(prob) == True:
                            eligible_males.append([age,a,i,person])
                            one_marriage_only = 1
                    if person[1] == 'Female':
                        prob = marriage_female[age-18]
                        if uniform(prob) == True:
                            eligible_females.append([age,a,i,person])
                            one_marriage_only = 1
                        
    difference = len(eligible_males) - len(eligible_females)
    difference_abs = abs(difference)
    
    if difference < 0:
        for b in range(difference_abs):
            remove = random.randint(0,len(eligible_females)-1)
            eligible_females.remove(eligible_females[remove])
        
    if difference > 0:
        for b in range(difference_abs):
            remove = random.randint(0,len(eligible_males)-1)
            eligible_males.remove(eligible_males[remove])
            
    eligible_females.sort()
    eligible_males.sort()
    Num_Marriages = len(eligible_males)
    
    for z in range(len(eligible_males)):
        
        male_needs_to_move_out = False
        female_needs_to_move_out = False
        
        house_size_of_male = eligible_males[z][1]
        house_array_m = house_arrays[house_size_of_male]
        male_household = house_array_m[eligible_males[z][2]]

        house_size_of_female = eligible_females[z][1]
        house_array_f = house_arrays[house_size_of_female]
        female_household = house_array_f[eligible_females[z][2]]
        
        for check_married_m in range(len(male_household)):
            person = male_household[check_married_m]
            if person[2] == 'Married':
                male_needs_to_move_out = True
                
        for check_married_f in range(len(female_household)):
            person = female_household[check_married_f]
            if person[2] == 'Married':
                female_needs_to_move_out = True
        
        # Create new houses where both people need to move out
        if male_needs_to_move_out == True and female_needs_to_move_out == True:
            # Remove individuals
            house_arrays[house_size_of_male][eligible_males[z][2]].remove(eligible_males[z][3])
            house_arrays[house_size_of_female][eligible_females[z][2]].remove(eligible_females[z][3])
            
            male = eligible_males[z][3]
            male = (male[0],male[1],'Married')
            
            female = eligible_females[z][3]
            female = (female[0],female[1],'Married')
            
            #Create new two person home
            new_house_twos.append([male,female])
            
        # Instance only man needs to move out
        if male_needs_to_move_out == True and female_needs_to_move_out == False:
            
            # Remove man from house
            house_arrays[house_size_of_male][eligible_males[z][2]].remove(eligible_males[z][3])
            
            # Add male to other house
            male = eligible_males[z][3]
            male = (male[0],male[1],'Married')
            female = eligible_females[z][3]
            female_household.remove(female)
            female_household.append((female[0],female[1],'Married'))
            
            new_house = female_household + [male]
            
            # Update tags
            for j in range(len(new_house)):
                person = new_house[j]
                if person[2] == 'Single':
                    new_house[j] = (person[0],person[1],'Married')
                    
            houses_to_remove.append([female_household,house_size_of_female])
            
            all_new_houses.append(new_house)
        
        # Instance only female needs to move out
        if male_needs_to_move_out == False and female_needs_to_move_out == True:
            
            # Remove man from house
            house_arrays[house_size_of_female][eligible_females[z][2]].remove(eligible_females[z][3])
            
            # Add male to other house
            female = eligible_females[z][3]
            female = (female[0],female[1],'Married')
            male = eligible_males[z][3]
            male_household.remove(male)
            male_household.append([male[0],male[1],'Married'])
            
            new_house = male_household + [female]
            
            # Update tags
            for j in range(len(new_house)):
                person = new_house[j]
                if person[2] == 'Single':
                    new_house[j] = (person[0],person[1],'Married')
                    
            houses_to_remove.append([male_household,house_size_of_male])
            
            all_new_houses.append(new_house)
        
        # Instance nobody moves out
        if male_needs_to_move_out == False and female_needs_to_move_out == False:
            
            new_house = female_household + male_household
        
            for j in range(len(new_house)):
                person = new_house[j]
                if person[2] == 'Single':
                    new_house[j] = (person[0],person[1],'Married')
            
            houses_to_remove.append([male_household,house_size_of_male])
            houses_to_remove.append([female_household,house_size_of_female])
            
            all_new_houses.append(new_house)
    
    if len(houses_to_remove) > 0:
        for h in range(len(houses_to_remove)):
            house_getting_removed = houses_to_remove[h][0]
            size_of_removal = houses_to_remove[h][1]
            house_arrays[size_of_removal].remove(house_getting_removed)
            
    if len(all_new_houses)  > 0:  
        for t in range(len(all_new_houses)):
            new_house_to_add = all_new_houses[t]
            
            size_of_house = len(new_house_to_add)-1
            
            if size_of_house >= 8:
                size_of_house = 7
            
            house_arrays[size_of_house].append(new_house_to_add)
        
    one_person_houses = house_arrays[0]
    two_person_houses = house_arrays[1]
    three_person_houses = house_arrays[2]
    four_person_houses = house_arrays[3]
    five_person_houses = house_arrays[4]
    six_person_houses = house_arrays[5]
    seven_person_houses = house_arrays[6]
    eight_person_houses = house_arrays[7]
    
    two_person_houses = two_person_houses + new_house_twos
      
    return one_person_houses, two_person_houses, three_person_houses, four_person_houses, five_person_houses, six_person_houses, seven_person_houses, eight_person_houses, Num_Marriages

#%% Cohabiting event

def cohabiting_event(one_person_houses, Area_Of_Interest):
    
    #Setting the area of interest for the model(Getting indexes to extract correct data)
    Index_mapping = {'Derby': 0, 'Derbyshire': 1, 'Leicester': 2, 'Leicestershire': 3, 'Lincolnshire': 4,
                      'North Northamptonshire': 5, 'Nottingham': 6, 'Nottinghamshire': 7, 'Rutland': 8,
                      'West Northamptonshire': 9, 'East Midlands': 10}
    if Area_Of_Interest in Index_mapping:
        Index_value = Index_mapping[Area_Of_Interest]
    Area_Of_Interest = Area_Of_Interest + '%'
    
    #File path for file with all data
    file_path = r"Group Project Statistics - East Midlands.xlsx"
    Household_Size_Distribution_Data = pd.read_excel(file_path, sheet_name='Housing Distribution')
    
    #House size distibution in chosen area
    Household_Size_Distribution = Household_Size_Distribution_Data.iloc[Index_value]
    Household_Size_Distribution = Household_Size_Distribution[['1 Person%', '2 Person%', '3 Person%', '4 Person%', '5 Person%', '6 Person%', '7 Person%', '8+ Person%']]
    Household_Size_Distribution = Household_Size_Distribution.astype(float)
    House_Sizes = (1,2,3,4,5,6,7,8)
    
    Elderly_People = []
    Num_cohabits = 0
    
    # Find eligible candidates
    for possible_elderly in range(len(one_person_houses)):
        household = one_person_houses[possible_elderly-Num_cohabits]
        possible_candidate = household[0]
        age = possible_candidate[0]
        if age >= 55:
            if possible_candidate[2] == 'Single':
                if uniform(0.03) == True:
                    one_person_houses.remove(household)
                    Elderly_People.append(possible_candidate)
                    Num_cohabits += 1
    
    People_Processed = 0
    while People_Processed < len(Elderly_People):
        House = []
        Random_House_Size = 1
        while Random_House_Size == 1:
            Random_House_Size = random.choices(House_Sizes, weights=Household_Size_Distribution, k=1)[0]  
        for size in range(Random_House_Size):
            if len(Elderly_People) < size:
                for leftover in range(len(Elderly_People)):
                    one_person_houses.append([Elderly_People[leftover]])
                    
            else:
                person = Elderly_People[0]
                Elderly_People.remove(person)
                person = (person[0],person[1],'Cohabiting')
                House.append(person)
        one_person_houses.append(House)
            
    return one_person_houses, Num_cohabits

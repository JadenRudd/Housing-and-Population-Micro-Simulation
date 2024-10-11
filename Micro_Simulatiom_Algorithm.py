import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Micro_Simulation_Functions as MSF
from tqdm import tqdm

#%% The micro-simulation algorithm

def micro_simulation(Area, Years_To_Run = 126, Non_Optimal = False, Num_of_People = None):
    '''
    Run micro-simulation of housing in a specified local county of the East Midlands.

    Parameters
    ----------
    Area : str
        Can take one of ten values; 
            'Derby', 
            'Derbyshire', 
            'Leicester', 
            'Leicestershire',
            'Nottingham', 
            'Nottinghamshire', 
            'Rutland', 
            'Lincolnshire', 
            'West Northamptonshire', 
            'North Northamptonshire'.
    Years_To_Run : int, optional
        The number of years to simulate. The default is 126.
    Non_Optimal : bool, optional
        Decides if bedrooms should be sorted optimally or not,
        i.e. sharing/surplus, default assigns bedrooms optimally. The default is False.
    Num_of_People : int, optional
        The amount of people to simulate, allows smaller samples to save run time.
        The default is the areas population in 2021.
    '''
    
    #Use for making graphs
    years = []
    num_houses = []
    population = []

    proportion_single_only_list = []
    proportion_single_with_kids_list = []
    proportion_married_no_kids_list = []
    proportion_married_with_kids_list = []
    proportion_students_list = []
    proportion_cohabiting_list = []
    
    proportion_one = []
    proportion_two = []
    proportion_three = []
    proportion_four = []
    proportion_five = []
    proportion_six = []
    proportion_seven = []
    proportion_eight = []
    
    proportion_one_beds = []
    proportion_two_beds = []
    proportion_three_beds = []
    proportion_four_beds = []
    proportion_five_beds = []
    proportion_six_beds = []
    proportion_seven_beds = []
    proportion_eight_beds = []
    
    avg_bedroom_house_size_list = []
    avg_house_size_list = []
    
    # Total life events
    Deaths = []
    Births = []
    Leaving = []
    Divorce = []
    Marriage = []
    Cohabits = []
    
    # Import initial population
    if Num_of_People == None:   
        Num_of_People = pd.read_csv('Population_start.csv')
        Num_of_People = Num_of_People.at[0,Area]
    
    # Import death probs
    df_m = pd.read_csv('Male_Mortality_Rates.csv')
    df_f = pd.read_csv('Female_Mortality_Rates.csv')
    
    # Retrieve death probs
    death_prob_m = np.array(df_m[Area])
    death_prob_f = np.array(df_f[Area])
    
    # Import birth probs
    df = pd.read_csv('Birth_Rates.csv')
    x = df.loc[df['Area'] == Area]
    birth_prob = np.r_[np.array(x['Mean ']),np.zeros(115)]
    
    # Leaving home probs
    leaving_home_prob = np.linspace(0,0.001,151)
    leaving_home_prob[-1] = 1

    # Dissolution probs
    dissolution_prob = (1/1000) * np.array([0.2197909,0.2197909,2.5169895,4.3603349,5.8173099,6.9489447,7.8101030,8.4497695,8.9113364,9.2328902,9.4474986,9.5834974,9.6647771,9.7110700,9.7382370,9.7585540,9.7809993,9.8115403,9.8534200,9.9074441,9.9722677,10.0446824,10.1199028,10.1918533,10.2534554,10.2969140,10.3140045,10.2963595,10.2357557,10.1244008,9.9552202,9.7221438,9.4203930,9.0467675,8.5999318,8.0807024,7.4923347,6.8408094,6.1351197,5.3875578,4.6140021,3.8342040,3.0720741,2.3559699,1.7189822,1.1992217,0.8401064,0.6906479])
    dissolution_prob = np.r_[dissolution_prob,np.zeros(103)]
    
    # Marriage probs
    marriage_male = (1/1000) * np.array([1.242917,1.242917,1.242917,1.242711,3.857922,8.190577,13.50604,19.21586,24.86146,30.09865,34.68295,38.45583,41.33168,43.28571,44.34258,44.56599,44.04898,42.90517,41.26075,39.24736,36.99578,34.63048,32.26495,29.99793,27.91043,26.06361,24.49745,23.23035,22.25944,21.56182,21.09659,20.80774,20.62785,20.48262,20.29628,19.99779,19.52788,18.84695,17.94377,16.84505,15.6258,14.42061,13.43561,13.18802,12.52038,11.87009,11.23713,10.62152,10.02324,9.442311,8.87872,8.332471,7.803563,7.291996,6.79777,6.320886,5.861342,5.419141,4.99428,4.586761,4.196583,3.823746,3.46825,3.130096,2.809282,2.505811,2.21968,1.950891,1.699443,1.465336,1.24857,1.049146,0.867063,0.702321,0.55492,0.424861,0.312143,0.216766,0.13873,0.078036,0.034683,0.008671,0])
    marriage_male = np.r_[marriage_male,np.zeros(68)]
    marriage_female = (1/1000) * np.array([3.463998,3.463998,0.87788,3.177305,8.558697,15.60956,23.25308,30.69759,37.39063,42.97753,47.26415,50.18374,51.76754,52.11912,51.39207,49.77091,47.45512,44.64585,41.53539,38.29893,35.08863,32.02963,29.2179,26.71971,24.57242,22.78661,21.34903,20.22648,19.37024,18.72084,18.21307,17.78094,17.36245,16.90386,16.36345,15.71433,14.94628,14.06634,13.09799,12.0786,11.05516,10.07781,8.53518,8.113755,7.773286,7.190713,6.560569,5.677812,6.166668,5.809257,5.462515,5.126443,4.801039,4.486304,4.182238,3.888841,3.606114,3.334055,3.072665,2.821944,2.581892,2.352509,2.133795,1.92575,1.728374,1.541667,1.365629,1.20026,1.04556,0.901528,0.768166,0.645473,0.533449,0.432093,0.341407,0.26139,0.192042,0.133362,0.085352,0.04801,0.021338,0.005334,0])
    marriage_female = np.r_[marriage_female,np.zeros(68)]
    
    Index_mapping = {'Derby': 0, 'Derbyshire': 1, 'Leicester': 2, 'Leicestershire': 3, 'Lincolnshire': 4,
                      'North Northamptonshire': 5, 'Nottingham': 6, 'Nottinghamshire': 7, 'Rutland': 8,
                      'West Northamptonshire': 9, 'East Midlands': 10}
    Index_value = Index_mapping[Area]
    
    #Import Occupancy Probabilities
    df_occupancy = pd.read_excel('Group Project Statistics - East Midlands.xlsx', sheet_name = 'Housing Occupancy rating')
    Occupancy_prob = df_occupancy.iloc[Index_value]
    Occupancy_prob = Occupancy_prob[['Occupancy +2%', 'Occupancy +1%', 'Occupancy 0%', 'Occupancy -1%', 'Occupancy -2%']]
    Occupancy_sizes = (2,1,0,-1,-2)
    
    #Occupancy for married and singles as they cant be overcrowded
    Occupancy_prob_2 = Occupancy_prob[['Occupancy +2%', 'Occupancy +1%', 'Occupancy 0%']]
    Occupancy_sizes_2 = (2,1,0)
    
    # Inital
    one, two, three, four, five, six, seven, eight, percentages, age_percentages_array, Age_Distribution, gender_values, Gender_Distribution, House_Sizes, proportions, Household_Size_Distribution = MSF.initial_population(Area, Num_of_People)
    
    for i in tqdm (range (Years_To_Run), desc=f"{Area} progress"):
        
        # Scale birth and death probabilities
        year = 2024 + i 
        years.append(year+1)
        year = str(year)
        
        # Event counter initialisation
        Num_of_Deaths = 0
        Num_of_Births = 0
        Num_of_Leaving = 0
        Num_of_Divorce = 0
        Num_of_Marriages = 0
        Num_of_Cohabits = 0
        
        Num_of_Deaths_i = 0
        Num_of_Births_i = 0
        Num_of_Leaving_i = 0
        Num_of_Divorce_i = 0
        Num_of_Marriages_i = 0
        Num_of_Cohabits_i = 0
        
        # Marriage
        one, two, three, four, five, six, seven, eight, Num_of_Marriages_i = MSF.marriage_event(one, two, three, four, five, six, seven, eight,marriage_male,marriage_female)
        
        house_arrays = [one,two,three,four,five,six,seven,eight]
        
        # Life events
        for j in range(8):
            
            # Select house size
            house_array = house_arrays[j]
            
            # If more than one person
            if j > 1:
                
                # Birth
                house_array, Num_of_Births_i = MSF.birth_event(house_array, birth_prob)
                
                # Dissolution
                house_arrays[0], house_array, Num_of_Divorce_i = MSF.dissolution_event(house_arrays[0], house_array, dissolution_prob)
                
                # Leaving home
                house_arrays[0], house_array, Num_of_Leaving_i = MSF.leaving_home_event(house_arrays[0], house_array, leaving_home_prob)
                
            # Deaths
            house_array, Num_of_Deaths_i = MSF.death_event(house_array, death_prob_m, death_prob_f)
            
            # New house array
            house_arrays[j] = house_array
            
            Num_of_Deaths += Num_of_Deaths_i
            Num_of_Births += Num_of_Births_i
            Num_of_Leaving += Num_of_Leaving_i
            Num_of_Divorce += Num_of_Divorce_i
            Num_of_Marriages += Num_of_Marriages_i
            
        Deaths.append(Num_of_Deaths)
        Births.append(Num_of_Births)
        Leaving.append(Num_of_Leaving)
        Divorce.append(Num_of_Divorce)
        Marriage.append(Num_of_Marriages)
            
        # Sort houses into actual sizes
        for a in range(1,8):
            count = 0
            
            house_array = house_arrays[a]
            house_size_should_be = a+1
            
            for b in range(len(house_array)):
                
                house = house_array[b-count]
                house_size_actual = len(house)
                
                if house_size_actual != house_size_should_be:
                    
                    house_arrays[a].remove(house)
                    
                    if house_size_actual >= 8:
                        house_size_actual = 8
                    
                    house_arrays[house_size_actual-1].append(house)
                    
                    count += 1
            
        # Find kids with no parents and move them
        removal_count = 0
        for ones in range(len(house_arrays[0])):
            possible_child_only_house = house_arrays[0][ones-removal_count]
            child = possible_child_only_house[0]
            
            if child[2] == 'Child':
                house_arrays[0].remove(possible_child_only_house)
                removal_count += 1
                
                if child[0] >= 18:
                    house_arrays[0].append([(child[0],child[1],'Single')])
                
                else:
                    
                    house_size_to_assign = 1
                    while house_size_to_assign < 8:
                        for h in range(len(house_arrays[house_size_to_assign])):
                            if house_size_to_assign == 8:
                                break
                            
                            else:
                                occupants = house_arrays[house_size_to_assign][h]
                                
                                for y in range(len(occupants)):
                                    person = occupants[y]
                                    if person[2] != 'Child' and person[2] != 'Cohabiting' and person[2] != 'Student':
                                        house_arrays[house_size_to_assign][h].append(child)
                                        house_size_to_assign = 8
                                        break
                            
                        house_size_to_assign += 1
                        
        house_arrays[0], Num_of_Cohabits_i = MSF.cohabiting_event(house_arrays[0], Area)  
        Cohabits.append(Num_of_Cohabits_i)
         
        # Sort houses into actual sizes after kids moved and cohabits
        for a in range(1,8):
            count = 0
            
            house_array = house_arrays[a]
            house_size_should_be = a+1
            
            for b in range(len(house_array)):
                
                house = house_array[b-count]
                house_size_actual = len(house)
                
                if house_size_actual != house_size_should_be:
                    
                    house_arrays[a].remove(house)
                    
                    if house_size_actual >= 8:
                        house_size_actual = 8
                    
                    house_arrays[house_size_actual-1].append(house)
                    
                    count += 1
        
        # Add age to everyone except students
        for z in range(8):
            house_array = house_arrays[z]
            
            for k in range(len(house_array)):
                occupants = house_array[k]
                
                for n in range(len(occupants)):
                    person = occupants[n]
                    if person[2] == 'Student':
                        house_array[k][n] = (person[0],person[1],person[2])
                    else:
                        house_array[k][n] = (person[0]+1,person[1],person[2])
                
            house_arrays[z] = house_array
            
        # Add migration
        Net_Migration = Num_of_People * 0.025
        one_migration, two_migration, three_migration, four_migration, five_migration, six_migration, seven_migration, eight_migration = MSF.net_migration(Area, Net_Migration)
        migration_lists = [one_migration, two_migration, three_migration, four_migration, five_migration, six_migration, seven_migration, eight_migration]
        house_lists = [one, two, three, four, five, six, seven, eight]
        for p in range(len(migration_lists)):
            house_lists[p].extend(migration_lists[p])
            
        # Calculate population and number of houses for each year
        total_population = len(one) + 2 * len(two) + 3 * len(three) + 4 * len(four) + 5 * len(five) + 6 * len(six) + 7 * len(seven) + 8 * len(eight)
        total_houses = len(one) + len(two) + len(three) + len(four) + len(five) + len(six) + len(seven) + len(eight)
        
        # Add stuff to lists for graphs
        population.append(total_population)
        num_houses.append(total_houses) 
        
        # Update all arrays
        one = house_arrays[0]
        two = house_arrays[1]
        three = house_arrays[2]
        four = house_arrays[3]
        five = house_arrays[4]
        six = house_arrays[5]
        seven = house_arrays[6]
        eight = house_arrays[7]
        
        proportion_one.append((len(one)/total_houses)*100)
        proportion_two.append((len(two)/total_houses)*100)
        proportion_three.append((len(three)/total_houses)*100)
        proportion_four.append((len(four)/total_houses)*100)
        proportion_five.append((len(five)/total_houses)*100)
        proportion_six.append((len(six)/total_houses)*100)
        proportion_seven.append((len(seven)/total_houses)*100)
        proportion_eight.append((len(eight)/total_houses)*100)
        
        avg_house_size = total_population/total_houses
        avg_house_size_list.append(avg_house_size)
            
        #Keeping track of household types
        single_only_households = 0
        single_with_kids_households = 0
        married_couples_no_kids = 0
        married_with_kids_households = 0
        students = 0
        cohabiting_households = 0
        for z in range(8):
            house_array = house_arrays[z]
            for k in range(len(house_array)):
                occupants = house_array[k]
                if len(occupants) == 1:
                    single_only_households +=1
                else:
                    has_single_adult = False
                    has_married_couple = False
                    has_child = False
                    has_student = False
                    has_cohabitant = False
                    for n in range(len(occupants)):
                        person = occupants[n]
                        if person[2] == 'Student':
                            has_student = True
                        if person[2] == 'Cohabiting':
                            has_cohabitant = True
                        if person[2] == 'Married':
                            has_married_couple = True
                        if person[2] == 'Single':
                            has_single_adult = True
                        if person[2] == 'Child':
                            has_child = True
                    if has_single_adult and has_child:
                        single_with_kids_households += 1
                    if has_married_couple and not has_child:
                        married_couples_no_kids += 1
                    if has_married_couple and has_child:
                        married_with_kids_households += 1
                    if has_student:
                        students += 1
                    if has_cohabitant:
                        cohabiting_households += 1
        
        # Calculate proportions
        proportion_single_only = (single_only_households / total_houses)*100
        proportion_single_with_kids = (single_with_kids_households / total_houses)*100
        proportion_married_no_kids = (married_couples_no_kids / total_houses)*100
        proportion_married_with_kids = (married_with_kids_households / total_houses)*100
        proportion_students = (students / total_houses)*100
        proportion_cohabiting = (cohabiting_households / total_houses)*100
        
        #add to lists
        proportion_single_only_list.append(proportion_single_only)
        proportion_single_with_kids_list.append(proportion_single_with_kids)
        proportion_married_no_kids_list.append(proportion_married_no_kids)
        proportion_married_with_kids_list.append(proportion_married_with_kids)
        proportion_students_list.append(proportion_students)
        proportion_cohabiting_list.append(proportion_cohabiting)
        
        # Sort into bed size
        bedroom_houses = [[] for i in range(8)]
        
        # Sort into beds optimally
        # Create empty lists for bedroom house sizes from one to eight
        for z in range(8):
            house_array = house_arrays[z]
            for k in range(len(house_array)):
                occupants = house_array[k]
                Married_count = 0
                for n in range(len(occupants)):
                    person = occupants[n]
                    if person[2] == 'Married':
                        Married_count += 1
                Married_count = int(Married_count/2)
                Num_Bedrooms = int(len(occupants)-Married_count)
                if Num_Bedrooms >8:
                    bedroom_houses[7].append(occupants)
                else:
                    bedroom_houses[Num_Bedrooms - 1].append(occupants) 
            
        non_optimal_bedroom_houses = [[] for i in range(8)]            
        if Non_Optimal == True:
            #1 bed houses cant decrease in size
            for house in bedroom_houses[0]:
                Random_Occupancy = random.choices(Occupancy_sizes_2, weights=Occupancy_prob_2, k=1)[0]
                non_optimal_bedroom_houses[Random_Occupancy].append(house)
            for i in range(1, 8):  # Iterate through each bedroom size list except the first one
                for house in bedroom_houses[i]:
                    for person in house:
                        if person[2] == 'Cohabiting' or person[2] == 'Student':
                            Random_Occupancy = random.choices(Occupancy_sizes_2, weights=Occupancy_prob_2, k=1)[0]
                        else:
                            Random_Occupancy = random.choices(Occupancy_sizes, weights=Occupancy_prob, k=1)[0]
                    index = i +Random_Occupancy
                    if index > 7:
                        index = 7
                    non_optimal_bedroom_houses[index].append(house)
                    Random_Occupancy = random.choices(Occupancy_sizes_2, weights=Occupancy_prob_2, k=1)[0]
                    non_optimal_bedroom_houses[index].append(house)
            
        if Non_Optimal == True:
            total_houses = len(non_optimal_bedroom_houses[0])+len(non_optimal_bedroom_houses[1])+len(non_optimal_bedroom_houses[2])+len(non_optimal_bedroom_houses[3])+len(non_optimal_bedroom_houses[4])+len(non_optimal_bedroom_houses[5])+len(non_optimal_bedroom_houses[6])+len(non_optimal_bedroom_houses[7])
            avg_bedroom_house_size = ((len(non_optimal_bedroom_houses[0])+(2*len(non_optimal_bedroom_houses[1]))+ (3*len(non_optimal_bedroom_houses[2]))+(4*len(non_optimal_bedroom_houses[3]))+(5*len(non_optimal_bedroom_houses[4]))+(6*len(non_optimal_bedroom_houses[5]))+(7*len(non_optimal_bedroom_houses[6]))+(8*len(non_optimal_bedroom_houses[7])))/total_houses)
            avg_bedroom_house_size_list.append(avg_bedroom_house_size)
            proportion_one_beds.append((len(non_optimal_bedroom_houses[0])/total_houses)*100)
            proportion_two_beds.append((len(non_optimal_bedroom_houses[1])/total_houses)*100)
            proportion_three_beds.append((len(non_optimal_bedroom_houses[2])/total_houses)*100)
            proportion_four_beds.append((len(non_optimal_bedroom_houses[3])/total_houses)*100)
            proportion_five_beds.append((len(non_optimal_bedroom_houses[4])/total_houses)*100)
            proportion_six_beds.append((len(non_optimal_bedroom_houses[5])/total_houses)*100)
            proportion_seven_beds.append((len(non_optimal_bedroom_houses[6])/total_houses)*100)
            proportion_eight_beds.append((len(non_optimal_bedroom_houses[7])/total_houses)*100)  
            
        else:
            avg_bedroom_house_size = ((len(bedroom_houses[0])+(2*len(bedroom_houses[1]))+ (3*len(bedroom_houses[2]))+(4*len(bedroom_houses[3]))+(5*len(bedroom_houses[4]))+(6*len(bedroom_houses[5]))+(7*len(bedroom_houses[6]))+(8*len(bedroom_houses[7])))/total_houses)
            avg_bedroom_house_size_list.append(avg_bedroom_house_size)
            proportion_one_beds.append((len(bedroom_houses[0])/total_houses)*100)
            proportion_two_beds.append((len(bedroom_houses[1])/total_houses)*100)
            proportion_three_beds.append((len(bedroom_houses[2])/total_houses)*100)
            proportion_four_beds.append((len(bedroom_houses[3])/total_houses)*100)
            proportion_five_beds.append((len(bedroom_houses[4])/total_houses)*100)
            proportion_six_beds.append((len(bedroom_houses[5])/total_houses)*100)
            proportion_seven_beds.append((len(bedroom_houses[6])/total_houses)*100)
            proportion_eight_beds.append((len(bedroom_houses[7])/total_houses)*100)
        
        # Sort into beds with sharing and surplus accounted for
        one_bed, two_bed, three_bed, four_bed, five_bed, six_bed, seven_bed, eight_bed = bedroom_houses
        
    house_size_proportions = [proportion_one,proportion_two,proportion_three,proportion_four,proportion_five,proportion_six,proportion_seven,proportion_eight]
    bedroom_size_proportions = [proportion_one_beds, proportion_two_beds, proportion_three_beds, proportion_four_beds, proportion_five_beds, proportion_six_beds, proportion_seven_beds, proportion_eight_beds]
    house_types = [proportion_single_only_list, proportion_single_with_kids_list, proportion_married_no_kids_list, proportion_married_with_kids_list, proportion_students_list, proportion_cohabiting_list]
                    
    return one, two, three, four, five, six, seven, eight, \
        num_houses, population, \
            Deaths, Births, Leaving, Marriage, Divorce, Cohabits, \
                years, \
                    bedroom_houses, avg_house_size_list, avg_bedroom_house_size_list, house_size_proportions, bedroom_size_proportions, house_types, \
                        percentages, age_percentages_array, Age_Distribution, gender_values, Gender_Distribution, House_Sizes, proportions, Household_Size_Distribution

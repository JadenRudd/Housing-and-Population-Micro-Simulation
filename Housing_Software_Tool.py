import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import Micro_Simulatiom_Algorithm as MSA

#%% Docstring

help(MSA.micro_simulation)

#%% Choices

Area_of_Interest = 'North Northamptonshire'
Years_To_Run = 126
Non_Optimal = True
Num_of_People = 5000
No_of_Sims = 10

#%% One sim

Simulation = MSA.micro_simulation(Area_of_Interest, Years_To_Run=Years_To_Run, Num_of_People=Num_of_People, Non_Optimal=Non_Optimal)

#%% Initialise values - One Sim

one = Simulation[0]
two = Simulation[1]
three = Simulation[2]
four = Simulation[3]
five = Simulation[4]
six = Simulation[5]
seven = Simulation[6]
eight = Simulation[7]

num_houses = Simulation[8]
population = Simulation[9]

Deaths = Simulation[10]
Births = Simulation[11]
Leaving = Simulation[12]
Marriage = Simulation[13]
Divorce = Simulation[14]
Cohabits = Simulation[15]

years = Simulation[16]

one_bed, two_bed, three_bed, four_bed, five_bed, six_bed, seven_bed, eight_bed = Simulation[17]

avg_house_size_list = Simulation[18]
avg_bedroom_house_size_list = Simulation[19]

proportion_one,proportion_two,proportion_three,proportion_four,proportion_five,proportion_six,proportion_seven,proportion_eight = Simulation[20]
proportion_one_beds, proportion_two_beds, proportion_three_beds, proportion_four_beds, proportion_five_beds, proportion_six_beds, proportion_seven_beds, proportion_eight_beds = Simulation[21]

proportion_single_only_list, proportion_single_with_kids_list, proportion_married_no_kids_list, proportion_married_with_kids_list, proportion_students_list, proportion_cohabiting_list = Simulation[22]

percentages = Simulation[23]
age_percentages_array = Simulation[24]
Age_Distribution = Simulation[25]
gender_values = Simulation[26]
Gender_Distribution = Simulation[27]
House_Sizes = Simulation[28]
proportions = Simulation[29]
Household_Size_Distribution = Simulation[30]

#%% Averages

no_ones = 0
no_twos = 0
no_threes = 0
no_fours = 0
no_fives = 0
no_sixes = 0
no_sevens = 0
no_eights = 0

num_houses_avg = 0
population_avg = 0

Deaths_avg = 0
Births_avg = 0
Leaving_avg = 0
Marriage_avg = 0
Divorce_avg = 0
Cohabits_avg = 0

avg_house_size_list_avg = 0
avg_bedroom_house_size_list_avg = 0

proportion_one_avg = 0
proportion_two_avg = 0
proportion_three_avg = 0
proportion_four_avg = 0
proportion_five_avg = 0
proportion_six_avg = 0
proportion_seven_avg = 0
proportion_eight_avg = 0

proportion_one_beds_avg = 0
proportion_two_beds_avg = 0
proportion_three_beds_avg = 0
proportion_four_beds_avg = 0
proportion_five_beds_avg = 0
proportion_six_beds_avg = 0
proportion_seven_beds_avg = 0
proportion_eight_beds_avg = 0

proportion_single_only_list_avg = 0
proportion_single_with_kids_list_avg = 0
proportion_married_no_kids_list_avg = 0
proportion_married_with_kids_list_avg = 0
proportion_students_list_avg = 0
proportion_cohabiting_list_avg = 0

population_iterations = []
num_houses_iterations = []
avg_bedroom_house_size_list_iterations = []
avg_house_size_list_iterations = []

for i in range(No_of_Sims):
    
    # Run sim
    Simulation = MSA.micro_simulation(Area_of_Interest, Years_To_Run=Years_To_Run, Num_of_People=Num_of_People, Non_Optimal=Non_Optimal)

    # Initialise values
    no_ones += len(Simulation[0])
    no_twos += len(Simulation[1])
    no_threes += len(Simulation[2])
    no_fours += len(Simulation[3])
    no_fives += len(Simulation[4])
    no_sixes += len(Simulation[5])
    no_sevens += len(Simulation[6])
    no_eights += len(Simulation[7])
    
    num_houses_i = np.array(Simulation[8])
    population_i = np.array(Simulation[9])

    Deaths_i = np.array(Simulation[10])
    Births_i = np.array(Simulation[11])
    Leaving_i = np.array(Simulation[12])
    Marriage_i = np.array(Simulation[13])
    Divorce_i = np.array(Simulation[14])
    Cohabits_i = np.array(Simulation[15])
    
    avg_house_size_list_i = np.array(Simulation[18])
    avg_bedroom_house_size_list_i = np.array(Simulation[19])
    
    proportion_one,proportion_two,proportion_three,proportion_four,proportion_five,proportion_six,proportion_seven,proportion_eight = Simulation[20]
    proportion_one_i = np.array(proportion_one)
    proportion_two_i = np.array(proportion_two)
    proportion_three_i = np.array(proportion_three)
    proportion_four_i = np.array(proportion_four)
    proportion_five_i = np.array(proportion_five)
    proportion_six_i = np.array(proportion_six)
    proportion_seven_i = np.array(proportion_seven)
    proportion_eight_i = np.array(proportion_eight)
    
    proportion_one_beds, proportion_two_beds, proportion_three_beds, proportion_four_beds, proportion_five_beds, proportion_six_beds, proportion_seven_beds, proportion_eight_beds = Simulation[21]
    proportion_one_beds_i = np.array(proportion_one_beds)
    proportion_two_beds_i = np.array(proportion_two_beds)
    proportion_three_beds_i = np.array(proportion_three_beds)
    proportion_four_beds_i = np.array(proportion_four_beds)
    proportion_five_beds_i = np.array(proportion_five_beds)
    proportion_six_beds_i = np.array(proportion_six_beds)
    proportion_seven_beds_i = np.array(proportion_seven_beds)
    proportion_eight_beds_i = np.array(proportion_eight_beds)

    proportion_single_only_list, proportion_single_with_kids_list, proportion_married_no_kids_list, proportion_married_with_kids_list, proportion_students_list, proportion_cohabiting_list = Simulation[22]
    proportion_single_only_list_i = np.array(proportion_single_only_list)
    proportion_single_with_kids_list_i = np.array(proportion_single_with_kids_list)
    proportion_married_no_kids_list_i = np.array(proportion_married_no_kids_list)
    proportion_married_with_kids_list_i = np.array(proportion_married_with_kids_list)
    proportion_students_list_i = np.array(proportion_students_list)
    proportion_cohabiting_list_i = np.array(proportion_cohabiting_list)
    
    # Add values
    num_houses_avg += num_houses_i
    population_avg += population_i
    
    Deaths_avg += Deaths_i
    Births_avg += Births_i
    Leaving_avg += Leaving_i
    Marriage_avg += Marriage_i
    Divorce_avg += Divorce_i
    Cohabits_avg += Cohabits_i
    
    avg_house_size_list_avg += avg_house_size_list_i
    avg_bedroom_house_size_list_avg += avg_bedroom_house_size_list_i
    
    proportion_one_avg += proportion_one_i
    proportion_two_avg += proportion_two_i
    proportion_three_avg += proportion_three_i
    proportion_four_avg += proportion_four_i
    proportion_five_avg += proportion_five_i
    proportion_six_avg += proportion_six_i
    proportion_seven_avg += proportion_seven_i
    proportion_eight_avg += proportion_eight_i
    
    proportion_one_beds_avg += proportion_one_beds_i
    proportion_two_beds_avg += proportion_two_beds_i
    proportion_three_beds_avg += proportion_three_beds_i
    proportion_four_beds_avg += proportion_four_beds_i
    proportion_five_beds_avg += proportion_five_beds_i
    proportion_six_beds_avg += proportion_six_beds_i
    proportion_seven_beds_avg += proportion_seven_beds_i
    proportion_eight_beds_avg += proportion_eight_beds_i
    
    proportion_single_only_list_avg += proportion_single_only_list_i
    proportion_single_with_kids_list_avg += proportion_single_with_kids_list_i
    proportion_married_no_kids_list_avg += proportion_married_no_kids_list_i
    proportion_married_with_kids_list_avg += proportion_married_with_kids_list_i
    proportion_students_list_avg += proportion_students_list_i
    proportion_cohabiting_list_avg += proportion_cohabiting_list_i
    
    # Add iterations to list
    population_iterations.append(population_i)
    num_houses_iterations.append(num_houses_i)
    avg_bedroom_house_size_list_iterations.append(avg_bedroom_house_size_list_i)
    avg_house_size_list_iterations.append(avg_house_size_list_i)
  
# Calculate averages
no_ones = no_ones/No_of_Sims
no_twos = no_twos/No_of_Sims
no_threes = no_threes/No_of_Sims
no_fours = no_fours/No_of_Sims
no_fives = no_fives/No_of_Sims
no_sixes = no_sixes/No_of_Sims
no_sevens = no_sevens/No_of_Sims
no_eights = no_eights/No_of_Sims

num_houses = num_houses_avg/No_of_Sims
population = population_avg/No_of_Sims

Deaths = np.round(Deaths_avg/No_of_Sims)
Births = np.round(Births_avg/No_of_Sims)
Leaving = np.round(Leaving_avg/No_of_Sims)
Marriage = np.round(Marriage_avg/No_of_Sims)
Divorce = np.round(Divorce_avg/No_of_Sims)
Cohabits = np.round(Cohabits_avg/No_of_Sims)

avg_house_size_list = avg_house_size_list_avg/No_of_Sims
avg_bedroom_house_size_list = avg_bedroom_house_size_list_avg/No_of_Sims

proportion_one = proportion_one_avg/No_of_Sims
proportion_two = proportion_two_avg/No_of_Sims
proportion_three = proportion_three_avg/No_of_Sims
proportion_four = proportion_four_avg/No_of_Sims
proportion_five = proportion_five_avg/No_of_Sims
proportion_six = proportion_six_avg/No_of_Sims
proportion_seven = proportion_seven_avg/No_of_Sims
proportion_eight = proportion_eight_avg/No_of_Sims

proportion_one_beds = proportion_one_beds_avg/No_of_Sims
proportion_two_beds = proportion_two_beds_avg/No_of_Sims
proportion_three_beds = proportion_three_beds_avg/No_of_Sims
proportion_four_beds = proportion_four_beds_avg/No_of_Sims
proportion_five_beds = proportion_five_beds_avg/No_of_Sims
proportion_six_beds = proportion_six_beds_avg/No_of_Sims
proportion_seven_beds = proportion_seven_beds_avg/No_of_Sims
proportion_eight_beds = proportion_eight_beds_avg/No_of_Sims

proportion_single_only_list = proportion_single_only_list_avg/No_of_Sims
proportion_single_with_kids_list = proportion_single_with_kids_list_avg/No_of_Sims
proportion_married_no_kids_list = proportion_married_no_kids_list_avg/No_of_Sims
proportion_married_with_kids_list = proportion_married_with_kids_list_avg/No_of_Sims
proportion_students_list = proportion_students_list_avg/No_of_Sims
proportion_cohabiting_list = proportion_cohabiting_list_avg/No_of_Sims

#%% Statistics

print('\n')
print(f'{Area_of_Interest} results:\n')

print(f'No of houses; 1 | {round(no_ones)}, 2 | {round(no_twos)}, 3 | {round(no_threes)}, 4 | {round(no_fours)}, 5 | {round(no_fives)}, 6 | {round(no_sixes)}, 7 | {round(no_sevens)}, 8+ | {round(no_eights)}')

print(f'Proportion of one person house: {round(no_ones/num_houses[-1] * 100,2)}%')
print(f'Proportion of two person house: {round(no_twos/num_houses[-1] * 100,2)}%')
print(f'Proportion of three person house: {round(no_threes/num_houses[-1] * 100,2)}%')
print(f'Proportion of four person house: {round(no_fours/num_houses[-1] * 100,2)}%')
print(f'Proportion of five person house: {round(no_fives/num_houses[-1] * 100,2)}%')
print(f'Proportion of six person house: {round(no_sixes/num_houses[-1] * 100,2)}%')
print(f'Proportion of seven person house: {round(no_sevens/num_houses[-1] * 100,2)}%')
print(f'Proportion of eight+ person house: {round(no_eights/num_houses[-1] * 100,2)}%')

x = np.array([['Place','One Person','Two People','Three People','Four People','Five People','Six People','Seven People','Eight People'], \
              [f'{Area_of_Interest}',round(no_ones/num_houses[-1] * 100,2),round(no_twos/num_houses[-1] * 100,2),round(no_threes/num_houses[-1] * 100,2),round(no_fours/num_houses[-1] * 100,2), \
                                       round(no_fives/num_houses[-1] * 100,2), round(no_sixes/num_houses[-1] * 100,2), round(no_sevens/num_houses[-1] * 100,2), round(no_eights/num_houses[-1] * 100,2)]])

df_proportions = pd.DataFrame(data=x[1:,1:], index=x[1:,0], columns=x[0,1:])
df_proportions.to_csv(f'Figures/{Area_of_Interest}/House_Size_Proportions.csv')

df_pop_houses = pd.DataFrame(list(zip(np.round(population), np.round(num_houses))), columns =['Population', 'Number of Houses'])
df_pop_houses.to_csv(f'Figures/{Area_of_Interest}/Population_Size_and_No_Houses.csv')

#%% Life Events

print('\n')
print('Deaths:', Deaths)
print('Births:',Births)
print('Leaving home:', Leaving)
print('Marriage', Marriage)
print('Divorce:', Divorce)
print('Cohabits:', Cohabits)

df_events = pd.DataFrame(list(zip(Deaths, Births, Leaving, Marriage, Divorce, Cohabits)), \
                         columns =['Deaths', 'Births', 'Leaving', 'Marriage', 'Divorce', 'Cohabits'])
    
df_events.to_csv(f'Figures/{Area_of_Interest}/Life_Events.csv')

#%% Set plot style

plt.style.use('ggplot')

#%% Initial pop graphs

# Creating labels for the bar chart and plotting it
household_types = ['Single Houses', 'Couples with Kids', 'Single with Kids', 'Couple Only', 'Students', 'Cohabiting']
fig1 = plt.figure(figsize=(8, 6))
bars = plt.bar(household_types, percentages)
plt.xlabel('Household Types')
plt.ylabel('Percentage of Population')
plt.title('Initial Percentage of Household Types')
plt.ylim(0, 100)  # y-axis limits from 0 to 100
plt.grid(axis='y', linestyle='--', alpha=0.7) #Alpha is transparency of grid lines
fig1.autofmt_xdate()
for i in range(6):
    bars[i].set_color(list(plt.rcParams['axes.prop_cycle'])[i]['color'])
plt.show()
fig1.savefig(f'Figures/{Area_of_Interest}/Initial_House_Type_Bars.png')

fig2 = plt.figure(figsize=(10, 6))
plt.plot(range(0, 101), age_percentages_array, color=list(plt.rcParams['axes.prop_cycle'])[0]['color'], alpha=0.7, label ='Model Age Distribution')
plt.plot(range(0, 101), Age_Distribution, color=list(plt.rcParams['axes.prop_cycle'])[1]['color'], alpha=0.7, label='Age Distribution')
plt.title('Percentage of People by Age')
plt.xlabel('Age')
plt.ylabel('Percentage')
plt.grid(True)
plt.legend()
plt.show()
fig2.savefig(f'Figures/{Area_of_Interest}/Initial_Prop_People_By_Age.png')

fig3 = plt.figure(figsize=(6, 6))
gender_labels = ['Male', 'Female']
bar_width = 0.35
index = np.arange(len(gender_labels))
plt.bar(index, gender_values, bar_width, color=list(plt.rcParams['axes.prop_cycle'])[1]['color'], label='Model Gender Distribution')
plt.bar(index + bar_width, Gender_Distribution, bar_width, color=list(plt.rcParams['axes.prop_cycle'])[2]['color'], label='Gender Distribution')
plt.xlabel('Gender')
plt.ylim(0, 60)
plt.ylabel('Percentage')
plt.title('Gender Distribution')
plt.xticks(index + bar_width / 2, gender_labels)
plt.legend()
plt.tight_layout()
plt.show()  
fig3.savefig(f'Figures/{Area_of_Interest}/Initial_Gender_Bars.png')

fig4 = plt.figure(figsize=(10, 6))
plt.plot(House_Sizes, proportions, marker='o', color=list(plt.rcParams['axes.prop_cycle'])[0]['color'], linestyle='-', label = 'Model Housing Size Distribution')
plt.plot(House_Sizes, Household_Size_Distribution, marker='o', color=list(plt.rcParams['axes.prop_cycle'])[1]['color'], alpha=0.7, label='Housing Size Distribution')
plt.title('Proportion of Household Sizes')
plt.xlabel('Household Size')
plt.ylabel('Percentage')
plt.xticks(House_Sizes)
plt.grid(True)
plt.legend()
plt.show()
fig4.savefig(f'Figures/{Area_of_Interest}/Initial_Prop_House_Size.png')

#%% House size - Residents - Line

fig5 = plt.figure(figsize=(10, 6))
plt.plot(years, proportion_one, label='1 Person')
plt.plot(years, proportion_two, label='2 People')
plt.plot(years, proportion_three, label='3 People')
plt.plot(years, proportion_four, label='4 People')
plt.plot(years, proportion_five, label='5 People')
plt.plot(years, proportion_six, label='6 People')
plt.plot(years, proportion_seven, label='7 People')
plt.plot(years, proportion_eight, label='8+ People')
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title('Proportion of Household Size by Number of Residents Over Time')
legend = plt.legend(loc = 'lower right',bbox_to_anchor=(1.2, 0),borderaxespad=0)
legend.set_title("Number of Residents")
legtitle = legend.get_title()
legtitle.set_fontweight("bold")
plt.grid(True)
fig5.savefig(f'Figures/{Area_of_Interest}/House_Size_Res_Line.png', bbox_inches='tight')

#%% House size - Residents - Pie

labels = '1 Person', '2 People', '3 People', '4 People', '5 People', '6 People', '7 People', '8+ People' 
sizes = [len(one), len(two), len(three), len(four), len(five), len(six), len(seven), len(eight)]
explode = (0, 0, 0, 0, 0, 0.2, 0.325, 0.45) 
fig6, ax = plt.subplots(figsize=(7,5))
pie = ax.pie(sizes, labels=labels, explode=explode, shadow=True, startangle=270, labeldistance=None, autopct='%1.1f%%')
for i in range(8):
    pie[2][i].set_fontsize(12)
plt.title('Proportion of Household Sizes by Residents', fontsize=20, x = 0.6)
plt.legend(loc = 'lower center', bbox_to_anchor=(1.1, 0.225), labelspacing = 1.1)
fig6.subplots_adjust(top=0.7)
fig6.tight_layout()
fig6.savefig(f'Figures/{Area_of_Interest}/House_Size_Res_Pie.png', bbox_inches='tight')

#%% House size - Bedrooms - Line

fig7 = plt.figure(figsize=(10, 6))
plt.plot(years, proportion_one_beds, label='1 Bedroom')
plt.plot(years, proportion_two_beds, label='2 Bedrooms')
plt.plot(years, proportion_three_beds, label='3 Bedrooms')
plt.plot(years, proportion_four_beds, label='4 Bedrooms')
plt.plot(years, proportion_five_beds, label='5 Bedrooms')
plt.plot(years, proportion_six_beds, label='6 Bedrooms')
plt.plot(years, proportion_seven_beds, label='7 Bedrooms')
plt.plot(years, proportion_eight_beds, label='8+ Bedrooms')
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title('Proportion of Household Size by Number of Bedrooms Over Time')
legend = plt.legend(loc = 'lower right',bbox_to_anchor=(1.2, 0),borderaxespad=0)
legend.set_title("Number of Bedrooms")
legtitle = legend.get_title()
legtitle.set_fontweight("bold")
legend._legend_box.align = "left"
plt.grid(True)
fig7.savefig(f'Figures/{Area_of_Interest}/House_Size_Bed_Line.png', bbox_inches='tight')

#%% House size - Bedrooms - Pie

labels = '1 Bedroom', '2 Bedrooms', '3 Bedrooms', '4 Bedrooms', '5 Bedrooms', '6 Bedrooms', '7 Bedrooms', '8+ Bedrooms' 
sizes = [len(one_bed), len(two_bed), len(three_bed), len(four_bed), len(five_bed), len(six_bed), len(seven_bed), len(eight_bed)]
explode = (0, 0, 0, 0, 0, 0.2, 0.325, 0.45) 
fig8, ax = plt.subplots(figsize=(7,5))
pie = ax.pie(sizes, labels=labels, explode=explode, shadow=True, startangle=270, labeldistance=None, autopct='%1.1f%%')
for i in range(8):
    pie[2][i].set_fontsize(12)
plt.title('Proportion of Household Sizes by Bedrooms', fontsize=20, x = 0.6)
plt.legend(loc = 'lower center', bbox_to_anchor=(1.1, 0.225), labelspacing = 1.1)
fig8.subplots_adjust(top=0.7)
fig8.tight_layout()
fig8.savefig(f'Figures/{Area_of_Interest}/House_Size_Bed_Pie.png', bbox_inches='tight')

#%% Avg house size - Bedroom - Line

fig9 = plt.figure(figsize=(10, 6))
plt.plot(years, avg_bedroom_house_size_list, label='Average Number of Bedrooms')
plt.xlabel('Years')
plt.ylabel('Number of Bedrooms')
plt.title('Average House Size by Number of Bedrooms Over Time')
legend = plt.legend()
legtext = legend.get_texts()
legtext[0].set_fontsize(12)
legtext[0].set_fontweight("bold")
plt.grid(True)
fig9.savefig(f'Figures/{Area_of_Interest}/Avg_House_Size_Bed_Line.png')

#%% Avg house size - Residents - Line

fig10 = plt.figure(figsize=(10, 6))
plt.plot(years, avg_house_size_list, label='Average Number of Residents')
plt.xlabel('Years')
plt.ylabel('Number of Residents')
plt.title('Average House Size by Number of Residents Over Time')
legend = plt.legend()
legtext = legend.get_texts()
legtext[0].set_fontsize(12)
legtext[0].set_fontweight("bold")
plt.grid(True)
fig10.savefig(f'Figures/{Area_of_Interest}/Avg_House_Size_Res_Line.png')

#%% Plotting proportion of each house type over time

fig11 = plt.figure(figsize=(10, 6))
plt.plot(np.array(years), proportion_single_only_list, label='Single Only')
plt.plot(np.array(years), proportion_single_with_kids_list, label='Single with Kids')
plt.plot(np.array(years), proportion_married_no_kids_list, label='Married, No Kids')
plt.plot(np.array(years), proportion_married_with_kids_list, label='Married with Kids')
plt.plot(np.array(years), proportion_students_list, label='Students')
plt.plot(np.array(years), proportion_cohabiting_list, label='Cohabiting')
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title('Proportion of Household Types Over Time')
legend = plt.legend(loc = 'lower right',bbox_to_anchor=(1.2, 0),borderaxespad=0)
legend.set_title("Household Type")
legtitle = legend.get_title()
legtitle.set_fontweight("bold")
legend._legend_box.align = "left"
plt.grid(True)
plt.show()
fig11.savefig(f'Figures/{Area_of_Interest}/Projected_House_Type_Line.png', bbox_inches='tight')

#%% House type - Bar

fig12 = plt.figure(figsize=(8, 6))
labels = ['Single Only', 'Single with Kids', 'Married, No Kids', 'Married, With Kids', 'Students', 'Cohabiting']
bar_width = [proportion_single_only_list[-1], proportion_single_with_kids_list[-1], proportion_married_no_kids_list[-1], proportion_married_with_kids_list[-1], proportion_students_list[-1], proportion_cohabiting_list[-1]]
bars = plt.bar(labels, bar_width)
plt.xlabel('Household Types')
plt.ylabel('Percentage of Population')
plt.title('Projected Percentage of Household Types')
plt.ylim(0, 100)  # y-axis limits from 0 to 100
plt.grid(axis='y', linestyle='--', alpha=0.7) #Alpha is transparency of grid lines
fig12.autofmt_xdate()
for i in range(6):
    bars[i].set_color(list(plt.rcParams['axes.prop_cycle'])[i]['color'])
fig12.savefig(f'Figures/{Area_of_Interest}/Projected_House_Type_Bar.png')

#%% Houses vs Population - Line - 2 Axis

fig13, ax1 = plt.subplots(1,1,figsize=(10,6))
plt.xlabel('Years')
ax1.plot(np.array(years), num_houses, label='Number of Houses', color=list(plt.rcParams['axes.prop_cycle'])[1]['color'])
plt.ylabel('Number of houses', color=list(plt.rcParams['axes.prop_cycle'])[1]['color'])
plt.tick_params(axis='y', labelcolor=list(plt.rcParams['axes.prop_cycle'])[1]['color'])
ax2 = ax1.twinx()
ax2.plot(np.array(years), population, label='Population', color=list(plt.rcParams['axes.prop_cycle'])[0]['color'])
plt.title('Population and Number of Houses Over Time')
plt.ylabel('Population size', color=list(plt.rcParams['axes.prop_cycle'])[0]['color'])
plt.tick_params(axis='y', labelcolor=list(plt.rcParams['axes.prop_cycle'])[0]['color'])
plt.grid(True)
legend = ax1.legend()
legtext = legend.get_texts()
legtext[0].set_fontsize(12)
legtext[0].set_fontweight("bold")
legend = ax2.legend(bbox_to_anchor=(0.926, 0.96))
legtext = legend.get_texts()
legtext[0].set_fontsize(12)
legtext[0].set_fontweight("bold")
plt.tight_layout()
plt.show()
fig13.savefig(f'Figures/{Area_of_Interest}/House_vs_Pop_Line_2_Axis.png')

#%% Houses vs Population - Line - 1 Axis

fig14 = plt.figure(figsize=(10, 6))
plt.plot(np.array(years), num_houses, label='Number of Houses', color=list(plt.rcParams['axes.prop_cycle'])[1]['color'])
plt.plot(np.array(years), population, label='Population', color=list(plt.rcParams['axes.prop_cycle'])[0]['color'])
plt.xlabel('Years')
plt.ylabel('Count')
plt.title('Population and Number of Houses Over Time')
legend = plt.legend()
legtext = legend.get_texts()
legtext[0].set_fontsize(12)
legtext[0].set_fontweight("bold")
legtext[1].set_fontsize(12)
legtext[1].set_fontweight("bold")
plt.grid(True)
plt.tight_layout()
plt.show()
fig14.savefig(f'Figures/{Area_of_Interest}/House_vs_Pop_Line_1_Axis.png')

#%% Average Graphs - Pop

fig15, ax15 = plt.subplots()
for i in range(No_of_Sims):
    ax15.plot(years,population_iterations[i], color = 'grey', lw = 0.75, label = 'Iterations')    
ax15.plot(years,population, lw = 4, label = 'Average Population Size')
plt.xlabel('Years')
plt.ylabel('Population size')
plt.title(f'Average Population Size Over Time: {No_of_Sims} Simulations')
handles, labels = ax15.get_legend_handles_labels()
display = (0,No_of_Sims)
legend = plt.legend([handle for i,handle in enumerate(handles) if i in display], [label for i,label in enumerate(labels) if i in display], loc = 'lower right')
legtext = legend.get_texts()
legtext[0].set_fontsize(11)
legtext[0].set_fontweight("bold")
legtext[1].set_fontsize(11)
legtext[1].set_fontweight("bold")
plt.show()
fig15.savefig(f'Figures/{Area_of_Interest}/Pop_Size_Iterations.png')

#%% Averge Graphs - House

fig16, ax16 = plt.subplots()
for i in range(No_of_Sims):
    ax16.plot(years,num_houses_iterations[i], color = 'grey', lw = 0.75, label = 'Iterations')    
ax16.plot(years,num_houses, lw = 4, label = 'Average Population Size')
plt.xlabel('Years')
plt.ylabel('Number of houses')
plt.title(f'Average Number of Houses Over Time: {No_of_Sims} Simulations')
handles, labels = ax16.get_legend_handles_labels()
display = (0,No_of_Sims)
legend = plt.legend([handle for i,handle in enumerate(handles) if i in display], [label for i,label in enumerate(labels) if i in display], loc = 'lower right')
legtext = legend.get_texts()
legtext[0].set_fontsize(11)
legtext[0].set_fontweight("bold")
legtext[1].set_fontsize(11)
legtext[1].set_fontweight("bold")
plt.show()
fig16.savefig(f'Figures/{Area_of_Interest}/House_Size_Iterations.png')

#%% Average Graphs - House

#%% Average Graphs - Avg House Bedroom size

fig17, ax17 = plt.subplots(figsize = (12,6))
for i in range(No_of_Sims):
    ax17.plot(years,avg_bedroom_house_size_list_iterations[i], color = 'grey', lw = 0.75, label = 'Iterations')  
ax17.plot(years,avg_bedroom_house_size_list, lw = 4, label = 'Average Number of Bedrooms')
plt.xlabel('Years')
plt.ylabel('Number of Bedrooms')
plt.title(f'Average House Size by Number of Bedrooms Over Time: {No_of_Sims} Simulations', fontsize = 14)
handles, labels = ax17.get_legend_handles_labels()
display = (0,No_of_Sims)
legend = plt.legend([handle for i,handle in enumerate(handles) if i in display], [label for i,label in enumerate(labels) if i in display], loc = 'lower left')
legtext = legend.get_texts()
legtext[0].set_fontsize(11)
legtext[0].set_fontweight("bold")
legtext[1].set_fontsize(11)
legtext[1].set_fontweight("bold")
plt.show()
fig17.savefig(f'Figures/{Area_of_Interest}/Avg_Bedroom_House_Size_Iterations.png')

#%% Average Graphs - Avg House Resident size

fig18, ax18 = plt.subplots(figsize = (12,6))
for i in range(No_of_Sims):
    ax18.plot(years,avg_house_size_list_iterations[i], color = 'grey', lw = 0.75, label = 'Iterations')  
ax18.plot(years,avg_house_size_list, lw = 4, label = 'Average Number of Residents')
plt.xlabel('Years')
plt.ylabel('Number of Residents')
plt.title(f'Average House Size by Number of Residents Over Time: {No_of_Sims} Simulations', fontsize = 14)
handles, labels = ax18.get_legend_handles_labels()
display = (0,No_of_Sims)
legend = plt.legend([handle for i,handle in enumerate(handles) if i in display], [label for i,label in enumerate(labels) if i in display], loc = 'lower left')
legtext = legend.get_texts()
legtext[0].set_fontsize(11)
legtext[0].set_fontweight("bold")
legtext[1].set_fontsize(11)
legtext[1].set_fontweight("bold")
plt.show()
fig18.savefig(f'Figures/{Area_of_Interest}/Avg_House_Size_Iterations.png')
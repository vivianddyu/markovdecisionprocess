"""
Created on Wed Nov 18 2021
Markov Decision Process
@author: Vivian_Yu
"""
# Instructions from Prof
# Make sure it's easy to
# 1) change the initial plane capacity (say a 75-seat plane instead of 100), and/or
# 2) change the prices for each of the 15 days, and/or
# 3) change the avg demand for each of the 15 days.

# Import packages
import pandas as pd


# Parameter settings
capacity = 100
ndays = 15
probs = 1/3


# Read Data
df = pd.read_excel('Solution Output.xlsx', sheet_name= 'Input')


# Define functions
# days_remaining ranges from 1 to ndays (15)
# seats_remaining ranges from 1 to capacity (100)
def action(days_remaining, seats_remaining):
    mean_demand = df['Demand mean'][ndays - days_remaining]
    price = df['Price'][ndays - days_remaining]
    demand_lst = [mean_demand-1, mean_demand, mean_demand+1]

    t_value = [] #value at current time = days_remaining
    t_action = [] #action (sell how many tickets) at current time = days_remaining
    for current_d in demand_lst:
        # print(current_d)
        loop_q = min(current_d, seats_remaining)
        action_value = []
        for i in range(loop_q + 1):
            current_value = i * price
            remaining_value = ex_action(days_remaining - 1, seats_remaining - i)  # 還沒寫好 #demand = loop_q+1-i
            # print('c', current_value)
            # print('r', remaining_value)
            action_value.append(current_value + remaining_value)
        max_value = max(action_value)  # value of selling max_action at this stage
        # print(max_value)
        max_action = action_value.index(max_value)  # sell this quantity at this stage
        # print(max_action)
        t_value.append(max_value)
        t_action.append(max_action)

    return t_value, t_action

def ex_action(days_remaining, seats_remaining):
    if days_remaining == 0 or seats_remaining == 0:
        t1_value = 0
    else:
        t1_value = ans_list1[days_remaining-1][seats_remaining-1][0]*probs + ans_list1[days_remaining-1][seats_remaining-1][1]*probs + ans_list1[days_remaining-1][seats_remaining-1][2]*probs
        # print(t1_value)
    return t1_value


# Get value and action for each demand, store to ans_list1 and ans_list2 respectively
ans_list1 = []
ans_list2 = []
for j in range(1, ndays+1): # days
    temp_list1 = []
    temp_list2 = []
    for i in range(1, capacity+1): # capacity
        # print('this is loop', i)
        value_temp, action_temp = action(j,i)
        temp_list1.append(value_temp)
        temp_list2.append(action_temp)
    ans_list1.append(temp_list1)
    ans_list2.append(temp_list2)

# print(ans_list1)
# print(ans_list2)

# Retrieve mean demand value and action, store to ans_list3 and ans_list4 respectively
ans_list3 = []
ans_list4 = []
for j in range(1, ndays+1): # days
    temp_list3 = []
    temp_list4 = []
    for i in range(1, capacity+1): # capacity
        meand_value = ans_list1[j-1][i-1][1]
        meand_action = ans_list2[j-1][i-1][1]
        temp_list3.append(meand_value)
        temp_list4.append(meand_action)
    ans_list3.append(temp_list3)
    ans_list4.append(temp_list4)


# Export to Excel
df2 = pd.DataFrame(ans_list3)
df3 = pd.DataFrame(ans_list4)
# For output purpose, change indexing
df2.index += 1
df3.index += 1

with pd.ExcelWriter('vvn_output.xlsx') as writer:
    df2.to_excel(writer, sheet_name='value', header = [i for i in range(1, capacity+1)], index_label='days remaining/ seats available')
    df3.to_excel(writer, sheet_name='action', header = [i for i in range(1, capacity+1)], index_label='days remaining/ seats available')
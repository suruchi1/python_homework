import os
import csv
import numpy as np

csvpath = '../Resources/budget_data.csv'

total_months = 0
sum = 0
total_net = 0
month_of_change =[]
net_change_list = []
greatest_increase = []
greatest_decrease = []
profit_loss = []
differences_list = []


with open(csvpath, newline='') as handler:
	csvreader = csv.reader(handler, delimiter=",")

	head = next(csvreader)

	for row in csvreader:
		#track total
		total_months = total_months + 1
		total_net = total_net + int(row[1])
		profit_loss.append(int(row[1]))
	print(total_months)
	print(total_net)
	print(profit_loss)

	for i in range(1,len(profit_loss)):

		difference = profit_loss[i] - profit_loss[i-1]
		differences_list.append(float(difference))


	print(differences_list)
	print(np.mean(differences_list))
	print(np.max(differences_list))
	print(np.min(differences_list))

	greatest_increase = np.max(differences_list)
	greatest_decrease = np.min(differences_list)

		








		# total_net = total_net + int(row[1])
		# #track the net change
		# net_change = int(row[1]) - prev_net
		# prev_net = int(row[1])
		# net_change_list = net_change_list + [net_change]
		# month_of_change = month_of_change + [row[0]]

		#calculating greatest increase/decrease
		# if net_change > greatest_increase[1]:
		# 	greatest_increase[0] = row[0]
		# 	greatest_increase[1] = net_change


		# #calculating greatest decrease
		# if net_change < greatest_decrease[1]:
		# 	greatest_decrease[0] = row[0]
		# 	greatest_decrease[1] = net_change


		# net_monthly_average = sum(net_change_list)/len(net_change_list)


		


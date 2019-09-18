import os
import csv
import numpy as np

csvpath = '../Resources/election_data.csv'

total_votes = 0
voter = []
voteFor = []


with open(csvpath, newline='') as handler:
	csvreader = csv.reader(handler, delimiter=",")


	head = next(csvreader)

	for row in csvreader:

		total_votes= total_votes + 1

		print(total_votes)
		

	


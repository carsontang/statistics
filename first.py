"""This file contains code that answers the questions in Allen B. Downey's book, Think Stats.
"""

import survey
table = survey.Pregnancies()
table.ReadRecords()
print "Number of pregnancies:", len(table.records)

# 1) Count the number of live births
# 2) Split live births into first babies and other babies
# 3) For live births, count total pregnancy lengths (in weeks)
# 4) Count number of babies with low birth weights
first_babies_num = 0
other_babies_num = 0

first_low = 0
other_low = 0
first_babies_total_prglength = 0
other_babies_total_prglength = 0
for record in table.records:
	if record.outcome == 1:																# outcome == 1 signifies live birth
		if record.birthord == 1:														# birthord == 1 signifies the baby was the family's first
			first_babies_num += 1
			first_babies_total_prglength += record.prglength
			if record.lbw1 == 1:
				first_low += 1
		else:
			other_babies_num += 1
			other_babies_total_prglength += record.prglength
			if record.lbw1 == 1:
				other_low += 1

# Counts can be verified with data at http://www.icpsr.umich.edu/nsfg6/Controller	
print "Number of live births:", first_babies_num + other_babies_num	
print "Number of first babies:", first_babies_num
print "Number of other babies:", other_babies_num

print "# of first babies with low weight to total # of first babies:", first_low*1.0/first_babies_num
print "# of other babies with low weight to total # of other babies:", other_low*1.0/other_babies_num

# Compute average pregnancy length (in weeks) for first babies
print "Average pregnancy length (in weeks) for first babies:", first_babies_total_prglength*1.0/first_babies_num

# Compute average pregnancy length (in weeks) for other babies
print "Average pregnancy length (in weeks) for other babies:", other_babies_total_prglength*1.0/other_babies_num
"""This file contains code that answers the questions in Allen B. Downey's book, Think Stats.
"""

import survey
table = survey.Pregnancies()
table.ReadRecords()
print "Number of pregnancies:", len(table.records)

# 1) Count the number of live births
# 2) Split live births into first babies and other babies
# 3) For live births, count total pregnancy lengths (in weeks)
first_babies = []
other_babies = []
first_babies_total_prglength = 0
other_babies_total_prglength = 0
for record in table.records:
	if record.outcome == 1:																# outcome == 1 signifies live birth
		if record.birthord == 1:														# birthord == 1 signifies the baby was the family's first
			first_babies.append(record)
			first_babies_total_prglength += record.prglength
		else:
			other_babies.append(record)
			other_babies_total_prglength += record.prglength

# Counts can be verified with data at http://www.icpsr.umich.edu/nsfg6/Controller	
print "Number of live births:", len(first_babies) + len(other_babies)	
print "Number of first babies:", len(first_babies)
print "Number of other babies:", len(other_babies)

# Compute average pregnancy length (in weeks) for first babies
print "Average pregnancy length (in weeks) for first babies:", first_babies_total_prglength*1.0/len(first_babies)

# Compute average pregnancy length (in weeks) for other babies
print "Average pregnancy length (in weeks) for other babies:", other_babies_total_prglength*1.0/len(other_babies)
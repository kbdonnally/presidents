# presidents.py

import csv
with open('presidents.csv', newline='') as csvfile:
	pres_reader = csv.reader(csvfile)

	# resets seek to 0, then goes one after that
	# this skips the fieldnames
	csvfile.seek(0)
	next(csvfile)

	# names of presidents
	names = [line[0] for line in pres_reader]
	
	# reset where it's seeking, skip fieldname
	csvfile.seek(0)
	next(csvfile)

	# number of president
	numbers = [line[1] for line in pres_reader]

	csvfile.seek(0)
	next(csvfile)

	# political parties, separated by comma if >1
	parties = [line[2] for line in pres_reader]

	csvfile.seek(0)
	next(csvfile)

	# elections they won
	winning_elections = [line[3] for line in pres_reader]
	
	csvfile.seek(0)
	next(csvfile)

	# date entered office
	served_from = [line[4] for line in pres_reader]
	
	csvfile.seek(0)
	next(csvfile)

	# date left office
	served_until = [line[5] for line in pres_reader]

	csvfile.seek(0)
	next(csvfile)

	# vice presidents
	vps = [line[6] for line in pres_reader]

	csvfile.seek(0)
	next(csvfile)

	# age at inauguration
	ages = [line[7] for line in pres_reader]

	csvfile.seek(0)
	next(csvfile)

	# portrait filenames
	img_names = [line[8] for line in pres_reader]

	csvfile.seek(0)
	next(csvfile)

	# notable achievements
	achievements = [line[9] for line in pres_reader]

	'''
	YAML:

	- name: {name}
	  number: {number}
	  party: {party}
	  winning_elections: {elections}
	  age: {age}
	  vp: {vp}
	  served_from: {date}
	  served_to: {date}
	  img_name: {img}
	  achievements: {achievements}
	'''
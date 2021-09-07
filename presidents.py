# presidents.py

import csv
with open('presidents.csv', newline='') as csvfile:
	pres_reader = csv.reader(csvfile)

	# resets seek to 0, then goes one after that
	# this skips the fieldnames
	csvfile.seek(0)
	next(csvfile)

	names = 			[]
	numbers = 			[]
	parties = 			[]
	winning_elections = []
	served_from = 		[]
	served_until = 		[]
	vps = 				[]
	ages = 				[]
	img_names = 		[]
	achievements = 		[]

	for line in pres_reader:
		for index, item in enumerate(line):
			if index == 0:
				names.append(item)
			if index == 1:
				numbers.append(item)
			if index == 2:
				item = item.split(",")
				parties.append(item)
			if index == 3: 
				item = item.split(",")
				winning_elections.append(item)
			if index == 4:
				served_from.append(item)
			if index == 5:
				served_until.append(item)
			if index == 6:
				item = item.split(",")
				vps.append(item)
			if index == 7:
				ages.append(item)
			if index == 8:
				img_names.append(item)
			if index == 9:
				item = item.split('\n')
				achievements.append(item)

presidents = [names, numbers, parties, winning_elections, served_from, served_until, vps, ages, img_names, achievements]

i = 0
while i <= 45:
	entry = f'- name: {names[i]}\n  number: {numbers[i]}\n  parties:  {parties[i]}\n  winning_elections: {winning_elections[i]}\n  served_from: {served_from[i]}\n  served_until: {served_until[i]}\n  vps: {vps[i]}\n  age: {ages[i]}\n  achievements: {achievements[i]}'
	i = i + 1
	print(entry)

test = ['hello', 'goodbye', 'what']

#for item in test:
#	"- " + item)


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
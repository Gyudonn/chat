lines = []

with open('3.txt', encoding = 'utf-8-sig') as file:
	for line in file:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(time + ' ' + name)
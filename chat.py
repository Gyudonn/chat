def read_file(filename):
	tmp_lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as file:
		for line in file:
			tmp_lines.append(line.strip())
	return tmp_lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			preson = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as file:
		for line in lines:
			file.write(line + '\n')

def main():
	lines = read_file('input.txt')
	new_lines = convert(lines)
	write_file('output.txt', new_lines)

main()
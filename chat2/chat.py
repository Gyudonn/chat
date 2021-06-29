

def read_file(filename):
	tmp_lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as file:
		for line in file:
			tmp_lines.append(line.strip())
	return tmp_lines


def convert(lines):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen says: ' + str(allen_word_count) + ', used: ' + str(allen_sticker_count) + ', send: ' + str(allen_image_count))
	print('Viki says :' + str(viki_word_count) + ', used: ' + str(viki_sticker_count) + ', send: ' + str(viki_image_count))


def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as file:
		for line in lines:
			file.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	new_lines = convert(lines)
	#write_file('output.txt', new_lines)

main()
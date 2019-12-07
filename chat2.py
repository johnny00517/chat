def read_file(filename):
	lines = []
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	allen_words_count = 0
	viki_words_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_picture_count = 0
	viki_picture_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for m in s[2:]:
					allen_words_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for m in s[2:]:
					viki_words_count += len(m)

	print('Allen共講了:', allen_words_count, '個字')
	print('Vicky共講了:', viki_words_count, '個字')
	print('Allen共傳了:', allen_sticker_count, '個貼圖')
	print('Vicky共傳了:', viki_sticker_count, '個貼圖')
	print('Allen共傳了:', allen_picture_count, '個圖片')
	print('Vicky共傳了:', viki_picture_count, '個圖片')


	

# def write_file(filename, lines):
# 	with open (filename, 'w', encoding='utf-8-sig') as f:
# 		for line in lines:
# 			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()
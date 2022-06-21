"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""

	"""
	all_alpha = []
	all_alpha += '      '
	for i in range(4):
		all_alpha += ' '
		row = input(str(i + 1) + ' row of letters: ')
		if len(row) > 7:
			print('Illegal Input')
			exit()
		for j in range(len(row)):
			if row[j] != ' ':
				all_alpha += row[j]
		all_alpha += ' '
	all_alpha += '      '

	possible_word = ''
	search(all_alpha, possible_word)
	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search(all_alpha, possible_word):
	count = 0
	dic = read_dictionary()
	for i in range(len(all_alpha)):
		exist_index = []
		if all_alpha[i] == ' ':
			pass
		else:
			search_2(i, all_alpha, possible_word, count, dic, exist_index)


def search_2(i, all_alpha, possible_word, count, dic, exist_index):
	exist_index.append(i)
	if possible_word in dic and len(possible_word) >= 4:
		print('Found: ' + possible_word)
		count += 1
	else:
		if all_alpha[i - 7] != ' ' and (i - 7) not in exist_index:
			possible_word += all_alpha[i - 7]
			i = i - 7
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i - 6] != ' ' and (i - 6) not in exist_index:
			possible_word += all_alpha[i - 6]
			i = i - 6
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i - 5] != ' ' and (i - 5) not in exist_index:
			possible_word += all_alpha[i - 5]
			i = i - 5
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i - 1] != ' ' and (i - 1) not in exist_index:
			possible_word += all_alpha[i - 1]
			i = i - 1
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i + 1] != ' ' and (i + 1) not in exist_index:
			possible_word += all_alpha[i + 1]
			i = i + 1
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i + 5] != ' ' and (i + 5) not in exist_index:
			possible_word += all_alpha[i + 5]
			i = i + 5
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i + 6] != ' ' and (i + 6) not in exist_index:
			possible_word += all_alpha[i + 6]
			i = i + 6
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()
		if all_alpha[i + 7] != ' ' and (i + 7) not in exist_index:
			possible_word += all_alpha[i + 7]
			i = i + 7
			search_2(i, all_alpha, possible_word, count, dic, exist_index)
			possible_word = possible_word[:-1]
			exist_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d = []
	with open(FILE, 'r') as f:
		for line in f:
			d.append(line.strip('\n'))
	return d


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	d = read_dictionary()
	for word in d:
		return word.startswith(sub_s)


if __name__ == '__main__':
	main()

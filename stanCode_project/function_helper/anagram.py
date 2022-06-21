"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'   # Controls when to stop the loop



def main():
    word_dictionary = read_dictionary()
    """
    TODO:
    """

    print('Welcome to stanCode "Anagram generator"(or -1 to quit)')
    s = str((input('find anagrams for: ')))
    start = time.time()
    while s != EXIT:
        print('Search...')
        ans = find_anagrams(s)
        print(str(len(ans)) + ' anagrams: ' + str(ans))
        ####################
        #                  #
        #       TODO:      #
        #                  #
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        s = str((input('find anagrams for: ')))




def read_dictionary():
    d = []
    with open(FILE, 'r') as f:
        for line in f:
            d.append(line.strip('\n'))
    return d


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    ans = ''
    ans_list = []
    control = 0
    find_anagrams_help(s, ans, ans_list)
    return ans_list


def find_anagrams_help(s, ans, ans_list):
    word_dictionary = read_dictionary()
    if len(ans) == len(s):
        if ans in word_dictionary:
            print('Found: ' + ans)
            ans_list.append(ans)
            print('Search...')
    else:
        for alpha in s:
            if alpha not in ans:
                ans += alpha
                has_prefix(ans)
                if True:
                    find_anagrams_help(s, ans, ans_list)
                    ans = ans[:-1]
    return ans_list






def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    d = read_dictionary()
    for word in d:
        return word.startswith(sub_s)










if __name__ == '__main__':
    main()

"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('tbody')
        for tag in tags:
            number = tag.text
            numbers = number.split()
            male_total = 0
            female_total = 0
            control = 5
            for i in range(2, len(numbers)-2):
                if control / 5 == 1:
                    if ',' in str(numbers[i]):
                        male_total += int(numbers[i].split(',')[0]+numbers[i].split(',')[1])
                        female_total += int(numbers[i+2].split(',')[0] + numbers[i+2].split(',')[1])
                        control = 1
                    else:
                        break
                else:
                    control += 1
            print(male_total)
            print(female_total)













if __name__ == '__main__':
    main()

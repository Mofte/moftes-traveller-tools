#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markovify

divider = "\n" + "-"*48 + "\n"
annoyance_counter = 0

with open('plothooks-in.txt') as f:
    data = f.read()
data_model = markovify.Text(data)

print(divider)

print('A simple sci-fi plothook generator!')

print(divider)

print('''This script is very basic.
It takes 660 writing prompts \'stolen\' from a blog post on servicescape.com and squeezes them through markovify.
You'll be then presented a randomly generated sentence which can be saved into a TXT or HTML file.
For more information go to https://github.com/mofte/moftes-traveller-tools.

markovify: https://pypi.org/project/markovify/
the blog post: https://www.servicescape.com/blog/660-science-fiction-writing-prompts-that-will-get-you-writing-at-warp-speed''')

print(divider)

while True:
    try:
        readme = input('''Show readme?
y/n? - ''')
        readme_valid = ('y', 'n', 'Y', 'N')
        if readme in readme_valid:
            break
        print('\n')
    except:
        print('Just enter y or n!')
        continue

print(divider)

if readme == 'y' or readme == 'Y':
    print('''Just follow these steps:
1. Select the filtype, TXT or HTML.
2. Enter how many sentences you want to generate.
3. The specified number of sentences will be randomly generated and presented.
   After each one you can save it into the file plothooks.txt/html.
4. Either start a new \'round\' or exit the script.\n''')
    input('Enter anything to continue - ')
elif readme == 'n' or readme == 'N':
    print('Fine, let\'s go!')

print(divider)

while True:
    try:
        filetype = input('''Output as TXT or HTML?
1 -> TXT
2 -> HTML
Your input: ''')
        if filetype == '1' or filetype == '2':
            break
        else:
            print('\n')
    except:
        print('Just enter 1 or 2!')
        continue

print(divider)

while True:
    try:
        amount = input('''How many sentenced should be generated?
Your input: ''')
        amount = int(amount)
        break
    except:
        if annoyance_counter < 5:
            print('\nJust enter a number...\n')
            annoyance_counter += 1
            continue
        elif annoyance_counter < 10:
            print('\nYou just want to be stupid, right?!\n')
            annoyance_counter += 1
            continue
        elif annoyance_counter == 10:
            print('\nI warn you! You got one last chance...\n')
            annoyance_counter += 1
            continue
        elif annoyance_counter > 10:
            while True:
                print('(┛◉Д◉)┛彡┻━┻' * 5)

running = 'y'

while running == 'y':
    while amount > 0:
        try:
            for i in range(1):
                sentence = data_model.make_sentence()
                print(divider)
                print('  ' + sentence)
                print(divider)
            save = input('''Save sentence?
y/n - ''')
            if save == 'y' or save == 'n':
                amount -= 1
                if save == 'y':
                    if filetype == '1':
                        g = open('plothooks.txt', 'a+')
                        g.write(sentence + '\n')
                        g.close()
                    elif filetype == '2':
                        g = open('plothooks.html', 'a+')
                        g.write('<p>' + sentence + '</p>\n')
                        g.close()
                elif save == 'n':
                    continue
        except:
            print('Just enter y or n!')
            continue
    while True:
        try:
            amount = input('''Do you want more?

Just enter the number of sentences to be generated. Enter 0 to exit.
Your input: ''')
            amount = int(amount)
            if amount > 0:
                break
            elif amount == 0:
                running = 'n'
                break
        except:
            print('I don\'t know what\'s happening...')
            running = 'n'
            break

print(divider)

print('Thanks for using this script. Hope to see you next time around!')

print(divider)
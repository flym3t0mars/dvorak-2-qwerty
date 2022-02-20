#! /bin/python
import sys
from os import system as s
from time import sleep as zz

# I want to simulate the press with these ascii character
# also redraw the keyboard with the key pressed
# but refresh the page without losing the message typed
# real time key press

qwerty = ['q','w','e','r','t','y','u','i','o','p','[',']','\\',
	   'a','s','d','f','g','h','j','k','l',';',"'",
	    'z','x','c','v','b','n','m',',','.','/',' ',
		'\n'
	 ]
dvorak = ["'",',','.','p','y','f','g','c','r','l','/','=','\\',
	   'a','o','e','u','i','d','h','t','n','s','-',
	    ';','q','j','k','x','b','m','w','v','z',' ',
		'\n'
	 ]

qw="""
[q][w][e][r][t][y][u][i][o][p][[][]][\]
 [a][s][d][f][g][h][j][k][l][;][']
  [z][x][c][v][b][n][m][,][.][/]
       [                 ]
"""

pres = '■'
timing=0.15

def oskb():
	with open('tt.md','r')as r:
		keyboard=r.readlines()
		for lines in keyboard:
			if "#" in lines:
				pass
			else:
				print(lines,end='')

def clear():
	try:
		if sys.platform != 'linux':
			s('cls')
		else:
			s('clear')
	except Exception as e:
		print(e)
	else:
		pass

def file(b='null'):
	if b == 'null':
		print(f'file provided: {b}')
		exit()
	else:
		print(f'file provided: {b}')
		with open (b,'r')as r:
			content = r.read()
			print(content,end='')
	print('='*8+'\n')
	for key in content.lower():
		index=dvorak.index(key)
		print(qwerty[index],end='')

def qw2dv(a):
	global ss
	ss=input('type message: ')
	try:
		if a == 'qw':
			for key in ss.lower():
				index=qwerty.index(key)
				print(dvorak[index],end='')
		elif a == 'dv':
			for key in ss.lower():
				index=dvorak.index(key)
				print(qwerty[index],end='')
		print('\n')
	except Exception as e:
		print(e)
	else:
		exit()


def pressed(msg='null'):
	opt()
	while True:
		for keys in msg:
			if keys == ' ':
                                print(choice.replace('[                 ]',' [               ]'))
                                zz(timing)
                                clear()
			else:
				print(choice.replace(keys,pres))
				zz(timing)
				clear()

def opt():
	global choice
	choice=input('qw or dv: ')
	if choice == 'qw':
		pass
#		qw2dv(choice)
	elif choice == 'dv':
		pass
#		qw2dv(choice)
	else:
		print('enter one of the choices (qw / dv):\n')
		opt()
	return choice

def ask(q):
	question = input(f'{q} (y/n): ')
	if question == 'y':
		pressed(input('type: '))
	elif question == 'n':
		ask2 = input(f'do you want to use a file (y/n): ')
		if ask2 == 'y':
			file()
		if ask2 == 'n':
			ask3 = input('do you want to type without animation (y/n): ')
			if ask3 == 'y':
				opt()
				qw2dv(choice)
			if ask3 == 'n':
				exit()
	else:
		pass


def main():
	ask('do you want to type with animation')


if __name__ == "__main__":
	main()

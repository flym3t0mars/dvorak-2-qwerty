#! /bin/python
import sys
from os import system as s
from time import sleep as zz

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

# I want to simulate the press with these ascii character
# also redraw the keyboard with the key pressed
# but refresh the page without losing the message typed
# real time key press


pressed = '■'

def oskb():
	with open('tt.md','r')as r:
		keyboard=r.readlines()
		for lines in keyboard:
			if "#" in lines:
				pass
			else:
				print(lines,end='')
		

		# print(keyboard)

def pressed(msg='null'):
	while True:
		oskb()
		zz(0.01)
		clear()
	


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
		exit()
	else:
		with open (b,'r')as r:
			content = r.read()
			print(content,end='')
	print('='*8)
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
def opt():
	choice=input('qw or dv: ')
	if choice == 'qw':
		qw2dv(choice)
	elif choice == 'dv':
		#dv2qw()
		qw2dv(choice)
	else:
		print('enter one of the choices (qw / dv):\n')
		opt()

def main():
#	oskb()
	pressed()
	ask=input('do you want to use a file (y/n): ')
	if ask == 'y':
		file(sys.argv[1])
	elif ask == 'n':
		opt()
	else:
		pass

if __name__ == "__main__":
	main()

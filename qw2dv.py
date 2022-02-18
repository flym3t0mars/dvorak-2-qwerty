#! /bin/python
import sys

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
	ask=input('do you want to use a file: ')
	if ask == 'no'
		opt()
	else:
		file(sys.argv[1])

if __name__ == "__main__":
	main()

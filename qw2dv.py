#! /bin/python

qwerty = ['q','w','e','r','t','y','u','i','o','p','[',']','\\',
	   'a','s','d','f','g','h','j','k','l',';',"'",
	    'z','x','c','v','b','n','m',',','.','/',' '
	 ]
dvorak = ["'",',','.','p','y','f','g','c','r','l','/','=','\\',
	   'a','o','e','u','i','d','h','t','n','s','-',
	    ';','q','j','k','x','b','m','w','v','z',' '
	 ]

def dv2qw():
	global s
	s=input('type: message:')
	try:
		for key in s:
			index=dvorak.index(key)
			print(qwerty[index],end='')
		print('\n')
	except Exception as e:
		print(e)
	else:
		exit()

def qw2dv():
	global ss
	ss=input('type message: ')
	try:
		for key in ss:
			index=qwerty.index(key)
			print(dvorak[index],end='')
		print('\n')
	except Exception as e:
		print(e)
	else:
		exit()

def main():
	choice=input('qw or dv: ')
	if choice == 'qw':
		qw2dv()
	else:
		dv2qw()

if __name__ == "__main__":
	main()

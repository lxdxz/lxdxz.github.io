oo = [123,124,125,126,111]
passwd = 123456
passwd_b = 12345678
passwd_c = 666666
a = input('enter passcode:')
if int(a) == passwd :
	print('login successfully')
	a_b = input('enter second passcode:')
	if int(a_b) == passwd_b :
		print('successful get in')
		l = 1
		while l == 1:
			w = input('~$China CopperCoin Army:')
			if not w == 'admin' :
				print(w,'~bash command not found')
			if w == 'admin' :
				e_p = input('enter admin passcode:')
				if int(e_p) == passwd_c :
					while l == 1 :
						do = input('what to do:')
						if do == 'append()' :
							ask = input('which')
							oo.append(int(ask))
				if not int(e_p) == passwd_c :
					print('warning!unexpeted enter!')
if int(a) != passwd :
	print('warning!unexpeted enter!')
	print('gocha')
	

user = input('user')
port = input('port')
ip = input('ip')
input('use ssh connect?[yes/no]')
password = 'alpine'
print('user:',user,'port:',port,'ip:',ip)
a = input('This the first connection.Are you sure to connect?[yes/no]')
if a == 'yes':
    passwd = input('passwd:')
    if passwd == password:
        l = 1
        while int(l) == 1:
            w = input('~$xiaolideqizhongyibuaifengx:')
            if  w != 'passwd' or 'python':
                print(w,'~bash command not found')
            if w == 'passwd':
                for e in range(5):
                    e = input('enter old password')
                    if not int(e) == password:
                        print('permission denied')
                    if int(e) == password:
                        y = input('new password')
                        uu = input('are you sure?[yes/no]')
                        if uu == 'yes':
                            print('Done')
                            while l == 1:
                                w = input('~$xiaolideqizhongyibuaifengx:')
                                print(w,'$bash command not found')
            if w == 'python':
                while l == 1:
                    t = input('>>')
                    if t == 'print()':
                        print('')
                    if t == 'exit()':
                        while l == 1:
                            w = input('~$xiaolideqizhongyibuaifengx:')
                            print(w,'$bash command not found')

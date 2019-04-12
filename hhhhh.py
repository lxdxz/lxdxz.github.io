import itchat
itchat.auto_login()#会有二维码出来，扫二维码
users=itchat.search_friends(name=u'wm')#可以是备注名字，也可以是昵称
userName=users[0]['UserName']
i = 1
for x in range(100):
    itchat.send(u'hahahaha',userName)

# itchat目前不能登录，腾讯已经做了限制
import itchat

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
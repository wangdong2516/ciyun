import itchat
import jieba
import imageio
import wordcloud


# 进行微信登录
# itchat.login()

signature_list = []

# 获取微信好友列表
# friends = itchat.get_friends(update=True)
#
# # 提取每个好友的个性签名
# for friend in friends:
#     signature = friend['signature']
#
#     # 对表情不做处理
#     if 'emoji' in signature:
#         pass
#     else:
#         signature_list.append(signature)
#
# # 拼接所有的签名
# text = ' '.join(signature_list)
f = open('../intro.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

# 进行分词处理
text_list = jieba.lcut(content, cut_all=True)

content = ' '.join(text_list)

# 读取图片，作为词云的形状
mask = imageio.imread('person.png')

# 创建词云对象
word = wordcloud.WordCloud(
    background_color='white', height=100, width=100, collocations=False,
    mask=mask, prefer_horizontal=0.2, scale=5, font_path='simsun.ttf',
    contour_color='black', contour_width=2
)

word.generate(content)

# nickname = friends[0]['NickName']
# filename = "output11-{}的微信好友个性签名词云图.png".format(nickname)
word.to_file('last.png')
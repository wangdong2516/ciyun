"""制作词云"""

import wordcloud

# 创建词云对象
word = wordcloud.WordCloud(
    width=500, height=500, prefer_horizontal=0.2,
    min_font_size=2, scale=2, max_words=200, stopwords=['One', 'night'],
    mode='RGBA', background_color=None
)

# 传入需要制作词云的文本
word.generate('this is my house, i am leborn james One day,we donlt have to say goodoye,just say good night.')

# 将生成的词云保存为图片，保存路径在当前目录的文件夹下
image = word.to_image()
image.save('ss.png')

# 图像颜色生成器
# image_generator = wordcloud.ImageColorGenerator()

# 随机颜色，色相生成器
wordcloud.random_color_func()

# 创建一个颜色函数，该函数返回单个色调和饱和度
color_func1 = wordcloud.get_single_color_func('deepskyblue')
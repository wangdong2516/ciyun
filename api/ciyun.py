"""制作词云"""

import wordcloud
import imageio
import jieba
import matplotlib.pyplot as plt


# 指定词云形状的图片,imread函数，并用这个函数读取本地图片，作为词云形状图片
mask = imageio.imread('person.png')

# 打开外部文件并且读取
f = open('../intro.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

# 创建词云对象,这里如果文本是中文的话，需要下载中文字体文件
# 如果需要去掉重复出现的单词，可以指定collocations参数，该参数表示是否需要包含两个词的组合
word = wordcloud.WordCloud(
    width=1000, height=700, background_color='black',
    font_path='simsun.ttf', prefer_horizontal=0.2,
    mask=mask, scale=2, collocations=False,
    contour_color='black', contour_width=2
)

# 提取背景图片的颜色
image_color = wordcloud.ImageColorGenerator(image=mask)

# 加入jieba分词
content_list = jieba.lcut(content)
content = ' '.join(content_list)
# 传入需要制作词云的文本
word.generate(content)


# 显示原生词云图、按模板图片颜色的词云图和模板图片，按左、中、右显示
fig, axes = plt.subplots(1, 3)
# 最左边的图片显示原生词云图
axes[0].imshow(word)
# 中间的图片显示按模板图片颜色生成的词云图，采用双线性插值的方法显示颜色
axes[1].imshow(word.recolor(color_func=image_color), interpolation="bilinear")
# 右边的图片显示模板图片
axes[2].imshow(mask, cmap=plt.cm.gray)
for ax in axes:
    ax.set_axis_off()
plt.show()
wc_color = word.recolor(color_func=image_color)

word.to_file('wordcloud.png')
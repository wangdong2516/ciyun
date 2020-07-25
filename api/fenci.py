"""中文分词组件"""
import sys

import jieba
import jieba.posseg as pseg
import jieba.analyse
from optparse import OptionParser

# 开启paddle模式
jieba.enable_paddle()
str_list = ['我来自北京', '我是一名程序员', '我从事python开发']
for str in str_list:
    # seg = jieba.cut(str, cut_all=True)  # 使用全模式
    # seg = jieba.cut(str, use_paddle=True)   # 使用paddle模式
    # seg = jieba.cut(str)  # 使用精确模式，默认的
    # seg = jieba.cut(str, HMM=True)  # 使用HMM模型
    seg = jieba.cut_for_search(str)  # 使用搜索引擎模式，默认使用HMM模型
    print(list(seg))

# 加载自定义的词典
jieba.load_userdict('../custom_dict.txt')

# 在运行的过程中，添加新词到字典中
jieba.add_word('石墨烯')
jieba.add_word('正確應該不會被切開')
jieba.del_word('自定义词')

test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)

words = jieba.cut(test_sent)
print(list(words))

print("=" * 40)

result = pseg.cut(test_sent)
for i in result:
    print(i.word, "/", i.flag, ", ", end=' ')

print("\n" + "=" * 40)

terms = jieba.cut('easy_install is great')
print('/'.join(terms))
terms = jieba.cut('python 的正则表达式是好用的')
print('/'.join(terms))

print("=" * 40)
# test frequency tune
testlist = [
    ('今天天气不错', ('今天', '天气')),
    ('如果放到post中将出错。', ('中', '将')),
    ('我们中出了一个叛徒', ('中', '出')),
]

# for sent, seg in testlist:
#     print('/'.join(jieba.cut(sent, HMM=False)))
#     word = ''.join(seg)
#     print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
#     print('/'.join(jieba.cut(sent, HMM=False)))
#     print("-"*40)

print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True)
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('/'.join(jieba.cut('「台订单」正确应该不会被切开', HMM=False)))
jieba.suggest_freq('台订单', True)
print('/'.join(jieba.cut('「台订单」正确应该不会被切开', HMM=False)))

# 关键词提取
# # USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
# # parser = OptionParser(USAGE)
# # parser.add_option("-k", dest="topK")
# # opt, args = parser.parse_args()
# # if len(args) < 1:
# #     print(USAGE)
# #     sys.exit(1)
# #
# # file_name = args[0]
# #
# # if opt.topK is None:
# #     topK = 10
# # else:
# #     topK = int(opt.topK)
#
# content = open('../a.txt', 'rb').read()
#
# tags = jieba.analyse.extract_tags(content, topK=20)
#
# print(",".join(tags))

# 自定义语料库
# content = open('../a.txt', 'rb').read()
# jieba.analyse.set_idf_path("../idf.txt.big")
# tags = jieba.analyse.extract_tags(content, topK=20)

# 自定义停止词文本语料库
content = open('../a.txt', 'rb').read()
jieba.analyse.set_idf_path("../idf.txt.big")
jieba.analyse.set_stop_words("../stop_words.txt")
tags = jieba.analyse.extract_tags(content, topK=20)

print(",".join(tags))

# 自定义停止词文本语料库
withWeight = True
content = open('../a.txt', 'rb').read()
jieba.analyse.set_idf_path("../idf.txt.big")
jieba.analyse.set_stop_words("../stop_words.txt")
tags = jieba.analyse.extract_tags(content, topK=20, withWeight=withWeight)
if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
else:
    print(",".join(tags))

# 基于TextRank算法的关键词抽取
s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

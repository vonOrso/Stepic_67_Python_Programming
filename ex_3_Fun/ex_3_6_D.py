import requests

# 1
# r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/811.txt')
# print(len(r.text.splitlines()))

# 2
# r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
# print(r.text)

# 3
# st = ''
# text = '699991.txt'
# while st != 'We':
#     text = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+text).text
#     st = text[0]+text[1]
#     print(text)

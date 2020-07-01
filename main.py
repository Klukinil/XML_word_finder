import xml.etree.ElementTree as ET
def word_finder(xml_file,word_length, top):
  parser = ET.XMLParser(encoding="utf-8")
  tree = ET.parse(xml_file, parser)
  root = tree.getroot()
  items_list2 = root.findall("channel/item/description")
  text = []
  for description in items_list2:
    text.append(description.text)
  words_list = []
  for news in text:
    words_list.append(news.split())
  words = words_list[0]
  for i in range(1, len(words_list)):
    words += words_list[i]
    i +=1
  long_words = []
  for word in words:
    if len(word) >= 6:
      long_words.append(word)
  long_words.sort()
  words_count = dict()
  for  long_word in long_words:
    words_count[long_word] = long_words.count(long_word)
  value_count = []
  for value in words_count.values():
    value_count.append(value)
  value_count.sort(reverse=True)
  top_value = value_count[0:10]
  top_word = dict()
  for key,value in words_count.items():
    if value in top_value:
      top_word[key] = value
  print(top_word)

word_finder("newsafr.xml", 6, 10)
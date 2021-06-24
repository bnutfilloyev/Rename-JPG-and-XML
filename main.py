import os

nameList = os.listdir('/Users/yoshlikmedia/PycharmProjects/TextToXml/path/images')
xmlList = os.listdir('/Users/yoshlikmedia/PycharmProjects/TextToXml/path/xmls')
# print(xmlList)
name_list = []
xml_list = []


#
# for i in nameList:
#     for j in xmlList:
#         if i[:-4] == j[:-4]:
#             name_list.append(i)
#             xml_list.append(j)
count = 0
#
# for i in nameList:
#     if i not in name_list:
#         os.remove(f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/images/{i}')
#
# for i in xmlList:
#     if i not in xml_list:
#         # os.remove(f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/xmls/{i}')
#         count += 1
#         print(i)

print(count)
print(len(name_list))
print(xmlList)

print(name_list, xml_list)
print(nameList)
count = 5000
for i in nameList:
    count += 1
    print(f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/to/{i[:-4]}.xml', f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/to/head_image_000{count}.xml')
    try:
        os.rename(f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/to/{i[:-4]}.xml', f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/to/head_image_000{count}.xml')
        os.rename(f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/brainwash_10_27_2014_images/{i}', f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/brainwash_10_27_2014_images/head_image_000{count}.jpg')
    except:
        os.remove(f'/Users/yoshlikmedia/PycharmProjects/TextToXml/path/brainwash_10_27_2014_images/{i}')

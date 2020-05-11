import requests
import os
from pprint import pprint

Url = '这个是分析后书籍的KM地址&page={}'
FileName = "移动端图像处理白皮书v1.0"
PageCount = 103

def downloadPage():
    for x in range(1,PageCount+1):
        r = requests.get(Url.format(x))
        with open("{}/{}.jpeg".format(FileName, x), 'wb') as file:
            file.write(r.content)

def makeMarkdown():
	with open("{}/{}.md".format(FileName, FileName), 'w') as file:
		for x in range(1,PageCount+1):
			file.write("![]({}.jpeg)\n".format(x));

if __name__ == "__main__":
    os.mkdir(FileName)
    downloadPage()
    makeMarkdown();
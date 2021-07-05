import re

train = open("./train.src.clean.txt","w",encoding='utf8')
with open("./train.src.txt","r",encoding='utf8') as f:
    for line in f.readlines():
        line = re.sub(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})|"
                      r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})|"
                      r"(\d{4}-\d{1,2}-\d{1,2})|"
                      r"(\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})|"
                      r"\(.+?\)|"
                      r"（.+?）|"
                      r"【字体：】|"
                      r"显示图片{.*}|"
                      r"{.*}|"
                      r"显示图片|"
                      r"您的浏览器不支持video标签。|"
                      r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
                      , "", line)
        train.write(line.strip()+"\n")
train.close()

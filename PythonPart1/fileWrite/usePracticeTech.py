f = open(
    "C:/PythoneWorkspace/PythonPart1/fileWrite/KakaoTalkChats.txt",
    "r",
    encoding="utf-8",
)

wordcount={}

for i, line in enumerate(f.readlines()):
    # if line.startswith("2019"):
    #     break
    msg = None
    if i > 4:
        line = line.replace("\n", "")

        if not line.startswith("20") and (line != ""):
            msg = line

        else:
            try:
                line = line.split(" : ")
                msg = line[1]
                for ii, word in enumerate(line):
                    if ii > 1:
                        msg += " " + word
            except:
                pass
        if msg != None:
            msg = msg.strip().split(" ")
            for word in msg:
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1



print(wordcount)


f.close()

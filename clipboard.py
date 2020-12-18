import pyperclip
import re

clipboard = pyperclip.paste()

file = open('clipboard.txt', 'a')
file.write('<clipboarditem>\n' + clipboard + '\n</clipboarditem>\n')
file.close()


with open("clipboard.txt", encoding="utf-8") as file:
    #x = [re.search('<item>(.*)</item>', file) for s in file]
    #x = [s for s in file]
    #print(x);

    counter = 0;
    clipboardItem = []
    inRecordingMode = False
    for line in file:
        if not inRecordingMode:
            if line.startswith('<clipboarditem>'):
                inRecordingMode = True
        elif line.startswith('</clipboarditem>'):
            counter = counter + 1
            inRecordingMode = False
        else:
            #yield line
            # TODO: 
            clipboardItem[counter] = clipboardItem[counter] + line
            #clipboardItem.append(line)

    #print(clipboardItem);
    file = open('clipboard-result.txt', 'w')
    for item in clipboardItem:
        file.write(item)
    file.close()

userName = str.capitalize(str.strip(input('what is your name? ')))

saveFileDoc = open(r"C:\Users\gjriv\Downloads\Python\My Codes\Text files\TicTacToeSaveFiles.txt" , "r+")
fileLines = saveFileDoc.read()

textList = fileLines.split()

if userName in textList:
    print('welcome back ' + userName)
    textList[textList.index(userName) + 1] = str(int(textList[textList.index(userName) + 1]) + 1)
    print('you have visited ' + textList[textList.index(userName) + 1] + ' times')
    newSave = ' '.join(textList)
    saveFileDoc.seek(0)
    saveFileDoc.write(newSave)
    saveFileDoc.close()
else:
    print('f')
    saveFileDoc.close()

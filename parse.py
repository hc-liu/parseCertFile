import sys
import os

# open cert file
fileContent = open(sys.argv[1], 'r').read()
startPos = fileContent.find("-----BEGIN")
if startPos >= 0:
    newString = fileContent[startPos+10:]
    startPos = newString.find("-----")
    if startPos > 0:
        newString = newString[startPos+6:]
        endPos = newString.find("-----")
        if endPos > 0:
            newString = newString[:endPos]
            newString = newString.replace('\r\n', '')
            newString = newString.replace('\n', '')
            print newString
            os.system('fw_setenv cloud_cert ' + newString)

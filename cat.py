
with open('command.fort.13', 'wb') as outFile:
	with open ('command.info', 'rb') as com, open('fort.13', 'rb') as fort13:
		outFile.write(com.read())
		outFile.write(fort13.read())



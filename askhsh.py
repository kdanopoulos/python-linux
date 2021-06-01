
def superSales(filename):
	fp = open(curFile, "r");
	dictionary = {}
	supermarkets = []
	for line in fp: 
		line = line.split(" ")
		line[2] = float(line[2])
		alreadyExists = 0
		for curSuper in supermarkets: # run all savings to find if the supermaket input already exists or not
			if(curSuper==line[1]): # add the extra value to the old supermarket
				alreadyExists = 1
				dictionary[curSuper]+=line[2]
				break
		if(alreadyExists==0):	# add the new supermarket	 
			dictionary[line[1]] = line[2]
			supermarkets.append(line[1])
	myMax = 0
	bestKey = ''
	for key, value in dictionary.items():
		if(value>myMax):
			myMax = value
			bestKey = key

	print(filename+" "+bestKey+" "+str(myMax))
	fp.close()		




files =  input("Please give the name of the files for processing:  ")
myList = files.split(" ")
for curFile in myList:
	if(curFile!=""):
		#print(curFile)
		superSales(curFile)
		

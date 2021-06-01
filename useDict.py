fp = open("inputTeams", "r")
dictionary_spot_1 = {}
dictionary_spot_2 = {}
labs = []
for line in fp:             #create dictionaries from file
	line =line.split("\n")
	line = line[0] 
	#print(line)
	line = line.split(" ")
	print(line)
	labs.append(line[0])
	if(len(line)==3):
		dictionary_spot_1[line[0]]=line[1]
		dictionary_spot_2[line[0]]=line[2]
	else:
		dictionary_spot_1[line[0]]=line[1]
		dictionary_spot_2[line[0]]='empty'

user_option=0
while(user_option!=5):
	print(len(labs))
	print("----------------Menu----------------")
	print("1. Combine Teams")
	print("2. Print Teams")
	print("3. Search a specific Team")
	print("4. Search a specific student")
	print("5. Exit")
	print("------------------------------------")
	user_option = int(input("What would you like to do? :"))
	if(user_option==1):
		found_one=-1
		index=0
		for curLab in labs:
			if(dictionary_spot_2[curLab]=='empty'):
				if(found_one!=-1): # we have found another empty spot at the lab at possition = found_one
					dictionary_spot_2[found_one] = dictionary_spot_1[curLab]
					#delete lab[i] at labs and at the dictionaries
					dictionary_spot_1.pop(curLab, None)
					dictionary_spot_2.pop(curLab, None)
					labs.pop(index)
					found_one=-1
				else: # this is the first empty spot and we store the possition of the lab with the empty spot
					found_one = curLab
			index+=1
	elif(user_option==2):
		temp =''
		for cur in labs:
			print(cur)
			temp+=(cur+"\n")
			#also print them in a file	
		f = open("outputTeams", "w")
		f.write(temp)	
		f.close()	
	elif(user_option==3):
		wantedLab = input("Please give the lab that you want to Search for: ")
		found=0
		for cur in range(len(labs)):
			if(wantedLab==labs[cur]):
				found=1
				print("The lab "+wantedLab+" has been found. The member/s of this lab is/are :"+dictionary_spot_1[labs[cur]]+", "+dictionary_spot_2[labs[cur]])
				break
		if(found==0):
			print("The lab "+wantedLab+" does not exist")
	elif(user_option==4):
		wantedStudent = input("Please give the AM of the student that you want to Search for: ")
		found=0
		for cur in labs:
			if(dictionary_spot_1[cur]==wantedStudent):
				found=1
				print("The student with AM: "+wantedStudent+" is at the lab "+cur)
				break
			elif(dictionary_spot_2[cur]==wantedStudent):
				found=1
				print("The student with AM: "+wantedStudent+" is at the lab "+cur)
				break
		if(found==0):
			print("The student with AM: "+wantedStudent+" does not exist")
	elif(user_option==5):
		print("Thank you for using our application.")
	else:
		print("Invalid option. Please choose again.")

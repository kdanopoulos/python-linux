import random
import urllib.request as urllib2

def printWordFound(word):
	for i in word:
		print(i,end="")
	print("\n",end="")

#f = open("http://norvig.com/ngrams/sowpods.txt .", "r")
#print(f.read())
myList=[]
data = urllib2.urlopen("http://norvig.com/ngrams/sowpods.txt")
for i in data:
	cur = str(i).split("'")
	cur = cur[1]
	cur = cur[:-2]
	myList.append(cur)
	length = len(myList)


user_input=1
while(user_input==1):
	word_len=0
	while(word_len<5):   # run until find a random word with more than 5 letters
		ran = random.randint(0, length-1)
		cur_word = myList[ran]
		word_len = len(cur_word)

	print("Welcome to Hangman!")  # the game starts
	word_found = []
	for i in range(word_len):
		word_found.append("_")

	incorrect_letters =''
	while(len(incorrect_letters)<6):
		found=0
		printWordFound(word_found)
		print("Incorrect letters:"+incorrect_letters)


		new_input_true=1
		while(new_input_true):
			new_input = input("Guess your letter: ")
			new_input_true=0
			for pp in incorrect_letters:
				if(new_input==pp):
					print("You have already picked that letter. Try again.")
					new_input_true=1
									
		for k in range(word_len):    # run all the word from finding matching letters with the input of the user
			currentLetter = cur_word[k]
			if(currentLetter==new_input):
				found=1
				word_found[k]=new_input

		if(found):
			print("Correct!")
		else:
			print("Incorrect!")
			incorrect_letters+=new_input	

		won=1
		for mm in word_found:
			if(mm=="_"):
				won=0
		if(won):
			print("Winner!!! You found the word!!!")
	if(won==0):
		print("You lost the game!")
		print("The word was :"+cur_word)


		
		

	anwser = input("Do you want to play again? (Y/y or N/n): ");
	if(anwser=='Y' or anwser=='y'):
		user_input=1
	else:
		user_input=2
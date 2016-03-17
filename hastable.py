def getHint(secret, guss):

	total = 0
	bull = 0
	for i in range(0, len(secret)):
		if secret[i] == guess[i]:
			bull = bull + 1
	hashtable = {}
	for i in range(0, len(secret)):
		if secret[i] in hashtable:
			hashtable[secret[i]] += 1
		else:
			hashtable[secret[i]] = 1
	print hashtable
	for i in range(0, len(guess)):
		if guess[i] in hashtable:
			total = total + 1
			hashtable[guess[i]] -= 1
			if hashtable[guess[i]] == 0:
				del hashtable[guess[i]]
	print hashtable
	cow = total - bull

	return str(bull)+'A'+str(cow)+'B'

secret = "1234"
guess = "0111"

print getHint(secret, guess)

#program-4: word shuffling
sentence = "Gujrat vidyapith is great college"
word1 = sentence[0:6]
word2 = sentence[7:17]
word3 = sentence[17:19]
word4 = sentence[20:25]
word5 = sentence[26:33]

print("possible sentences is given below:")
print("*********************************************************************")
print(word3,word4,word2,word1,word5)
print(word2,word1,word3,word5,word4)
print(word1,word3,word5,word2,word4)
print(word4,word2,word1,word3,word4)
print(word5,word3,word4,word2,word1)
#--------------------------------------------------------------------------
# Global Variables definition
#--------------------------------------------------------------------------
#!/usr/bin/env python
tags = ['NN', 'NST', 'PRP', 'DEM', 'VM', 'JJ', 'RP', 'RB', 'CC', 'WQ', 'QF', 'NUM', 'NEG', 'SYM', 'PSP','COMP','UT', 'ECH', 'UNK']


		
#max_connect function performs the viterbi decoding. Choosing which tag
#for the current word leads to a better tag sequence. 

import stop
def max_connect(x, y, viterbi_matrix, emission, transmission_matrix):
	max = -99999
	path = -1
	
	for k in xrange(len(tags)):
		val = viterbi_matrix[k][x-1] * transmission_matrix[k][y]
		#print(val)
		if val * emission > max:
			max = val
			path = k
	return max, path

# from flask import Flask,render_template
# import entity
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("entity_input.php")
# if __name__ == "__main__":
#     app.run(debug=True)	


def main():

	#--------------------------------------------------------------------------
	# Start of Training Phase
	#--------------------------------------------------------------------------
	
	start_time = time.time()

	# Path of training files
	filepath = ["./data/kannada_training.txt"]
	languages = ["kannada"]
	exclude = ["<s>", "</s>", "START", "END"]
	wordtypes = []
	tagscount = []
	b=""

	# Open training file to read the contents
	f = codecs.open("./data/kannada_training.txt", 'r', encoding='utf-8')
	file_contents = f.readlines()
	#print(type(file_contents))

	a=str(file_contents)
	#print(type(a))

	# list=[':',',','?','.','"','\'','(',')','[',']','!','@','#','$','%','^','&','*','+','-','=','/']
	# for i in list:
	# 	a=a.replace(i,'')

	#print(a)	

	#file_contents=list(a.split(" "))
	#print(type(file_contents))


	# Initialize count of each tag to Zero's
	for x in xrange(len(tags)):
		tagscount.append(0)

	# Calculate count of each tag in the training corpus and also the wordtypes in the corpus
	for x in xrange(len(file_contents)):
		line = file_contents.pop(0).strip().split(' ')
		for i, word in enumerate(line):
			if i == 0:
				if word not in wordtypes and word not in exclude:
					wordtypes.append(word)
			else:
				if word in tags and word not in exclude:
					tagscount[tags.index(word)] += 1
	#print(tagscount)
	#print(wordtypes) 				
	f.close()
	
	# Declare variables for emission and transmission matrix	
	emission_matrix = []
	transmission_matrix = []
		
	# Initialize emission matrix
	for x in xrange(len(tags)):
		emission_matrix.append([])
		for y in xrange(len(wordtypes)):
			emission_matrix[x].append(0)
	#print(emission_matrix)		

	# Initialize transmission matrix
	for x in xrange(len(tags)):
		transmission_matrix.append([])
		for y in xrange(len(tags)):
			transmission_matrix[x].append(0)
	#print(transmission_matrix)

	# Open training file to update emission and transmission matrix
	f = codecs.open("./data/kannada_training.txt", 'r', encoding='utf-8')
	file_contents = f.readlines()

	# b=str(file_contents)
	
	# list=[':',',','?','.','"','\'','(',')','[',']','!','@','#','$','%','^','&','*','+','-','=','/']
	# for i in list:
	# 	b=b.replace(i,'')

	# Update emission and transmission matrix with appropriate counts
	row_id = -1
	for x in xrange(len(file_contents)):
		line = file_contents.pop(0).strip().split(' ')
		#print(line[0])
		#print(line[1])
		
		if line[0] not in exclude:
			col_id = wordtypes.index(line[0])
			#print(col_id)
			prev_row_id = row_id
			#print(prev_row_id)
			row_id = tags.index(line[1])
			#print(row_id)
			emission_matrix[row_id][col_id] += 1
			#print(emission_matrix)
			if prev_row_id != -1:
				transmission_matrix[prev_row_id][row_id] += 1
		else:
			row_id = -1

	#print(emission_matrix)
	#print(transmission_matrix)		
	
	# Divide each entry in emission matrix by appropriate tag count to store probabilities in each entry instead of just count
	for x in xrange(len(tags)):
		for y in xrange(len(wordtypes)):
			if tagscount[x] != 0:
				emission_matrix[x][y] = float(emission_matrix[x][y]) / tagscount[x]
	#print(emission_matrix)			

	# Divide each entry in transmission matrix by appropriate tag count to store probabilities in each entry instead of just count
	for x in xrange(len(tags)):
		for y in xrange(len(tags)):
			if tagscount[x] != 0:
				transmission_matrix[x][y] = float(transmission_matrix[x][y]) / tagscount[x]
	#print(transmission_matrix)		

	#print time.time() - start_time, "seconds for training"


	start_time = time.time()

	# Open the testing file to read test sentences
	testpath = ["./data/kannada_testing.txt"]
	file_test = codecs.open("./data/kannada_testing.txt", 'r', encoding='utf-8')
	test_input = file_test.readlines()

	
	
	# Declare variables for test words and pos tags
	test_words = []
	pos_tags = []

	# Create an output file to write the output tags for each sentences
	file_output = codecs.open("./output/kannada_tags.txt", 'w', 'utf-8')
	file_output.close()

	# For each line POS tags are computed
	for j in xrange(len(test_input)):
		
		test_words = []
		pos_tags = []

		line = test_input.pop(0).strip().split(' ')
		#print(line)
		
		for word in line:
			test_words.append(word)
			pos_tags.append(-1)
		#print(test_words)
		#print(pos_tags)	

		viterbi_matrix = []
		viterbi_path = []
		
		# Initialize viterbi matrix of size |tags| * |no of words in test sentence|
		for x in xrange(len(tags)):
			viterbi_matrix.append([])
			viterbi_path.append([])
			for y in xrange(len(test_words)):
				viterbi_matrix[x].append(0)
				viterbi_path[x].append(0)

		#print(viterbi_matrix)
		#print(viterbi_path)	

		# Update viterbi matrix column wise
		for x in xrange(len(test_words)):
			for y in xrange(len(tags)):
				if test_words[x] in wordtypes:
					word_index = wordtypes.index(test_words[x])
					#print(word_index)
					tag_index = tags.index(tags[y])
					#print(tag_index)
					emission = emission_matrix[tag_index][word_index]
					#print(emission)

				elif test_words[x][:-1] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-1])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]	

				elif test_words[x][:-2] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-2])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]	

				elif test_words[x][:-3] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-3])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]	

				elif test_words[x][:-4] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-4])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-5] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-5])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-6] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-6])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-7] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-7])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-8] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-8])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-9] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-9])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-10] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-10])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-11] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-11])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-12] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-12])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]

				elif test_words[x][:-13] in wordtypes:
					word_index = wordtypes.index(test_words[x][:-13])
					tag_index = tags.index(tags[y])
					emission = emission_matrix[tag_index][word_index]																						
				else:
				
					emission = 0.5

				if x > 0:
					max, viterbi_path[y][x] = max_connect(x, y, viterbi_matrix, emission, transmission_matrix)
				else:
					max = 1
				viterbi_matrix[y][x] = emission * max

                

		# Identify the max probability in last column i.e. best tag for last word in test sentence
		maxval = -999999
		maxs = -1
		for x in xrange(len(tags)):
			if viterbi_matrix[x][len(test_words)-1] > maxval:
				maxval = viterbi_matrix[x][len(test_words)-1]
				maxs = x
			
		# Backtrack and identify best tags for each words
		for x in range(len(test_words)-1, -1, -1):
			pos_tags[x] = maxs
			maxs = viterbi_path[maxs][x]

		# Display POS Tags in the console.
		# print pos_tags
		
		# Print output to the file.	
		file_output = codecs.open("./output/kannada_tags.txt", 'a', 'utf-8')
		for i, x in enumerate(pos_tags):
			file_output.write("\n" + test_words[i] + " " + tags[x])
		file_output.write("\n"+"*")	

	f.close()
	file_output.close()
	file_test.close()

	#print time.time() - start_time, "testing dataset"
	print("Executed")
	
	print "Check ./output/kannada_tags.txt file for POS tags."


#If all the libraries are available in target system, main() is called, 
#else program exits gracefully by displaying dependancies.

if __name__ == "__main__":
	try:
		import codecs
		import os
		import sys
		import time

		
		# if len(sys.argv) == 3:
		main()
		# else:
		# 	print "Usage: python entity.py <language> <test_file_path>"
		# 	print "Example: python supervised.py 0 ./data/kannada_testing.txt"
			

	except ImportError as error:
		print "Couldn't find the module - {0}, kindly install before proceeding.".format(error.message[16:])

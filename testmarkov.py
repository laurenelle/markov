import random
from sys import argv

script, fileinput = argv

opened = open(fileinput)

read_txt = opened.read()

txt = read_txt.lower()

word_list = txt.split()

input_length = len(word_list)

word_dict = {}

index = 0
word_list_length = len(word_list)

for index, word in enumerate(word_list):
    if index < word_list_length - 2:
        first_word = word_list[index]
        tuple_first_word = tuple([first_word])
        second_word = word_list[index + 1]
        tuple_second_word = tuple([second_word])
        third_word = word_list[index + 2]

        #create each word pair using the index of the list
        # word_pair = first_word + ", "+ second_word
        word_pair = tuple_first_word + tuple_second_word
        final_word_pair = word_pair
        #create a tuple out of the word_pair 
        # final_word_pair = tuple([word_pair])
        if final_word_pair in word_dict:
            word_dict[final_word_pair].append(third_word)
        else:
            # add [] to third_word each value becomes a list and can be expanded
            word_dict[final_word_pair] = [third_word]







final_output_list = []
random_tuple = random.choice(word_dict.keys())
final_output_list.append(random_tuple[0])
final_output_list.append(random_tuple[1])

# index, words in enumerate(final_output_list)
output_length = len(final_output_list)

while output_length < 100:
    last_tuple = final_output_list[-2:]

    last_tuple = tuple(last_tuple)

    # make a tuple not a list
    # third_word = word_dict[last_tuple]
    # print third_word



    random_third_word = random.choice(word_dict[last_tuple])
    final_output_list.append(random_third_word)
    output_length = len(final_output_list)
    # if tuple doesn't have a value then continue
    if third_word == None:
        continue


print final_output_list

# print final_output_list

 

    # keys function
    # len of list
    # list function
    # use append
    # choose key randomly by enumerating list
    # for index, list_value in enumerate(key_list):

    #     randint(beginning, end)
    #randomly choose a key and then pick one of the values from the key

    #use the chosen key as the beginning of the word pair and find a word pair 

    #start the process over again
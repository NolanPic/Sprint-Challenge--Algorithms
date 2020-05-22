'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case--if the word has no length, return
    if len(word) < 2:
        return 0
    
    # count if the next two letters are th
    count = 0
    if word[0] == 't' and word[1] == 'h':
        count = 1
    
    # if the count went up, skip the cut off
    # the first two letters
    if count == 1:
        word = word[2:]
    # if the count did not go up, cut off the 
    # the next letter
    else:
        word = word[1:]
    return count + count_th(word)

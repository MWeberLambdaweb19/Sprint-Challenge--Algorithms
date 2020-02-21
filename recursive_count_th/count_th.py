'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    a = 0
    count = 0
    if len(word) <= 1:
        return count
    elif len(word) == 0:
        return count
    else: 
        if word[a] + word[a+1] == 'th':
            count += 1
            a += 1
            word = word[a:]
            return count_th(word)
        else:
            a += 1
            word = word[a:]
            return count_th(word)
    # elif word[a] + word[a+1] == 'th':
    #     print('HIT TRUE')
    #     count += 1
    #     a += 1
    #     word = word[a:]
    #     count_th(word)
    # else:
    #     print('HIT FALSE')
    #     a += 1
    #     word = word[a:]
    #     count_th(word)
    # print(count)
    return count

count_th('thoughtful')
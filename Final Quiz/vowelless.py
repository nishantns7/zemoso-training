def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''

    vowels=['a','e','i','o','u','A','E','I','O','U']
    s1=""
    for i in s:
        if i not in vowels:
            s1+=i
    print(s1)

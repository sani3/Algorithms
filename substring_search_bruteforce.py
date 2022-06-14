def search(text, pattern):
    j = 0
    i = 0
    while i < len(text):
        if text[i] == pattern[j]:
            if j != len(pattern) - 1:
                i += 1
                j += 1
                continue
            else:
                return i - j, text[i - j: i+1]
        if j != 0:
            i -= j - 1
            j = 0
            continue
        i += 1
    return -1


if __name__ != 'main':
    search("stolen as they sleep", "colen")  # -1
    search("stolen as they sleep", "stole")  # (0, 'stole')
    search("stolen as they sleep", "stolen")  # (0, 'stolen')
    search("stolen as they sleep", "olen")  # (2, 'olen')
    search("stolen as they sleep", "as")  # (7, 'as')
    search("stolen as they sleep", "them")  # -1
    search("stolen as they sleep", "hey")  # (11, 'hey')
    search("stolen as they sleep", "sleep")  # (15, 'sleep')
    search("stolen as they sleep", "eep")  # (17, 'eep')
    search("stolen as they sleep", "pot")  # -1
    search("sabam", "sam")  # -1
    search("sasam", "sam")  # (2, 'sam')
    search("mesomesomo", "mesomo")  # (4, 'mesomo')

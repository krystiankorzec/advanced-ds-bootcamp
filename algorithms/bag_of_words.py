def build_bag_of_words(s):
    word_counts = {}
    punctuation = ',.:-_"'
    tab = str.maketrans("","", punctuation)
    s = s.translate(tab).lower()
    for word in s.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

s = "Charon is processing emails. Emails are processed fast, really fast."
print(build_bag_of_words(s))
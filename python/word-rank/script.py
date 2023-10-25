from time import perf_counter

# coding=utf-8
# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

# Good luck! You can write all the code in this file.

set_time = perf_counter()

words = []
for i in sentences:
    one_word = i.replace(',', '').replace('.', '')
    words.extend(one_word.lower().split())

words.sort()

# Firstly we get rid of all comas and periods
# Then we create list of all words from sentences, lowered and splitted by space
# Finally list is sorted alphabetically

print('POSITION \t WORD \t - \t NUMBER OF REPETITIONS')

for i in range(3):

    count = list(map(lambda x: words.count(x), words))
    repetition = max(count)
    max_word = words[count.index(repetition)]

    words = list(filter(lambda x: x != max_word, words))

    print(f'\t{i+1}.\t\t {max_word} \t - \t\t\t {repetition}')

# In every loop we map a count list, as a list of repetition of every word in words list
# Then we find first word (in alphabetical order) that appeared the most
# Words is printed and removed from list, so in newly mapped count list the next max value can be found

print(f'\nDone in {perf_counter() - set_time}s')
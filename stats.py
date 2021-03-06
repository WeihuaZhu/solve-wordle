from utils import get_all_5_letter_words
import string

ALL_WORDS = frozenset(get_all_5_letter_words())


def get_single_letter_freq_wo_dup():
    count = {x: 0 for x in string.ascii_lowercase}
    for word in ALL_WORDS:
        for letter in set(word):
            letter = letter.lower()
            count[letter] += 1
    return count


def count_occurence(letters, word):
    occurence = 0
    word_set = set(word)
    for letter in letters:
        if letter in word_set:
            occurence += 1
    return occurence


count = get_single_letter_freq_wo_dup()
count_tuples = [(k, v) for k, v in count.items()]
count_tuples.sort(key=lambda x: x[1], reverse=True)
print(count_tuples)
candidate_letters = [count_tuple[0] for count_tuple in count_tuples[:5]]
candidate_letter_scores = {
    count_tuples[i][0]: (len(count_tuples) - i) for i in range(len(count_tuples))
}
print(candidate_letter_scores)

candidate_0s = []
for word in ALL_WORDS:
    if count_occurence(candidate_letters, word) >= 4:
        score = 0
        visited = set()
        for letter in word:
            if letter not in visited:
                score += candidate_letter_scores.get(letter, 0)
                visited.add(letter)
            else:
                continue
        candidate_0s.append((word, score))
candidate_0s.sort(key=lambda x: x[1], reverse=True)
print(candidate_0s)

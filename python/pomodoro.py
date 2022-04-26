str = "Pomodoro words"


def letter_counter(str):
    arr = str.split()
    word_counter = []

    for i in arr:
        total = []

        for j in i:
            total.append(i.count(j))
        word_counter.append(max(total))
    result = arr[word_counter.index(max(word_counter))]
    if max(word_counter) == 1:
        result = -1
    return result


print(letter_counter(str))
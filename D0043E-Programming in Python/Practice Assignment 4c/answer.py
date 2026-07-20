def count_word_frequency(text):
    words = text.lower().split()
    counts = {}

    for word in words:
        word = word.strip(",.!?")
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    return counts


def bubble_sort(word_list):
    n = len(word_list)

    # bubble sort passses
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if word_list[j]["freq"] < word_list[j + 1]["freq"]:
                temp = word_list[j]
                word_list[j] = word_list[j + 1]
                word_list[j + 1] = temp

    return word_list


while True:
    text = input("Enter a sentence: ").strip()
    if text == "":
        print("Input cannot be empty. Please type a sentence.")
    else:
        break

word_counts = count_word_frequency(text)

word_list = []
for word, freq in word_counts.items():
    word_freq = {"word": word, "freq": freq}
    word_list.append(word_freq)

sorted_word = bubble_sort(word_list)

while True:
    top_input = input("How many top words would you like to see? ").strip()

    if not top_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    top_n = int(top_input)

    if top_n < 1:
        print("PleaPlease enter a number greater than 0.")
        continue

    break


print("\nMost common words:")
for i in range(min(top_n, len(sorted_word))):
    word_info = sorted_word[i]
    print(f'{i + 1}. "{word_info["word"]}" - {word_info["freq"]} times')

### **Mini Project: Word Frequency Analyzer**

#### **Concepts Covered:**

Lists, dictionaries, loops

***

### **Project Description**

Write a program that analyzes how frequently words appear in a given text.

*   The user enters a **sentence or paragraph**.
*   The program **splits** the text into words and counts how many times each word appears.
*   The results are stored in a **dictionary**, where keys are words and values are frequencies.
*   The program then sorts them by frequency.
    *   Convert the dictionary into a list of dictionaries
    *   Sort the list based on the count
*   The program prints the **top N most common words**, where N is chosen by the user.

The program ignores punctuation and case.

Define a function count\_word\_frequency(text) that takes in the text and calculates the word frequency and return a dictionary with words as keys and count as values Define a function bubble\_sort(word\_list\_dict) that takes in a list of dictionaries and returns a sorted list

### **Example Interaction:**

    Enter a sentence: The sun is shining, the sky is blue, and the sun is bright. How many top words would you like to see? 2Most common words:1. "the" - 3 times2. "is" - 2 times
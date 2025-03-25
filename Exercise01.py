import re

words = "1387 – Hundred Years' War: An English fleet led by Richard Fitzalan attacked 250 to 360 French, Flemish and Castilian vessels in the Battle of Margate."
def word_freq(sentence:str):
    pattern = r"[^a-z ]+"
    sentence = sentence.lower()
    sentence = re.sub(pattern," ", sentence.lower())
    word_list = sentence.strip().split(" ")
    counts = {}
    for word in word_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

grades = {
    "Abcde Fghij": 150,
    "Mao":  80,
    "Violet": 100,
    "Maxwell": 70,
    "Edwin": 50,
    "Kenpo": 30,
    "Stalin": 72,
    "Elon Musk": 0
}

def student_grades(grades):
    student_list = []
    for students in grades.items():
        student_list.append(students)
    sortd = sorted(student_list, key=lambda student_list: student_list[1], reverse=True)
    results = f"Top student: {sortd[0][0]} with a score of {sortd[0][1]}"
    return results

def group_word(words):
    word_dict = {}
    for word in words:
        word_len = len(word)
        if word_len not in word_dict:
            word_dict[word_len] = []
        word_dict[word_len].append(word)
    return word_dict

if __name__ == "__main__":
    #frew = word_freq(words)
    #print(frew)
    #to_print = student_grades(grades)
    #print(to_print)
    worlist = []
    with open("word.txt") as l:
        for g in l:
            words = eval(g)
            print(words)
            hh = worlist.append(words)
    print(group_word(hh))
    pass
import random
from colorama import Fore, Style, init

init(autoreset=True)

words = ("кухня", "чобіт", "човен", "любов", "щастя", "мотор", "кожух", "геній", "масло", "мийка", "риска", "кішка", "сирок", "парта", "дошка", "груша","курка", "заєць", "війна", "ручка", "пушка", "пишка", "мишка", "мошка","байка", "варка")

hidden_word = random.choice(words)
attempts = 6
now_attempt = 0

print("ВІТАЄМО У WORDLE")
print(f"У вас є 6 спроб, щоб вгадати слово з 5 літер.\n")

while now_attempt < attempts:
    now_attempt += 1
    guess = input(f"Спроба {now_attempt}/{attempts}:\nВведіть слово: ").lower()

    if len(guess) != 5:
        print("Слово повинно містити 5 літер\n")
        now_attempt -= 1
        continue

    result = []
    for i in range(5):
        if guess[i] == hidden_word[i]:
            result.append(Fore.GREEN + guess[i] + Style.RESET_ALL)
        elif guess[i] in hidden_word:
            result.append(Fore.YELLOW + guess[i] + Style.RESET_ALL)
        else:
            result.append(Fore.WHITE + guess[i] + Style.RESET_ALL)

    print( " ".join(result), "\n")

    if guess == hidden_word:
        print(f"Ви вгадали наше слово {Fore.GREEN + hidden_word.upper()} за {now_attempt} спроб(и)!")
        break
else:
    print(f"На жаль, ви не вгадали слово. Ми загадали слово: {hidden_word.upper()}")


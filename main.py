import random

words = []
with open("5 letter words.txt", mode="r") as file:
    # print(file.readlines)
    words = [word.strip() for word in file.readlines()]
answer = random.choice(words)

is_game_over = False
chances = 1
result = []
while not is_game_over:
    user_word = input("Enter a word: ")
    if user_word.lower() in words:
        if user_word.lower() == answer.lower():
            print("Nice. You won") 
            is_game_over = True
            continue
        else:
            for index in range(0, 5):
                if user_word[index].lower() == answer[index]:
                    result.append("💚")
                elif user_word[index].lower() in answer:
                    result.append("💛")
                else:
                    result.append("🤍")
            string_result = "".join(result)
            print("Your answer: ")
            print(user_word)
            print(string_result)
            result = []
            chances += 1
            if chances > 6:
                print("You lost. Try again next time")
                break
    else:
        print("Your word is not in the list\n")
        continue
    

        
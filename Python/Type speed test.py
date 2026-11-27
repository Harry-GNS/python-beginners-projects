import difflib
import time

ready = input("Type Start when you are ready: ").capitalize()

if ready == "Start":
    sen = "The quick brown fox jumps over the lazy dog while typing fast and accurately"
    print(sen)
    start = time.time()
    type_user = input("")
    end = time.time()

    time_taken = round(end - start, 2)

    accuracy = round(difflib.SequenceMatcher(None, sen, type_user).ratio() * 100)
    words_per_minute = round(len(type_user.split()) / (time_taken / 60)) if time_taken > 0 else 0

    print(f"Accuracy: {accuracy}%")
    print(f"Time taken: {time_taken} sec")
    print(f"Speed: {words_per_minute} words per minute")

else:
    print("Exit")








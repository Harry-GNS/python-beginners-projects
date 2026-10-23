import time

ready = input("Type Start when you are ready: ").capitalize()

if ready == "Start":
    sen = "The quick brown fox jumps over the lazy dog while typing fast and accurately"
    print(sen)
    start = time.time()
    type_user = input("")
    end = time.time()

    time_taken = round(end - start, 2)

    if type_user == sen:
        print("100% Accuracy")
        print(f"Time taken: {time_taken} sec")

    else:
        print("Poor accuracy!")

else:
    print("Exit")








Questions= ("Who is the prime minister of India?",
            "How many elements are their in periodic table?",
            "Who is the richest person in the world?",
            "Who is known as the father of computer?",)


options = (("A) Manmohan Singh", "B) Mahatma Gandhi", "C) Indira Gandhi", "D) Narendra Modi"),
           ("A) 117", "B) 118", "C) 119", "D) 116"),
           ("A) Bill Gates", "B) Elon Musk", "C) Jeff Bezos", "D) Mukesh Ambani"),
           ("A) Charles Babbage", "B) Nikola Tesla", "C) Albert Einstein", "D) Virat Kohli"))


answers=["D","B","B","A"]

test=["A","B","C","D"]

score=0


for question,option,correct in zip(Questions,options,answers):
    print("-----------------------")
    print(question)
    for opt in option:
        print(opt)
    ans=input("Enter the correct option: ").upper()
    if ans == correct:
        print("Correct answer✅")
        score=score+1

    elif ans in test and ans!=correct:
        print("Wrong answer❌")
        print(f"The correct asnwer is:{correct}")    

    elif ans not in test:
        print("This option is not available")


print(f"Your score is {score}/4")







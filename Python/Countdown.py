import time

seconds= int(input("Enter time in seconds: "))

for counter in reversed(range (0,seconds+1)):
    seconds= counter % 60
    minutes= (counter // 60) % 60
    hours= counter // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!") 
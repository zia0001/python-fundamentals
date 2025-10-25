secret_number = 9

guess_count =0
attempts = 3
while guess_count < attempts:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
     print("You failed!")
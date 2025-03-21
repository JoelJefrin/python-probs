secret_num= 9
guess_count=0
guess_limit = 3
while guess_count < guess_limit:
    ur_num = int(input("guess a num between 1 to 10: "))
    guess_count+=1
    
    if ur_num == secret_num:
        print("you win")
        break
else:
    print("sorry, You Failed")
   
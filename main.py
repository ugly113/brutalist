import itertools


# Possible password characters
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?/\|}{[]`~_.,-+=:;"

# Starting variables
attempt = 0
length = 0
cracked = False


# Show results of password crack
def results(cracked, password, attempt):
    print(f'\n.:: {password} ::. Password cracked after {attempt} attempts\n')
    again = input('Crack another? y/n ')
    if again.lower() == 'y':
        main()
    else:
        exit()

# Loop combinations - Count attempts
def loop(length, password, attempt, cracked):
    if cracked == True:
        results(cracked, password, attempt)
    per = itertools.product(characters, repeat = length)
    for val in per:
        print(*val)
        cracked = ''.join(val)
        attempt = attempt + 1
        if password == cracked:
            cracked = True
            break
    length = length + 1
    loop(length, password, attempt, cracked)

# Input test password and initiate crack function
def main():
    password = input('Choose password: ')
    length = int(input('Choose min password length: '))
    loop(length, password, 0, cracked)

if __name__ == '__main__':
    main()

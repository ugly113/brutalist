
import itertools


# Possible password characters
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?/\|}{[]`~_.,-+=:;"


# Show results of password crack
def results(password, attempt):
    print(f'\n.:: {password} ::. Password cracked after {attempt} attempts')
    again = input(f'\nCrack another? y/n ')
    if again.lower() == 'y':
        main()
    else:
        exit()

# Attempt to crack with word list before brute force
def list(length, password, attempt, cracked):
    if cracked == True:
        results(cracked, password, attempt)
    else:
        with open('pw_list.txt', encoding='utf-8') as f:
            pw_list = [line.strip() for line in f]
            for pw in pw_list:
                print(pw)
                cracked = pw
                attempt += 1
                if password == cracked:
                    cracked = True
                    break
            brute(length, password, attempt, cracked)

# Attempt to crack with brute force
def brute(length, password, attempt, cracked):
    if cracked == True:
        results(password, attempt)
    per = itertools.product(characters, repeat = length)
    for val in per:
        print(*val)
        cracked = ''.join(val)
        attempt += 1
        if password == cracked:
            cracked = True
            break
    length += 1
    brute(length, password, attempt, cracked)

# Input test password and initiate crack function
def main():
    password = input('Choose password: ')
    length = int(input('Choose min password length: '))
    list(length, password, 0, False)


if __name__ == '__main__':
    main()

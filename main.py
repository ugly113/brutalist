
import itertools


# Possible password characters
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?/\|}{[]`~_.,-+=:; "


# Show results of password crack
def results(password, attempt):
    print(f'\n::: {password} ::: Password cracked after {attempt:,} attempts')
    again = input(f'\nCrack another? y/n ')
    if again.lower() == 'y':
        main()
    else:
        exit()

# Attempt to crack with word list before brute force
def list(length, password, attempt, cracked, mode):
    with open('pw_list.txt', encoding='utf-8') as f:
        pw_list = [line.strip() for line in f]
        for pw in pw_list:
            if len(pw) >= length:
                print(pw)
                cracked = pw
                attempt += 1
                if attempt % 1000000 == 0 and mode =='m':
                    continue_check = (input('Continue? y/n '))
                    if continue_check == 'y':
                        continue
                    else:
                        main()
                if password == cracked:
                    cracked = True
                    results(password, attempt)
                    break
        if mode == f:
            brute(length, password, attempt, cracked)
        elif mode == 'm' or 's':
            to_brute = input('\nNot found in password list. Try brute force? y/n ')
            if to_brute == 'y':
                brute(length, password, attempt, cracked)
            else:
                exit()

# Attempt to crack with brute force
def brute(length, password, attempt, cracked):
    if cracked == True:
        results(password, attempt)
    per = itertools.product(characters, repeat = length)
    for val in per:
        print(*val)
        cracked = ''.join(val)
        attempt += 1
        if attempt % 100000 == 0 and mode == 'm':
            continue_check = (input('Continue? y/n '))
            if continue_check == 'y':
                continue
            else:
                main()
        if password == cracked:
            cracked = True
            break
    length += 1
    brute(length, password, attempt, cracked)

# Input test password - set min password length - mode select - initiate crack function
def main():
    password = input('Choose password: ')
    length = int(input('Choose min password length: '))
    mode_select = input(f'M_anual\nS_emi Auto\nF_ull Auto\nChoose mode: ')
    mode = mode_select
    list(length, password, 0, False, mode)


if __name__ == '__main__':
    main()

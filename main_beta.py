import itertools
import hashing as h


# Possible password characters
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?/\|}{[]`~_.,-+=:; "
# Smart dictionary from user input
dictionary = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '?',
                '<', '>', 'loves', 'love', 'hate', '69', '666', '123', '777',
                'Love', 'Loves', 'I', 'i', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '0']

# Show results of password crack
def results(attempt, cracked):
    print(f'\n::: {cracked} ::: Password cracked after {attempt:,} attempts')
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
                cracked_pw = pw
                cracked_pw_h = h.sha256(cracked_pw)
                attempt += 1
                if attempt % 10000000 == 0 and mode =='m':
                    continue_check = (input(f'{attempt:,} attempts. Continue? y/n '))
                    if continue_check == 'y':
                        continue
                    else:
                        main()
                if password == str(cracked_pw_h):
                    cracked = cracked_pw
                    results(attempt, cracked)
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
    per = itertools.product(characters, repeat = length)
    for val in per:
        print(*val)
        cracked_pw = ''.join(val)
        attempt += 1
        if attempt % 10000000 == 0 and mode == 'm':
            continue_check = (input(f'{attempt:,} attempts. Continue? y/n '))
            if continue_check == 'y':
                continue
            else:
                main()
        if password == cracked_pw:
            cracked = cracked_pw
            results(attempt, cracked)
    length += 1
    brute(length, password, attempt, cracked)

# Attempt to crack with smart dictionary
def smart_dict(password, attempt, cracked, dictionary, item_num, mode, length):
    def smart_dict_loop(password, attempt, cracked, dictionary, item_num, mode, length):
        item_num += 1
        per = itertools.product(dictionary, repeat = item_num)
        for item in per:
            cracked_pw = ''.join(item)
            if len(cracked_pw) >= length:
                print(cracked_pw)
                cracked_pw_h = h.sha256(cracked_pw)
                attempt += 1
                if attempt % 10000000 == 0 and mode == 'm':
                    continue_check = (input(f'{attempt:,} attempts. Continue? y/n '))
                    if continue_check == 'y':
                        continue
                    else:
                        main()
                if attempt % 10000000 == 0:
                    continue_check = (input(f'{attempt:,} attempts. Continue? y/n '))
                    if continue_check == 'y':
                        continue
                    elif continue_check == 'n':
                        next_attack = input('N_ext attack or M_ain? ')
                        if next_attack.lower() == 'n':
                            # Moves onto password list attack
                            list(length, password, attempt, cracked, mode)
                        else:
                            main()
                    else:
                        exit()
                if password == str(cracked_pw_h):
                    cracked = cracked_pw
                    results(attempt, cracked)
        smart_dict_loop(password, attempt, cracked, dictionary, item_num, mode, length)
    smart_dict_loop(password, attempt, cracked, dictionary, item_num, mode, length)

# Input test password - set min password length - mode select -
# smart dictionary input - initiate crack function
def main():
    password = input('\nInput hashed password: ')
    length = int(input('\nChoose min password length: '))
    mode_select = input(f"""
                        \nM_anual - Skips smart dictionary, choose to continue after each phase and every 1mil attemps
                        \nS_emi Auto - Skips smart dictionary and choose to continue after each phase
                        \nF_ull Auto - Skips smart dictionary and runs until cracked or ctrl-c
                        \nSmart D_ictionary - Attack using OSINT info before starting blind attacks
                        \nChoose mode:
                        """)
    mode = mode_select.lower()
    if mode == 'd':
        smart_dict_input = input('OSINT keywords and #s (seperated by space): ')
        dictionary1 = smart_dict_input.split()
        for item in dictionary1:
            dictionary.insert(0, item)
            dictionary.insert(0, item.title())
        smart_dict(password, 0, False, dictionary, 0, mode, length)
    list(length, password, 0, False, mode)


if __name__ == '__main__':
    main()

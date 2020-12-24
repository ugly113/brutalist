import itertools
from time import process_time_ns, strftime, gmtime

# Possible password characters
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?/\|}{[]`~_.,-+=:;"


# Show results of password crack
def results(cracked, password, attempt, time):
    print(f'\n.:: {password} ::. Password cracked after {attempt} attempts')
    print(f'Time elapsed- {strftime("%H:%M:%S", gmtime(time))}')
#    convert_time(time)
    again = input(f'\nCrack another? y/n ')
    if again.lower() == 'y':
        main()
    else:
        exit()

# Loop combinations - Count attempts
def loop(length, password, attempt, cracked, t1_start):
    if cracked == True:
        t1_stop = process_time_ns()
        time = (t1_stop - t1_start)
        results(cracked, password, attempt, time)
    per = itertools.product(characters, repeat = length)
    for val in per:
        print(*val)
        cracked = ''.join(val)
        attempt = attempt + 1
        if password == cracked:
            cracked = True
            break
    length = length + 1
    loop(length, password, attempt, cracked, t1_start)

# Input test password and initiate crack function
def main():
    password = input('Choose password: ')
    length = int(input('Choose min password length: '))
    t1_start = process_time_ns()
    loop(length, password, 0, False, t1_start)


if __name__ == '__main__':
    main()

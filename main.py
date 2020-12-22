import itertools


characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?/\|}{[]`~`}"

def crack(password):
    attempt = 0
    per = itertools.product(characters, repeat=6)
    for val in per:
        attempt = attempt +1
        print(*val)
        cracked = ''.join(val)
        if password == cracked:
            print(f'\n.:: {password} ::. Password broken after {attempt} attemps')
            break


def main():
    password = input('Choose a 6 character password: ')
    crack(password)


if __name__ == '__main__':
    main()

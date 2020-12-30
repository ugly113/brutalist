********************************************************************************
                        .: Brutalist Password Cracker :.
********************************************************************************

Experiment in password cracking.

Current functionality includes setting minimum password length to limit guessing
to only passwords meeting minimum password requirements. Also includes three
modes; manual - user decides if the program should continue after every 100
million attempts and after each attack phase, semi-auto - user decides if
program should continue after each attack phase, and full-auto - program runs
through all phases without stopping until password is cracked or until ctrl-C;
or smart dictionary - takes OSINT info combined with common characters and words
before attempting the other attack phases.


Attack types:

[+] Smart dictionary - Uses user input of OSINT keywords and numbers combined
    with common characters and words.

[+] Password list - Uses a password list i.e. rockyou.

[+] Brute force - Iterates through letter, number, and special character
    combinations systematically. Only recommended for last resort. Might take
    the rest of your life to crack one hashed password.



********************************** GOALS ***************************************

Add tier 2 smart dictionary attack.
Add support for user selected word lists.
Add support for import of lists of hashed passwords.





*I'm a novice when it comes to coding. This program was built as a learning
project to help me improve my Python skills and explore an aspect of
cyber-security. Questions? Comments? -> givemeyoursouls@yahoo.com

import os
import time
import maximize_window
import text_files

maximize_window.maximize_console()

def call_main_menu():
       os.system('cls')
       print (r"""

       ==========================================================================
                                   Select an option:
                                   -----------------

       (1) New Toy Ideas 2020
       (2) Toys for Naughty List Citizens
       (3) (memo) If you're reading this, I fear it may already be too late...
       (0) Log Out

       ==========================================================================
       """)

       menu_choices = ["0", "1", "2", "3", "4"]
       menu_selection = input("Select an option by entering a number from the menu above: ")

       while menu_selection not in menu_choices:
              menu_selection = input("Selection invalid, please try again: ")
       
       if menu_selection in menu_choices:
              if menu_selection == "0":
                     menu_option0()
              elif menu_selection == "1":
                     menu_option1()
              elif menu_selection == "2":
                     menu_option2()
              elif menu_selection == "3":
                     menu_option3()

def menu_option0():
       os.system('cls')
       print("SEE YOU LATER, MR. NICK!\n")
       time.sleep(1)
       print("...\n")
       time.sleep(1)
       print("YOU HAVE BEEN LOGGED OUT")
       input("\n(Press any key to close this window)")

def menu_option1():
       os.system('cls')
       text_files.new_toy_ideas()
       input("\n(Press any key to return to main menu)")
       call_main_menu()

def menu_option2():
       os.system('cls')
       text_files.naughty_toys()
       input("\n(Press any key to return to main menu)")
       call_main_menu()

def menu_option3():
       os.system('cls')
       text_files.santa_memo()
       input("\n(Press any key to return to main menu)")
       call_main_menu()

os.system('cls')
print("\n")

time.sleep(2)

print (r"""

-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
 .       .        _+_        .                  .             .
                  /|\
       .           *     .       .            .                   .
.                i/|\i                                   .               .
      .    .     // \\*              
                */( )\\      .    Welcome to Santa's Virtual Workshop!  .
        .      i/*/ \ \i          *************************************
 .             / /* *\+\                               .. .
      .       */// + \*\\*                          ... .
             i/  /^  ^\  \i    .               ... . ...
.        .   / /+/ ()^ *\ \                 ........ .
            i//*/_^- -  \*\i              ...  ..  ..               .
    .       / // * ^ \ * \ \             ..
          i/ /*  ^  * ^ + \ \i          ..     ___            _________
          / / // / | \ \  \ *\         >U___^_[[_]|  ______  |_|_|_|_|_|
   ____(|)____    |||                  [__________|=|______|=|_|_|_|_|_|=
  |_____|_____|   |||                   oo OOOO oo   oo  oo   o-o   o-o
 -|     |     |-.-|||.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
  |_____|_____|
""")

print("\n")
print("Username: StNick280\n")
pw = input("Enter Password: ").upper()
while pw != "SANTABABY":
       pw = input("Incorrect. Please enter correct password: ").upper()
print("\nAcess Granted....\n")
time.sleep(1)
print("Loading files...")
for i in range(4):
       time.sleep(1)
       print("...")

call_main_menu()





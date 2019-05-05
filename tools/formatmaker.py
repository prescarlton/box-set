'''
simple tool to build the format of tv show names for my master list
for my legal media collection
'''

import pyperclip


def main():
    show_name = input("enter show name: ")
    year = int(input("enter year created: "))
    seasons = int(input("enter num seasons: "))
    return_str = "{0} ({1}) [{2} seasons]".format(show_name, year, seasons)
    return_str += "\n"
    for i in range(seasons):
        return_str += "[%d]" %(i+1)
    return_str += "\n"

    pyperclip.copy(return_str)
    print("copied to clipboard")

if __name__ == '__main__':
    main()

import sys
import pyautogui as pag
from time import sleep

def main():
    file_name = sys.argv[1]

    # holds each char of a text file
    chars = []

    # opens text file and puts every character into chars[]
    with open(file_name, encoding="utf8") as file:
        for line in file:
            for char in line:
                chars.append(char)

    countdown()

    # minecraft book pages allow 255 characters each.
    # minecraft books allow up to 50 pages.
    # 255 * 50 = 12750: the book character limit
    page_start = 0
    page_end = 255
    book_size = 12750

    page_count = 0

    while page_start <= len(chars):
        # take a 255 character slice of the text file and write it onto the page.
        # then move onto the next page
        page = chars[page_start:page_end]
        pag.write(page)
        pag.click()

        # keep moving the indexes up
        page_start += 255
        page_end += 255

        # if we get to the end of the book, increment book_size and pause.
        # this is so we can switch books in minecraft before continuing.
        if page_end > book_size:
            book_size += 12750
            page_count += 1
            pause = input("Press enter to continue...")
            countdown()

# counts down from 5
def countdown():
    for i in list(range(5))[::-1]:
        print(i+1)
        sleep(1)


if __name__ == "__main__":
    try:
        main()
    except:
        print("Invalid file name.")
        print("Correct usage: python author.py filename.txt")

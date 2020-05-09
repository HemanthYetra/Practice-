def process_book(filename):
    book = open(filename)
    for line in book:
        line =line.split()
        print(line)

process_book("my book.txt")



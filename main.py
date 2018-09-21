from Queue import Queue


def main():
    q = Queue()
    print('''
    0 - Exit
    1 - Print
    2 - Push
    3 - Head
    4 - Tail
    5 - Pop
    6 - Copy''')
    while True:
        try:
            k = int(input("-> "))
        except ValueError:
            k = "error"
        if k == 0:
            break
        elif k == 1:
            print(str(q))
        elif k == 2:
            elem = input("New element: ")
            q.push(elem)
        elif k == 3:
            print("Head: " + str(q.head()))
        elif k == 4:
            print("Tail: " + str(q.tail()))
        elif k == 5:
            q.pop()
            print("Popped")
        elif k == 6:
            cpy = Queue(original=q)
            print("Copy: " + str(cpy))
        else:
            print("Incorrect input")


main()

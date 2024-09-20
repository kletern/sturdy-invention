def main():
    print("Debug message")
    l: list = [1, 2, 34]
    print(len(l))
    l.append(14)
    print(l, l.count(1))
    l.extend([45])
    print(l)
    l.pop()
    print(l)
    tu = (3, 4)
    print(len(tu), tu.index(3), max(tu), tuple(l), list(tu))


if __name__ == "__main__":
    main()

if __name__ == '__main__':
    _, set1 = input(), set(input().split())
    _, set2 = input(), set(input().split())
    print(len(set1 - set2))

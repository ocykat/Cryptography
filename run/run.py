from cipher import caesar

if __name__ == "__main__":
    s1 = input()
    s2 = caesar.encode(s1, 3)
    s3 = caesar.decode(s1, 3)
    print(s2)
    print(s3)

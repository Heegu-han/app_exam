if __name__ == "__main__":
    fp = open('hello.txt','rt',encoding='utf-8')
    lines = fp.readlines()
    print(lines)
    fp.close()

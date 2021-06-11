if __name__ == "__main__":
    fp = open('hello.txt','rt',encoding='utf-8')
    line = fp.readline()
    print(line.strip())
    line = fp.readline()
    print(line.strip())
    line = fp.readline()
    print(line.strip())
    fp.close()

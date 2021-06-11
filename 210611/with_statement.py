if __name__ == "__main__":
    with open('hello.txt','rt',encoding='utf-8') as fp:
        lines = fp.readlines()

        for line in lines:
            print(line.strip())

    print("DONE")

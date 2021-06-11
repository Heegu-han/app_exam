if __name__ == "__main__":
    fp = open ('hello.txt', 'wt', encoding='utf-8')
    num = 1
    pi = 3.14
    msg = 'hello world'
    fp.write(f'{num}\n')
    fp.write(f'{pi}\n')
    fp.write(f'{msg}\n')
    fp.close()

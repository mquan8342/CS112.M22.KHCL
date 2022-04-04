def palindromeCheck(stg):
    n = len(stg)
    if n<=1:
        return False
    stg = stg.lower()
    for i in range (n):
        if stg[i] != stg[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    stg = input("Nhap chuoi: ")
    print(palindromeCheck(stg))

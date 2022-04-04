def find_x(a, b):
    if a != 0:
        print("Ngiem cua phuon trinh la: ", format((-b/a), '.2f'))
        return "Done"
    elif b == 0:
        print("Phuong trinh co vo so nghiem.")
        return "All"
    else: 
        print("Phuong trinh vo nghiem.")
        return "None"
    
    
if __name__ == '__main__':
    print ("Giai phuong trinh: ax + b = 0")
    a, b = map(int, input("Nhap lan luot cac he so a va b: ").split())
    find_x (a,b)
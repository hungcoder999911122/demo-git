## Các hàm
def get_age():
    while True: 
        s = input("Nhập tuổi của bạn: ")
        if s.isdigit(): 
            return int (s)
        print ("Số nhập không đúng. Vui lòng nhập lại!")

## ------------------------------------------------------------------------##

## nhập xuất: input(), print
name = input('Nhập tên của bạn: ')
print("xin chào ban "+ name + "!")

## ------------------------------------------------------------------------##

## Điều kiện, vòng lặp: if else, while
print(" Chọn chức năng: \n1. Nhập tuổi (hàm)\n2. Nhập tuổi ")
choice = int( input("Lựa chọn: ") )
if (choice == 1):
    Age = get_age()
else:
    Age = int(input("Nhập tuổi của bạn: "))

if (26 >= Age > 18):
    print (name + " đang học đại học !")
elif(18 > Age >= 16):
    print (name + " đang học trung học phổ thông !")
elif( 16 > Age >= 12):
    print (name + " đang học trung học cơ sở ! ")
elif(12> Age >= 5 ):
    print (name + "đang học mầm non !")
elif(65>= Age > 26):
    print (name + " đã đi làm !")
elif (Age > 65):
    print (name + " đã về hưu !")
else:
    print (name + " Chưa được đi học !" )


## ------------------------------------------------------------------------##
## danh sách, mảng, for
## hàm
## hàm strip(,) dùng tách chuỗi thành các phần tử dựa vào ký tự phân cách (dấu phẩy, khoảng trống )

def get_list_number(): 
    numbers = input ("Nhập các số vào mảng: (cách nhau bởi dấu phẩy)").strip(',')
    ## Chuyển từng phần tử trong numbers sang số nguyên 
    numbers = [int (num) for num in numbers]
    ## trả về kiểu dữ liệu 
    print ("Danh sách bạn vừa nhập là: ", numbers)

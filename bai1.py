
## CÁC HÀM
## Hàm lấy tuổi và kiểm tra xem nhập tuổi có hợp lệ không ?
def get_age():
    while True: 
        s = input("Nhập tuổi của bạn: ")
        if s.isdigit(): 
            return int (s)
        print ("Số nhập không đúng. Vui lòng nhập lại!")


## ------------------------------------------------------------------------##
## danh sách, mảng, for
## hàm
## hàm strip(',') dùng để loại bỏ dấu phẩy ở đầu và cuối chuỗi 

def get_list_number(): 
    numbers = input ("Nhập các số vào mảng (cách nhau bởi dấu phẩy): ").strip(',')
    ## Chuyển từng phần tử trong numbers sang số nguyên 
    numbers = [int (num.strip()) for num in numbers.split(',')]
    ## sau khi loại bỏ dấu phẩy ở đầu và cuối, tác thành 1 danh sách các chuỗi con dưa vào dấu phẩy bằng split
    ## strip () loại bỏ khoảng trằng đầu và cuối 

    ## trả về kiểu dữ liệu 
    return ("Danh sách vừa nhập là: " + str(numbers))

def get_work(Age, name):
    if (6 > Age >= 3):
        return (name + " đang học mầm non !")
    elif (10 >= Age >= 6):
        return (name + " đang học tiểu học !")
    elif (14 >= Age > 10):
        return (name + "đang học trung học cơ sở !")
    elif (18 >= Age > 14):
        return (name + " đang học trung học phổ thông !")
    elif (25 >= Age > 18):
        return (name + " đang học đại học !")
    elif (60 >= Age >= 26):
        return name + " đang đi làm !"
    elif (Age > 60):
        return (name + " được nghỉ hưu !")
    else:
        return (name + " chưa được đi học vẫn còn ở nhà trẻ !")


## ------------------------------------------------------------------------##
    ## ------------------ ĐOẠN THAO TÁC CHÍNH ----------------------- ##

## nhập xuất: input(), print
name = input('Nhập tên của bạn: ')
print("xin chào ban "+ name + "!")

## Điều kiện, vòng lặp: if else, while
print(" Chọn chức năng: \n1. Nhập tuổi (hàm)\n2. Nhập tuổi\n3. sắp xếp dãy số nhập vào ")
choice = int( input("Lựa chọn: ") )

match choice:
    case 1:
        Age = get_age()
        result1 = get_work(Age, name)
        print (result1)
    case 2: 
        Age = int(input("Nhập tuổi của bạn: "))
        result1 = get_work(Age, name)
        print (result1)
    case 3:
        result_list = get_list_number()
        print (result_list)




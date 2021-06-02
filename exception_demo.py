def my_function():
    x = int(input("Nhap vao so chia: "))
    y = int(input("Nhap vao so bi chia: "))

    ds = [1,7]

    #Bắt lỗi trực tiếp
    try:
        print(y/x)
        print(ds[100])
    except Exception:
        raise

    print("Chia thanh cong!!!")

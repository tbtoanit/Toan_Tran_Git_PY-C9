from exception_demo import my_function

try:
    my_function()
except Exception as e:
    print("Chia cho khong bi loi")
finally:
    print("The final line")

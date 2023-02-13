# Project: Number to letter converter
yekan = ["","یک","دو","سه","چهار","پنج","شش","هفت","هشت","نه"]
numbers10_19 = ["ده","یازده","دوازده","سیزده","چهارده","پانزده","شانزده","هفده","هجده","نونزده"]
dahgan = ["بیست و","سی و","چهل و","پنجاه و","شصت و","هفتاد و","هشتاد و","نود و"]
sadgan = ["","صد و","دویست و","سیصد و","چهارصد و","پانصد و","ششصد و","هفتصد و","هشتصد و","نهصد و"]
basis = ["","هزار و","میلیون و","بیلیون و","تریلیون و","کوآدریلیون و","کوینتیلیون و","سکستیلیون و","سپتیلیون و","اکتیلیون و","نانیلیون و","دسیلیون و","آندسیلیون و","دیودسیلیون و","تریدسیلیون و","کواتیوردسیلیون و","کویندسیلیون و","سکسدسیلیون و","سپتدسیلیون و","اُکتودسیلیون و","نومدسیلیون و"]
def check(list, index):
    sum = 0
    for i in list[index+1:]:
        for j in i:
            j = int(j)
            sum += j
    return sum
possibility = True
while possibility:
    try:
        number = int(input("قیمت را به تومان وارد کنید: "))
        if str(abs(number)).isnumeric():
            possibility = False
    except:
        possibility = True
        print("ورودی باید یک عدد باشد، از وارد کردن کاراکتر های غیر از عدد خودداری کنید!")
number = number * 10
while len(str(number)) > 63:
    number = int(input("طول عدد(به ریال) وارد شده باید کمتر از 63 رفم باشد، لطفا عدد را دوباره وارد کنید: "))
else:
    if number < 0:
        print("منفی",end=" ")
        number = abs(number)
    formated_number = []
    while number != 0:
        formated_number.insert(0, str(number%1000))
        number //= 1000
    summer = 0
    for item in formated_number.copy():
        if int(item) >= 0:
            if item != "0" and item != "00" and item != "000":
                index = formated_number.index(item)
                length = len(formated_number)
                if check(formated_number,index) == 0:
                    item_basis = basis[length-1].rstrip("و")
                else:
                    item_basis = basis[length-1]
                if len(item) == 1:
                    unit = formated_number[index]
                    unit = int(unit)
                    price = yekan[unit] + " " + item_basis
                    print(price, end=" ")
                elif len(item) == 2:
                    if int(item) < 20:
                        o_unit = int(item) // 1 % 10
                        product = numbers10_19[o_unit] + " " + item_basis
                        print(product, end=" ")
                    else:
                        tens = int(item) // 10 % 10
                        units = int(item) // 1 % 10
                        if units == 0:
                            product = dahgan[tens - 2].rstrip("و") + " " + item_basis
                        else:
                            product = dahgan[tens - 2] + " " + yekan[units] + " " + item_basis
                        print(product, end=" ")
                elif len(item) == 3:
                    hun = int(item) // 100 % 10
                    tens_digit = int(item) // 10 % 10
                    units_digit = int(item) // 1 % 10
                    if tens_digit < 2:
                        if tens_digit == 0:
                            l = yekan[units_digit]
                        else:
                            l = numbers10_19[units_digit]
                    else:
                        if units_digit == 0:
                            l = dahgan[tens_digit - 2].rstrip("و")
                        else:
                            l = dahgan[tens_digit-2] + " " + yekan[units_digit]
                    if tens_digit == 0 and units_digit == 0:
                        result = sadgan[hun].rstrip("و") + " " + l + " " + item_basis
                    else:
                        result = sadgan[hun] + " " + l + " " + item_basis
                    print(result, end=" ")
        summer += int(item)
        formated_number.remove(item)
    if summer == 0:
        print("صفر" + " ریال")
    else:
        print("ریال", end=" ")
length=input("가로:")
width=input("세로:")
height=input("높이:")

length=float(length)
width=float(width)
height=float(height)

volume=length*width*height

print("박스의 부피는",volume,"입니다.")

#택배요금
total_length = length + width + height

#80cm 이하 : 5000원
#80~100cm : 8000원
#100~120cm : 10000원
#120~160cm : 13000원
#160cm~ : 배송X

if total_length <= 80:
    charge = 5000
elif total_length <= 100:
    charge = 8000
elif total_length <= 120:
    charge = 10000
elif total_length <= 160:
    charge = 13000
else:
    charge = "nono"
print("Total length:",total_length)
print("Charge:",charge)

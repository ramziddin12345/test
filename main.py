age = int(input("Yoshingizni kiriting: "))
if age <= 4:
    print("Siz uchun chipta bepul")
elif age <= 12:
    print("Siz uchun chipta 15000")
elif age < 16 or age <= 65:
    print("Siz uchun chipta 20000")
else:
    print("Siz uchun chipta bepul")

harorat = int(input("Havo haroratini kiriting: "))
if harorat <= 0:
    print("Havo harorati juda sovuq")
elif harorat >= 30:
    print("Havo harorati juda issiq")
elif harorat >= 0 and harorat <= 30:
    print("Havo harorati qulay")

baho = int(input("(0 dan 100 gacha) baho kiriting: "))
if baho >= 90:
    print("A'lo")
elif baho >= 80 and baho <= 90:
    print("Yahshi")
elif baho >=70 and baho <=80:
    print("Qoniqarli")
elif baho <= 70:
    print("Yomon")

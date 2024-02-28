w, h = map(int, input('введите вес (в фунтах) и высоту человека (в дюймах) ' ).split())
h = (h*2.54)/100
w = w*0.453592
bmi =w/(h**2)
print(round(bmi, 2))
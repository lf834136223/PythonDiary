#TempConvert.py
print ('输入温度值的格式为：数字加c/f，字母不区分大小写')
Tempstr = input('请输入带符号的温度值：')
if Tempstr[-1] in['F','f']:
    C = (eval(Tempstr[0:-1])-32)/1.8
    print('转换后的温度值是{:.2f}C'.format(C))
elif Tempstr[-1] in ['C','c']:
    F =  1.8 * eval(Tempstr[0:-1])+32
    print('转换后的温度值是{:.2f}F'.format(F))
else:
    print('输入格式错误')
    

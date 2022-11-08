r1, r2, i1, r3, i2, i3, i4 = map(int, input().split())
s1,s2,s3 = r1^i1^i2^i4, r2^i1^i3^i4, r3^i2^i3^i4
s = str(s1)+str(s2)+str(s3)
syndrome = ['000','001','010','011','100','101','110','111']
err_symbol = ['НЕТ','r3','r2','i3','r1','i2','i1','i4']
err = err_symbol[syndrome.index(s)]
if err == 'i1': i1 = (i1+1)%2
elif err == 'i2': i2 = (i2+1)%2
elif err == 'i3': i3 = (i3+1)%2
elif err == 'i4': i4 = (i4+1)%2
print(i1,i2,i3,i4,err)

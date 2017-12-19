s=10
A=a=9
B=b=8
C=c=7
D=d=6
E=e=5
U=u=0
s1=3
s11=raw_input("enter your first subject result grade : ")
if ((s11 == 's') or (s11 ==  'S')):
    s11 =10
elif ((s11 == 'a') or (s11 ==  'A')):
    s11 = 9   
elif ((s11 == 'b') or (s11 ==  'B')):
    s11 =8
elif ((s11 == 'c') or (s11 ==  'C')):
    s11 =7
elif ((s11 == 'd') or (s11 ==  'D')):
    s11 =6
elif ((s11 == 'e') or (s11 ==  'E')):
    s11 =5 
else:
    s11 =0
s2=4
s22=raw_input("enter your second subject result grade : ")
if ((s22 == 's') or (s22 ==  'S')):
    s22 =10
elif ((s22 == 'a') or (s22 ==  'A')):
    s22 = 9   
elif ((s22 == 'b') or (s22 ==  'B')):
    s22 =8
elif ((s22 == 'c') or (s22 ==  'C')):
    s22 =7
elif ((s22 == 'd') or (s22 ==  'D')):
    s22 =6
elif ((s22 == 'e') or (s22 ==  'E')):
    s22 =5
else:
    s22 =0
s3=3
s33=raw_input("enter your third subject result grade : ")
if ((s33 == 's') or (s33 ==  'S')):
    s33 =10
elif ((s33 == 'a') or (s33 ==  'A')):
    s33 = 9   
elif ((s33 == 'b') or (s33 ==  'B')):
    s33 =8
elif ((s33 == 'c') or (s33 ==  'C')):
    s33 =7
elif ((s33 == 'd') or (s33 ==  'D')):
    s33 =6
elif ((s33 == 'e') or (s33 ==  'E')):
    s33 =5
else:
    s33 =0
s4=2
s44=raw_input("enter your fourth subject result grade : ")
if ((s44 == 's') or (s44 ==  'S')):
    s44 =10
elif ((s44 == 'a') or (s44 ==  'A')):
    s44 = 9   
elif ((s44 == 'b') or (s44 ==  'B')):
    s44 =8
elif ((s44 == 'c') or (s44 ==  'C')):
    s44 =7
elif ((s44 == 'd') or (s44 ==  'D')):
    s44 =6
elif ((s44 == 'e') or (s44 ==  'E')):
    s44 =5
else:
    s44 =0
s5=3
s55=raw_input("enter your fifth subject result grade : ")
if ((s55 == 's') or (s55 ==  'S')):
    s55 =10
elif ((s55 == 'a') or (s55 ==  'A')):
    s55 = 9   
elif ((s55 == 'b') or (s55 ==  'B')):
    s55 =8
elif ((s55 == 'c') or (s55 ==  'C')):
    s55 =7
elif ((s55 == 'd') or (s55 ==  'D')):
    s55 =6
elif ((s55 == 'e') or (s55 ==  'E')):
    s55 =5
else:
    s55 =0
s6=4
s66=raw_input("enter your sixith subject result grade : ")
if ((s66 == 's') or (s66 ==  'S')):
    s66 =10
elif ((s66 == 'a') or (s66 ==  'A')):
    s66 = 9   
elif ((s66 == 'b') or (s66 ==  'B')):
    s66 =8
elif ((s66 == 'c') or (s66 ==  'C')):
    s66 =7
elif ((s66 == 'd') or (s66 ==  'D')):
    s66 =6
elif ((s66 == 'e') or (s66 ==  'E')):
    s66 =5
else:
    s66 =0
subjectcredit = (s1*s11) + (s2*s22) + (s3*s33) + (s4*s44) + (s5*s55) + (s6*s66)
credit=s1+s2+s3+s4+s5+s6
print("your gpa is {}".format(float(subjectcredit/credit)))


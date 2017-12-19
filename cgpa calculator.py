_author = 'balaganesan'
def grade():
    g=raw_input("enter your subject result grade : ")
    if ((g == 's') or (g ==  'S')):
        g =10
    elif ((g == 'a') or (g ==  'A')):
        g = 9   
    elif ((g == 'b') or (g ==  'B')):
       g =8
    elif ((g == 'c') or (g ==  'C')):
        g =7
    elif ((g == 'd') or (g ==  'D')):
        g =6
    elif ((g == 'e') or (g ==  'E')):
        g =5 
    else:
        g =0
    return g

print('\n####################@@@@@@@@@@@@@@@@@<------CGPA CALCULATOR------->@@@@@@@@@@@@@@@@######################')
while True:
    semester = int(raw_input("type your semsester: \n1\n2\n3\n4\n5\n6\n7\n8\nall\nyour choice : "))
    if semester == 1 :
        s1,s2,s3,s4,s5,s6,s7,s8,s9=4,4,3,3,3,4,2,2,1
        s11 = grade()
        s12 = grade()
        s13 = grade()
        s14 = grade()
        s15 = grade()
        s16 = grade()
        s17 = grade()
        s18 = grade()
        s19 = grade()
        first_semster = (s1*s11) + (s2*s12) + (s3*s13) + (s4*s14) + (s5*s15) + (s6*s16) + (s7*s17) + (s8*s18) + (s9*s19)
        first_credit=s1+s2+s3+s4+s5+s6+s7+s8+s9
        print("your  first semester gpa is {}".format(float(first_semster/first_credit)))
    elif semester == 2 :
        s1,s2,s3,s4,s5,s6,s7,s8=4,4,3,3,3,4,2,2
        s21 = grade()
        s22 = grade()
        s23 = grade()
        s24 = grade()
        s25 = grade()
        s26 = grade()
        s27 = grade()
        s28 = grade()
        second_semster = (s1*s21) + (s2*s22) + (s3*s23) + (s4*s24) + (s5*s25) + (s6*s26) + (s7*s27) + (s8*s28)
        second_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your  second semester gpa is {}".format(float(second_semster/second_credit)))
    elif semester == 3 :
        s1,s2,s3,s4,s5,s6,s7,s8=4,4,3,3,4,4,2,2
        s31 = grade()
        s32 = grade()
        s33 = grade()
        s34 = grade()
        s35 = grade()
        s36 = grade()
        s37 = grade()
        s38 = grade()
        third_semster =(s1*s31)+(s2*s32)+(s3*s33)+(s4*s34)+(s5*s35)+(s6*s36)+(s7*s37)+(s8*s38)
        third_credit = s1+s2+s3+s4+s5+s6+s7+s8
        print("your  third semester gpa is {}".format(float(third_semster / third_credit)))
    elif semester == 4 :
        s1,s2,s3,s4,s5,s6,s7,s8,s9=4,3,3,4,3,3,2,2,2
        s41 = grade()
        s42 = grade()
        s43 = grade()
        s44 = grade()
        s45 = grade()
        s46 = grade()
        s47 = grade()
        s48 = grade()
        fourth_semster = (s1*s41)+(s2*s42)+(s3*s43)+(s4*s44)+(s5*s45)+(s6*s46)+(s7*s47)+(s8*s48)
        fourth_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your fourth semester gpa is {}".format(float(fourth_semster/fourth_credit)))
    elif semester == 5 :
        s1,s2,s3,s4,s5,s6,s7,s8=3,4,4,3,3,2,2,2
        s51 = grade()
        s52 = grade()
        s53 = grade()
        s54 = grade()
        s55 = grade()
        s56 = grade()
        s57 = grade()
        s58 = grade()
        fifth_semster = (s1*s51)+(s2*s52)+(s3*s53)+(s4*s54)+(s5*s55)+(s6*s56)+(s7*s57)+(s8*s58)
        fifth_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your  fifth semester gpa is {}".format(float(fifth_semster/fifth_credit)))
    elif semester == 6 :
        s1,s2,s3,s4,s5,s6,s7,s8,s9=3,3,3,3,3,3,2,2,2
        s61 = grade()
        s62 = grade()
        s63 = grade()
        s64 = grade()
        s65 = grade()
        s66 = grade()
        s67 = grade()
        s68 = grade()
        s69 = grade()
        sixth_semster = (s1*s61)+(s2*s62)+(s3*s63)+(s4*s64)+(s5*s65)+(s6*s66)+(s7*s67)+(s8*s68)+(s9*s69)
        sixth_credit = s1+s2+s3+s4+s5+s6+s7+s8+s9
        print("your  sixth semester gpa is {}".format(float(sixth_semster/sixth_credit)))
    elif semester == 7 :
        s1,s2,s3,s4,s5,s6,s7,s8=3,3,3,3,3,3,2,2
        s71 = grade()
        s72 = grade()
        s73 = grade()
        s74 = grade()
        s75 = grade()
        s76 = grade()
        s77 = grade()
        s78 = grade()
        seventh_semster = (s1*s71) + (s2*s72) + (s3*s73) + (s4*s74) + (s5*s75) + (s6*s76) + (s7*s77) + (s8*s78)
        seventh_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your  seventh semester gpa is {}".format(float(seventh_semster/seventh_credit)))
    elif semester == 8 :
        s1,s2,s3,s4,s5=3,3,3,3,6
        s81 = grade()
        s82 = grade()
        s83 = grade()
        s84 = grade()
        s85 = grade()
        eight_semster = (s1*s81) + (s2*s82) + (s3*s83) + (s4*s84) + (s5*s85)
        eight_credit=s1+s2+s3+s4+s5
        print("your  8th semester gpa is {}".format(float(eight_semster/eight_credit)))
    elif semester == 10 :
        s1,s2,s3,s4,s5,s6,s7,s8,s9=4,4,3,3,3,4,2,2,1
        s11 = grade()
        s12 = grade()
        s13 = grade()
        s14 = grade()
        s15 = grade()
        s16 = grade()
        s17 = grade()
        s18 = grade()
        s19 = grade()
        first_semster = (s1*s11) + (s2*s12) + (s3*s13) + (s4*s14) + (s5*s15) + (s6*s16) + (s7*s17) + (s8*s18) + (s9*s19)
        first_credit=s1+s2+s3+s4+s5+s6+s7+s8+s9
        print("your  first semester gpa is {}".format(float(first_semster/first_credit)))
        print("your  first semester cgpa is {}".format(float(first_semster/first_credit)))
        s1,s2,s3,s4,s5,s6,s7,s8=4,4,3,3,3,4,2,2
        s21 = grade()
        s22 = grade()
        s23 = grade()
        s24 = grade()
        s25 = grade()
        s26 = grade()
        s27 = grade()
        s28 = grade()
        second_semster = (s1*s21) + (s2*s22) + (s3*s23) + (s4*s24) + (s5*s25) + (s6*s26) + (s7*s27) + (s8*s28)
        second_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your  second semester gpa is {}".format(float(second_semster/second_credit)))
        print("your upto-second semester cgpa is {}".format(float(first_semster+second_semster) / (first_credit+second_credit)))
        s1,s2,s3,s4,s5,s6,s7,s8=4,4,3,3,4,4,2,2
        s31 = grade()
        s32 = grade()
        s33 = grade()
        s34 = grade()
        s35 = grade()
        s36 = grade()
        s37 = grade()
        s38 = grade()
        third_semster =(s1*s31)+(s2*s32)+(s3*s33)+(s4*s34)+(s5*s35)+(s6*s36)+(s7*s37)+(s8*s38)
        third_credit = s1+s2+s3+s4+s5+s6+s7+s8
        print("your  third semester gpa is {}".format(float(third_semster / third_credit)))
        print("your  upto-third semester cgpa is {}".format(float(first_semster+second_semster+third_semster) / (first_credit+second_credit +third_credit)))
        s1,s2,s3,s4,s5,s6,s7,s8,s9=4,3,3,4,3,3,2,2,2
        s41 = grade()
        s42 = grade()
        s43 = grade()
        s44 = grade()
        s45 = grade()
        s46 = grade()
        s47 = grade()
        s48 = grade()
        fourth_semster = (s1*s41)+(s2*s42)+(s3*s43)+(s4*s44)+(s5*s45)+(s6*s46)+(s7*s47)+(s8*s48)
        fourth_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your fourth semester gpa is {}".format(float(fourth_semster/fourth_credit)))
        print("your upto-fourth semester cgpa is {}".format(float(first_semster+second_semster+third_semster+fourth_semster) / (first_credit+second_credit +third_credit+fourth_credit)))
        s1,s2,s3,s4,s5,s6,s7,s8=3,4,4,3,3,2,2,2
        s51 = grade()
        s52 = grade()
        s53 = grade()
        s54 = grade()
        s55 = grade()
        s56 = grade()
        s57 = grade()
        s58 = grade()
        fifth_semster = (s1*s51)+(s2*s52)+(s3*s53)+(s4*s54)+(s5*s55)+(s6*s56)+(s7*s57)+(s8*s58)
        fifth_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your  fifth semester gpa is {}".format(float(fifth_semster/fifth_credit)))
        print("your  upto-fifth semester cgpa is {}".format(float(first_semster+second_semster+third_semster+fourth_semster+fifth_semster) / (first_credit+second_credit +third_credit+fourth_credit+fifth_credit)))
        s1,s2,s3,s4,s5,s6,s7,s8,s9=3,3,3,3,3,3,2,2,2
        s61 = grade()
        s62 = grade()
        s63 = grade()
        s64 = grade()
        s65 = grade()
        s66 = grade()
        s67 = grade()
        s68 = grade()
        s69 = grade()
        sixth_semster = (s1*s61)+(s2*s62)+(s3*s63)+(s4*s64)+(s5*s65)+(s6*s66)+(s7*s67)+(s8*s68)+(s9*s69)
        sixth_credit = s1+s2+s3+s4+s5+s6+s7+s8+s9
        print("your  sixth semester gpa is {}".format(float(sixth_semster/sixth_credit)))
        print("your upto-sixth cgpa is {}".format(float(first_semster+second_semster+third_semster+fourth_semster+fifth_semster+sixth_semster) / (first_credit+second_credit +third_credit+fourth_credit+fifth_credit+sixth_credit)))
        s1,s2,s3,s4,s5,s6,s7,s8=3,3,3,3,3,3,2,2
        s71 = grade()
        s72 = grade()
        s73 = grade()
        s74 = grade()
        s75 = grade()
        s76 = grade()
        s77 = grade()
        s78 = grade()
        seventh_semster = (s1*s71) + (s2*s72) + (s3*s73) + (s4*s74) + (s5*s75) + (s6*s76) + (s7*s77) + (s8*s78)
        seventh_credit=s1+s2+s3+s4+s5+s6+s7+s8
        print("your  seventh semester gpa is {}".format(float(seventh_semster/seventh_credit)))
        print("your  seventh semester cgpa is {}".format(float(first_semster+second_semster+third_semster+fourth_semster+fifth_semster+sixth_semster+seventh_semster) / (first_credit+second_credit +third_credit+fourth_credit+fifth_credit+sixth_credit+seventh_credit)))
        s1,s2,s3,s4,s5=3,3,3,3,6
        s81 = grade()
        s82 = grade()
        s83 = grade()
        s84 = grade()
        s85 = grade()
        eight_semster = (s1*s81) + (s2*s82) + (s3*s83) + (s4*s84) + (s5*s85)
        eight_credit=s1+s2+s3+s4+s5
        CGPA= (first_semster+second_semster+third_semster+fourth_semster+fifth_semster+sixth_semster+seventh_semster+eight_semster) / (first_credit+second_credit +third_credit+fourth_credit+fifth_credit+sixth_credit+seventh_credit+eight_credit)
        print("your  8th semester gpa is {}".format(float(eight_semster/eight_credit)))
        print("your first cgpa is {}".format(float(first_semster+second_semster+third_semster+fourth_semster+fifth_semster+sixth_semster+seventh_semster+eight_semster)/(first_credit+second_credit+third_credit+fourth_credit+fifth_credit+sixth_credit+seventh_credit+eight_credit)))
        if CGPA >= 8.51 :
            print("your First Class Withdistinction(FWD)")
        elif ((CGPA <= 8.50) and (CGPA >= 6.51)):
            print("your First Class(FC)")
        elif ((CGPA <= 6.50) and (CGPA >= 5.01)):
            print("your second Class(SC)")
        else :
            print("you are not eligible on class please clear the arrear")
    else :
        break
        
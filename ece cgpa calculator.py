def first():
    print("enter your first semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("HS6151 Technical English :")
    s12=input("MA6151 Mathematics :")
    s13=input("PH6151 Engineering Physics :")
    s14=input("CY6151 Engineering Chemistry :")
    s15=input("GE6151 Computer Programming : ")
    s16=input("GE6152 Engineering Graphics : ")
    s17=input("GE6161 Computer Practices Laboratory : ")
    s18=input("GE6162 Engineering Practices Laboratory : ")
    s19=input("GE6163 Physics and Chemistry Laboratory - I : ")
    first_semster = (4*g[s11]) + (4*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (4*g[s16]) + (2*g[s17]) + (2*g[s18]) + (1*g[s19])
    first_credit=4+4+3+3+3+4+2+2+1
    print("your  first semester gpa is {}".format(float(first_semster/first_credit)))
def second():
    print("enter your second semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("HS6251 Technical English – II :")
    s12=input("MA6251 Mathematics – II :")
    s13=input("PH6251 Engineering Physics – II :")
    s14=input("CY6251 Engineering Chemistry – II :")
    s15=input("EC6201 Electronic Devices : ")
    s16=input("EE6201 Circuit Theory : ")
    s17=input("GE6262 Physics and Chemistry Laboratory - II : ")
    s18=input("EC6211 Circuits and Devices Laboratory : ")
    second_semster = (4*g[s11]) + (4*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (4*g[s16]) + (1*g[s17]) + (2*g[s18]) 
    second_credit=4+4+3+3+3+4+1+2
    print("your  second semester gpa is {}".format(float(second_semster/second_credit)))
def third():
    print("enter your third semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("MA6351 Transforms and Partial Differential Equations :")
    s12=input("EE6352 Electrical Engineering and Instrumentation :")
    s13=input("EC6301 Object Oriented Programming and Data Structures :")
    s14=input("EC6302 Digital Electronics :")
    s15=input("EC6303 Signals and Systems : ")
    s16=input("EC6304 Electronic Circuits- I : ")
    s17=input("EC6311 Analog and Digital Circuits Laboratory : ")
    s18=input("EC6312  OOPS and Data Structures Laboratory : ")
    third_semster = (4*g[s11]) + (4*g[s12]) + (3*g[s13]) + (3*g[s14]) + (4*g[s15]) + (4*g[s16]) + (2*g[s17]) + (2*g[s18]) 
    third_credit=4+4+3+3+4+4+2+2
    print("your  third semester gpa is {}".format(float(third_semster/third_credit)))
def fourth():
    print("enter your forth semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("MA6451 Probability and Random Processes :")
    s12=input("EC6401 Electronic Circuits II :")
    s13=input("EC6402 Communication Theory :")
    s14=input("EC6403 Electromagnetic Fields :")
    s15=input("EC6404 Linear Integrated Circuits : ")
    s16=input("EC6405 Control System Engineering : ")
    s17=input("EC6411 Circuit and Simulation Integrated Laboratory : ")
    s18=input("EC6412 Linear Integrated Circuit Laboratory : ")
    s19=input("EE6461 Electrical Engineering and Control System :")
    fourth_semster = (4*g[s11]) + (3*g[s12]) + (3*g[s13]) + (4*g[s14]) + (3*g[s15]) + (3*g[s16]) + (2*g[s17]) + (2*g[s18]) + (2*g[s19])
    fourth_credit=4+3+3+4+3+3+2+2+2
    print("your  fourth semester gpa is {}".format(float(fourth_semster/fourth_credit)))
def fifth():
    print("enter your fifth semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("EC6501 Digital Communication :")
    s12=input("EC6502  Principles of Digital Signal Processing :")
    s13=input("EC6503 Transmission Lines and Wave Guides :")
    s14=input("GE6351 Environmental Science and Engineering :")
    s15=input("EC6504 Microprocessor and Microcontroller : ")
    s16=input("EC6511 Digital Signal Processing Laboratory : ")
    s17=input("EC6512 Communication System Laboratory : ")
    s18=input("EC6513 Microprocessor and Microcontroller Laboratory : ")
    fifth_semster = (3*g[s11]) + (4*g[s12]) + (4*g[s13]) + (3*g[s14]) + (3*g[s15]) + (2*g[s16]) + (2*g[s17]) + (2*g[s18]) 
    fifth_credit=3+4+4+3+3+2+2+2
    print("your  fifth semester gpa is {}".format(float(fifth_semster/fifth_credit)))
def sixth():
    print("enter your sixth semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("MG6851 Principles of Management :")
    s12=input("CS6303 Computer Architecture :")
    s13=input("CS6551 Computer Networks :")
    s14=input("EC6601 VLSI Design :")
    s15=input("EC6602 Antenna and Wave proPagation : ")
    s16=input("EC2021 Medical Electronics : ")
    s17=input("EC6611 Computer Networks Laboratory : ")
    s18=input("EC6612 VLSI  Design Laboratory : ")
    s19=input("GE6674  Communication and Soft Skills Laboratory : ")
    sixth_semster = (3*g[s11]) + (3*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (3*g[s16]) + (2*g[s17]) + (2*g[s18]) +  (2*g[s19])
    sixth_credit=3+3+3+3+3+3+2+2+2
    print("your sixth semester gpa is {}".format(float(sixth_semster/sixth_credit)))
def seventh():
    print("enter your seventh semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("EC6701RF and Microwave Engineering :")
    s12=input("EC6702 Optical Communication and Networks :")
    s13=input("EC6703 Embedded and Real Time Systems :")
    s14=input("EC6004 Satellite Communication :")
    s15=input("EC6011 Electro Magnetic Interference and Compatibility : ")
    s16=input("EC6016-Opto Electronic Devices : ")
    s17=input("EC6711 Embedded  Laboratory : ")
    s18=input("EC6712 Optical and Microwave Laboratory : ")
    seventh_semster = (3*g[s11]) + (3*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (3*g[s16]) + (2*g[s17]) + (2*g[s18]) 
    seventh_credit=3+3+3+3+3+3+2+2
    print("your  seventh semester gpa is {}".format(float(seventh_semster/seventh_credit)))
def eighth():
    print("enter your eight  semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("EC6801 Wireless Communication :")
    s12=input("EC6802 Wireless Networks :")
    s13=input("GE6757 Total Quality Management :")
    s14=input("EC6018 Multimedia Compression and Communication :")
    s15=input("Project Work :")
    eight_semster = (3*g[s11]) + (3*g[s12]) + (3*g[s13]) + (3*g[s14]) + (6*g[s15]) 
    eight_credit=3+3+3+3+6
    print("your  eight semester gpa is {}".format(float(eight_semster/eight_credit)))
grade=input("type your result on semester : ")
if grade == 1 :
    first()
elif grade == 2 :
    second()
elif grade == 3 :
    third()
elif grade == 4 :
    fourth()
elif grade == 5 :
    fifth()
elif grade == 6 :
    sixth()
elif grade == 7 :
    seventh()
elif grade == 8 :
    eighth()
elif grade == 'all' :
    print("enter your first semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("HS6151 Technical English :")
    s12=input("MA6151 Mathematics :")
    s13=input("PH6151 Engineering Physics :")
    s14=input("CY6151 Engineering Chemistry :")
    s15=input("GE6151 Computer Programming : ")
    s16=input("GE6152 Engineering Graphics : ")
    s17=input("GE6161 Computer Practices Laboratory : ")
    s18=input("GE6162 Engineering Practices Laboratory : ")
    s19=input("GE6163 Physics and Chemistry Laboratory - I : ")
    first_semster = (4*g[s11]) + (4*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (4*g[s16]) + (2*g[s17]) + (2*g[s18]) + (1*g[s19])
    first_credit=4+4+3+3+3+4+2+2+1
    print("your  first semester gpa is {}".format(float(first_semster/first_credit)))
    print("enter your second semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("HS6251 Technical English – II :")
    s12=input("MA6251 Mathematics – II :")
    s13=input("PH6251 Engineering Physics – II :")
    s14=input("CY6251 Engineering Chemistry – II :")
    s15=input("EC6201 Electronic Devices : ")
    s16=input("EE6201 Circuit Theory : ")
    s17=input("GE6262 Physics and Chemistry Laboratory - II : ")
    s18=input("EC6211 Circuits and Devices Laboratory : ")
    second_semster = (4*g[s11]) + (4*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (4*g[s16]) + (1*g[s17]) + (2*g[s18]) 
    second_credit=4+4+3+3+3+4+1+2
    print("your  second semester gpa is {}".format(float(second_semster/second_credit)))
    print("enter your third semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("MA6351 Transforms and Partial Differential Equations :")
    s12=input("EE6352 Electrical Engineering and Instrumentation :")
    s13=input("EC6301 Object Oriented Programming and Data Structures :")
    s14=input("EC6302 Digital Electronics :")
    s15=input("EC6303 Signals and Systems : ")
    s16=input("EC6304 Electronic Circuits- I : ")
    s17=input("EC6311 Analog and Digital Circuits Laboratory : ")
    s18=input("EC6312  OOPS and Data Structures Laboratory : ")
    third_semster = (4*g[s11]) + (4*g[s12]) + (3*g[s13]) + (3*g[s14]) + (4*g[s15]) + (4*g[s16]) + (2*g[s17]) + (2*g[s18]) 
    third_credit=4+4+3+3+4+4+2+2
    print("your  third semester gpa is {}".format(float(third_semster/third_credit)))
    print("enter your forth semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("MA6451 Probability and Random Processes :")
    s12=input("EC6401 Electronic Circuits II :")
    s13=input("EC6402 Communication Theory :")
    s14=input("EC6403 Electromagnetic Fields :")
    s15=input("EC6404 Linear Integrated Circuits : ")
    s16=input("EC6405 Control System Engineering : ")
    s17=input("EC6411 Circuit and Simulation Integrated Laboratory : ")
    s18=input("EC6412 Linear Integrated Circuit Laboratory : ")
    s19=input("EE6461 Electrical Engineering and Control System :")
    fourth_semster = (4*g[s11]) + (3*g[s12]) + (3*g[s13]) + (4*g[s14]) + (3*g[s15]) + (3*g[s16]) + (2*g[s17]) + (2*g[s18]) + (2*g[s19])
    fourth_credit=4+3+3+4+3+3+2+2+2
    print("your  fourth semester gpa is {}".format(float(fourth_semster/fourth_credit)))
    print("enter your fifth semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("EC6501 Digital Communication :")
    s12=input("EC6502  Principles of Digital Signal Processing :")
    s13=input("EC6503 Transmission Lines and Wave Guides :")
    s14=input("GE6351 Environmental Science and Engineering :")
    s15=input("EC6504 Microprocessor and Microcontroller : ")
    s16=input("EC6511 Digital Signal Processing Laboratory : ")
    s17=input("EC6512 Communication System Laboratory : ")
    s18=input("EC6513 Microprocessor and Microcontroller Laboratory : ")
    fifth_semster = (3*g[s11]) + (4*g[s12]) + (4*g[s13]) + (3*g[s14]) + (3*g[s15]) + (2*g[s16]) + (2*g[s17]) + (2*g[s18]) 
    fifth_credit=3+4+4+3+3+2+2+2
    print("your  fifth semester gpa is {}".format(float(fifth_semster/fifth_credit)))
    print("enter your sixth semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("MG6851 Principles of Management :")
    s12=input("CS6303 Computer Architecture :")
    s13=input("CS6551 Computer Networks :")
    s14=input("EC6601 VLSI Design :")
    s15=input("EC6602 Antenna and Wave proPagation : ")
    s16=input("EC2021 Medical Electronics : ")
    s17=input("EC6611 Computer Networks Laboratory : ")
    s18=input("EC6612 VLSI  Design Laboratory : ")
    s19=input("GE6674  Communication and Soft Skills Laboratory : ")
    sixth_semster = (3*g[s11]) + (3*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (3*g[s16]) + (2*g[s17]) + (2*g[s18]) +  (2*g[s19])
    sixth_credit=3+3+3+3+3+3+2+2+2
    print("your sixth semester gpa is {}".format(float(sixth_semster/sixth_credit)))
    print("enter your seventh semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("EC6701RF and Microwave Engineering :")
    s12=input("EC6702 Optical Communication and Networks :")
    s13=input("EC6703 Embedded and Real Time Systems :")
    s14=input("EC6004 Satellite Communication :")
    s15=input("EC6011 Electro Magnetic Interference and Compatibility : ")
    s16=input("EC6016-Opto Electronic Devices : ")
    s17=input("EC6711 Embedded  Laboratory : ")
    s18=input("EC6712 Optical and Microwave Laboratory : ")
    seventh_semster = (3*g[s11]) + (3*g[s12]) + (3*g[s13]) + (3*g[s14]) + (3*g[s15]) + (3*g[s16]) + (2*g[s17]) + (2*g[s18]) 
    seventh_credit=3+3+3+3+3+3+2+2
    print("your  seventh semester gpa is {}".format(float(seventh_semster/seventh_credit)))
    print("enter your eight  semester grade point : ")
    g={'s':10,'S':10,'a':9,'A':9,'b':8,'B':8,'c':7,'C':7,'d':6,'D':6,'E':5,'e':5,'U':0,'u':0}
    s11=input("EC6801 Wireless Communication :")
    s12=input("EC6802 Wireless Networks :")
    s13=input("GE6757 Total Quality Management :")
    s14=input("EC6018 Multimedia Compression and Communication :")
    s15=input("Project Work :")
    eight_semster = (3*g[s11]) + (3*g[s12]) + (3*g[s13]) + (3*g[s14]) + (6*g[s15]) 
    eight_credit=3+3+3+3+6
    print("your  eight semester gpa is {}".format(float(eight_semster/eight_credit)))    
    CGPA= (first_semster+second_semster+third_semster+fourth_semster+fifth_semster+sixth_semster+seventh_semster+eight_semster) / (first_credit+second_credit +third_credit+fourth_credit+fifth_credit+sixth_credit+seventh_credit+eight_credit) 
    print("YOUR OVERALL ECE CGPA is {}".format(float(CGPA)))
    if CGPA >= 8.51 :
        print("your First Class Withdistinction(FWD)")
    elif ((CGPA <= 8.50) and (CGPA >= 6.51)):
        print("your First Class(FC)")
    elif ((CGPA <= 6.50) and (CGPA >= 5.01)):
        print("your second Class(SC)")
    else :
        print("you are not eligible on class please clear the arrear")
    


def subnetmask(x):
    x=str(x)
    xy = [y for y in x.split('.')]
    if len(xy) == 4 :
        if int(xy[0]) <= 126 and int(xy[0]) >= 0 :
            print("subnetmask=255.0.0.0")
        elif int(xy[0]) == 127 :
            print("your ip is loop back address subnetmask=255.0.0.0")
        elif int(xy[0]) <= 191 and int(xy[0]) >= 128 :
            print("subnetmask=255.255.0.0")
        elif int(xy[0]) <= 223 and int(xy[0]) >= 192 :
            print("subnetmask=255.255.255.0")
        else :
            print("your ip is not used in real time and subnetmask=255.255.255.255")
    else :
        print("type you correct ipv4 address ")
    
while True:
    x=raw_input("enter your ip address : ")
    subnetmask(x)
print("you are checking subnetmask on {} times ".format(count))
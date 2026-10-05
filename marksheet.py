sub1 = int(input("enter marks: "))
sub2 = int(input("enter marks: "))
sub3 = int(input("enter marks: "))
sub4 = int(input("enter marks: "))
sub5 = int(input("enter marks: "))

fs=0 
gs=0

if sub1<40:
    fs=fs+1
    gs=gs+(40-sub1)
    
if sub2<40:
    fs=fs+1
    gs=gs+(40-sub2)

if sub3<40:
    fs=fs+1
    gs=gs+(40-sub3)

if sub4<40:
    fs=fs+1
    gs=gs+(40-sub4)

if sub5<40:
    fs=fs+1
    gs=gs+(40-sub5) 

if fs <= 3 and gs <= 7:
    total = sub1 + sub2 + sub3 + sub4 + sub5
    per = total / 5

    print("Passed")
    print("Percentage:", per)

    if per >= 90:
        print("Grade: A")
    elif per >= 75:
        print("Grade: B")
    elif per >= 60:
        print("Grade: C")
    elif per >= 40:
        print("Grade: D")
    else:
        print("Fail")

else:
    print("Failed")
    
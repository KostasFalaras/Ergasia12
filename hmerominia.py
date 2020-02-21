from datetime import date
a = input(" your year")
b = input (" your month")
c = input (" your day")
d = input(" today's year") 
e = input(" today's month")
z = input (" today's day")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
z = int(z)
YourDate = date(a,b,c)
TodayDate = date(d,e,z) #Tha mporousa na parw to TodayDate apto library alla protimisa na to afisw etsi wste na exei kai alles xriseis oxi mono gia tin simerini imerominia
wow = YourDate - TodayDate #mporei na bgei - se prosimo  alla den allazei kati apla deixnei poia imerominia einai megalyteri 
k = wow.days
print (k) #meres pou apexoun 
hours = k*24
print (hours)
seconds = hours*3600
print (seconds)
if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12 :
    print('This month has 31 days')
elif b == 4 or b == 6 or b == 9 or b == 11 :
    print('This month has 30 days')
elif b == 2:

    if a%4 != 0:
        print('This month has 28 days')
    elif a%100 != 0:
        print ('This month has 29 days')
    elif a%400 != 0:
        print('This month has 28 days')
    else:
        print('This month has 29 days')







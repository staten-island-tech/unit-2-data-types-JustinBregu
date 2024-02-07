print('How was our service for you today')
tip_percent = 0
Service_a = input('Bad(0%) , Okay(15%), Good(20%), Great(25%)')
Service = Service_a.lower()
subtotal = float(input("What is your bill? "))
if (Service =='bad'):
    tip_percent = 0
elif (Service == 'okay'):
    tip_percent=15
elif (Service == 'good'):
    tip_percent = 20
elif (Service == 'great'):
    tip_percent = 25

tip = tip_percent*subtotal/100
Total=tip+subtotal
print(Total)


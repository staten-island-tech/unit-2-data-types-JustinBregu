tip_percent=float(input())
print('How was our service for you today')
print('Bad(0%) , Okay(15%), Good(20%), Great(25%)')
Service=(str(input()))
if (Service =='Bad'):
    tip_percent=0
if (Service == 'Okay'):
    tip_percent=15
if (Service == 'Good'):
    tip_percent=20
if (Service == 'Great'):
    tip_percent=25


subtotal=float(input())
def Tip_calculator(tip_percent):
    tip = tip_percent*subtotal/100
    Total=tip+subtotal
    print(Total)
Tip_calculator

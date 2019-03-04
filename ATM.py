#create an algorithm for ATM software which
#will accept a withdraw amount and gives 'Error' as
#an output if the amount is invalid, else gives no. of minimum notes required.
# Notes = 50, 100, 200, 500, 2000
#Write a program to accept a withdraw amount and givees no. of
#minimum notes needed.
# Test cases       |INPUT|    |OUTPUT|
#                   |2531|    |Error|
#                   |3500|    |4|
#                   |1250|    |3| 
#                   |1305|    |Error| 
def atm_output():
    wdraw = int(input('Enter Your Withdraw Amount:$'))
    if wdraw>= 2000:
        print('No. of $2000 note is', wdraw//2000)
        r1 = wdraw%2000    
    if r1>=500 and r1<2000:
        print('No. Of $500 note is',r1//500)
        r2 = r1 % 500
    if r2 >= 200 and r2<500:
        print('No. Of $200 note is', r2 // 200)
        r3 = r2 % 200
    if r3 >= 100 and r3<200:
        print('No. of $100 note is', r3 // 100)
        r4 = r2 % 100
    if r4 >= 50 and r4<100:
        print('No. of $50 note is', r4 // 50)
        r5 = r4 % 50
    if r5 == 0:
        print('Thank You! Have a Nice Day!')
    else:
        print('Amount unable to withdraw=',r5)                

atm_output()
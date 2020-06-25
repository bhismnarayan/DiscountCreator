
discountRegular={'Regular':[
                   {'Lower':0,'Upper':5000,'discount':0},
                   {'Lower':5000,'Upper':10000,'discount':.10},
                   {'Lower':10000,'Upper':10000000,'discount':.20}],
                   'Premium':[
                   {'Lower':0,'Upper':4000,'discount':.10},
                   {'Lower':4000,'Upper':8000,'discount':.15},
                   {'Lower':8000,'Upper':12000,'discount':.20},
                   {'Lower':12000,'Upper':10000000,'discount':.30}]

                }


def CustomerDiscount(currentAmount,customerType):
    Totaldiscount=0
    for i in discountRegular[customerType]:
        if currentAmount>i['Upper']:
            discount=(i['Upper']-i['Lower'])*i['discount']            
            print('discount {0} ',discount)
        else:
            discount=(currentAmount-i['Lower'])*i['discount']
            print('discount',discount)

        Totaldiscount+=discount        
    return Totaldiscount    


currentCustomerType='Premium'#input('Enter Customer type')
customerPurchaseAmount=20000 #int(input('Enter Customer purchase amount'))

currentAmount=customerPurchaseAmount
customerdiscount=CustomerDiscount(currentAmount,currentCustomerType)
    
print('Total Amount to pay{0}',customerPurchaseAmount-customerdiscount)            




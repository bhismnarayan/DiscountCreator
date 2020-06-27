#this dict contain customer type and and discount for different ranges
#if new customer type can be added as dictionary key and and different ranges cound be added.
#In order to make this make this program more modular we can read these values from json file
#wherein customer type and discount

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



def CalculateAmountAfterCustomerDiscount(customerType,currentAmount):
# This function would calculate discount based on customer type and amount

    try:
        Totaldiscount=0
        for i in discountRegular[customerType]:
            if currentAmount>i['Upper']:
                discount=(i['Upper']-i['Lower'])*i['discount']            
            else:
                discount=(currentAmount-i['Lower'])*i['discount']
            Totaldiscount+=discount        
        return currentAmount-Totaldiscount
    
    except Exception as e:
        return e
    



if __name__ == "__main__":
    currentCustomerType='Regular'#''input('Enter Customer type')
    customerPurchaseAmount=15000 #int(input('Enter Customer purchase amount'))
    print('Total Amount to pay{0}',CalculateAmountAfterCustomerDiscount(currentCustomerType,customerPurchaseAmount))            



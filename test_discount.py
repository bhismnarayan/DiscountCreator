import pytest
import DiscountCalculator

#This function would test discount for regular custome
def test_discountRegularCustomer():
    assert DiscountCalculator.CalculateAmountAfterCustomerDiscount('Regular',15000) == 13500,"Should be 135000"

def test_discountPremiumCustomer():
    assert DiscountCalculator.CalculateAmountAfterCustomerDiscount('Premium',20000) == 15800, "Should be 15800"

    

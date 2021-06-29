"""
@Author: Swapnil Bhoyar
@Date: 2021-06-29 23:09:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-29 23:09:00
@Title: Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
"""
import random

class Coupon:
    @staticmethod
    def getCouponNumber(couponCount):
        """
        Description:
            this function calculate random value
        Parameter:
            couponCount: int value
        Return:
            number: int
        """
        number = random.randint(0, couponCount)
        return number

    @staticmethod
    def generateCoupon(couponCount):
        """
        Description:
            this function store distinct value of coupons
        Parameter:
            couponCount: int value
        Return:
            RANDOM_NUMBER_COUNT: int
        """
        couponNumberList = []
        RANDOM_NUMBER_COUNT = 0

        while len(couponNumberList) < couponCount:
            couponNumber = Coupon.getCouponNumber(couponCount)
            if couponNumber not in couponNumberList:
                couponNumberList.append(couponNumber)
            RANDOM_NUMBER_COUNT += 1
        return RANDOM_NUMBER_COUNT

couponCount = int(input("Enter number of coupons to generate:"))
print(Coupon.generateCoupon(couponCount))
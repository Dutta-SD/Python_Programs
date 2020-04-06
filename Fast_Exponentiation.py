# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:41:49 2020

@author: sandip
"""

# =============================================================================
# Algorithm for fast exponentiation (Binary Exponentiation)
# Exponentiation in O( log n ) time
# =============================================================================

def Bin_Expo(a, n):
    if n == 0:
        return 1
    elif n > 0:
        if n & 1:
            return Bin_Expo(a, (n - 1) >> 1) * Bin_Expo(a, (n - 1) >> 1) * a
        else:
            return Bin_Expo(a, n >> 1) * Bin_Expo(a, n >> 1)
        
# =============================================================================
# Algorithm for GCD of two integers
# GCD(a, b) calculates the Gcd of 2 numbers in O( log { min(a, b) } ) time.
# Euclids algorithm is used to calculate the GCD of the algorithm
# =============================================================================
            
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
# =============================================================================
# Driver Functions
# =============================================================================
    
print(Bin_Expo(3, 20))
print(GCD(10, 5))
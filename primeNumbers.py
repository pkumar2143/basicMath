from math import *


def primeQ(n):
    '''Function: To check whether a number is prime.
        Input: A positive integer, n
        Output: Boolean (True, if n is prime; False if not).'''
    # Cover the fundamental primes
    if n == 1 or n == 2 or n == 5:
        return True

    # if last digit not 1, 3, 7, or 9, then not prime
    lastdig = n % 10
    if n == 0 or ((lastdig != 1) and (lastdig != 3) and (lastdig != 7) and (lastdig != 9)):
        return False

    # check divisibility by any odd number from 1 to sqrt(n)
    for i in range(3, floor(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

def primeList(n):
    '''Function: To list of all prime numbers up to a certain point, n.
        Input: A positive integer, n.
        Output: A list of all prime numbers from 1 to n.'''
    list0 = []
    for i in range(1, n+1):
        if primeQ(i):
            list0.append(i)

    return list0

def nextPrime(n):
    '''Function: To find the next prime number after a chosen point, n.
        Input: A positive integer n.
        Output: The next prime number after n.'''
    curr = n+1
    while primeQ(curr) == False:
        curr += 1

    return curr

def primeDensity(n):
    '''Function: To compute the density of all prime numbers from 1 to a chosen point, n.
        (Or the probability of a number between 1 and n being prime.)
        Input: A positive integer n.
        Output: A real number between 0 and 1. '''
    return len(primeList(n))/n

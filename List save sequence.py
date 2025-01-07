# Databricks notebook source
a=[1,2,3]
b=a
a+=[4,5]
print (a)
print(b)
# you thought a will be different after the operation. but that's the caveat here. a got updated and reflected that acress board

# -*- coding: utf-8 -*-
"""WK1_IP_23/07/21_Ryan_Mburu_Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14mf03ZV7RwJCBIezs8eLWy4cJZX3p73X
"""

#Python IP WK1

#Conversion of Pounds to Kgs

#User to progress his/her weight loss/gain
# User to input 2 values (in pounds)

weight19 = int(input("Enter your 2019's weight :"))
weight21 = int(input("Enter this year's weight : "))

#sum of the two year's weights
total_weight = (weight19 + weight21)

print ("Your total weight between the two years is : " + str(total_weight))

#average weight between the two years
avg_weight = (total_weight / 2)

print ("The average weight is : "  + str(avg_weight))

#The weight difference
weight_diff = (weight19 - weight21)

print ("The weight difference is :" +str(weight_diff))

#The quotient of the two weights
weight_div = (weight19 / weight21)

print ("The quotient of the two weights is : " +str(weight_div))

#determining whether any of the given weights are even or odd

if (weight19 % 2) == 0:
  print("The first number is even")
else:
  print("The first number is odd")

if (weight21 % 2) == 0:
  print("The second number is even")
else:
  print("The second number is odd")


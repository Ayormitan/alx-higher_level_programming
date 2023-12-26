#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I leart C!"
lenght, first = multiple_returns(sentence)
print("lenght: {:d} - first character: {}".format(lenght, first))

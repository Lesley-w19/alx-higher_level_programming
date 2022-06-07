#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_end = ()
    if len(sentence) == 0:
        tuple_end = len(sentence), None
        return tuple_end
    else:
        tuple_end = len(sentence), sentence[0]
        return tuple_end    

from collections import defaultdict
def DNA_strand(dna):
    # code here
    dict_ = {"A":"T", "T":"A", "G":"C", "C":"G"}
    res = ''.join([dict_[i] for i in dna])  
    return res
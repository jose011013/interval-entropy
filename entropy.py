import pandas as pd
import numpy as np
from itertools import product

class SymbolicInterval:

    def __init__(self, nums):

        self.min = np.min(nums)
        self.max = np.max(nums)
        self.len = self.max-self.min

        if self.len > 0:
            self.pdf = 1/self.len
        else:
            self.pdf = 0

    def __str__(self):
        return f"[{self.min} : {self.max}]"
    
    def isSubset(self, interval: SymbolicInterval) -> bool:
        return (self.min >= interval.min) & (self.max <= interval.max)

class SymbolicMultivalued:

    def __init__(self, vals, modal=True):

        if modal:
            self.hist = {}
            for val in vals:
                if val in self.hist.keys():
                    self.hist[val] += 1
                else:
                    self.hist[val] = 1
        else:
            self.hist = {val: 1 for val in vals}

        self.n = sum(self.hist.values())

    def __str__(self):
        return str(self.hist)
    
    def pdf(self, key):
        if key in self.hist.keys():
            return self.hist[key]/self.n
        else:
            return 0

# (Hu, On statistics, probability, and entropy of interval-valued datasets)
def intervalPDF(X: pd.Series):

    nondegen_len = sum([x.min != x.max for x in X])

    c = list(set(([x.min for x in X] + [x.max for x in X])))
    c.sort()

    segs = {(c[i-1], c[i]): 0 for i in range(1,len(c))}

    for x in X:
        for seg in segs:
            if (seg[0] >= x.min) & (seg[1] <= x.max):
                segs[seg] += x.pdf
    
    for seg in segs:
        segs[seg] = segs[seg]/nondegen_len * (seg[1]-seg[0])

    return segs

def intervalEntropy(pmf: dict, delta=0.01):
    return -sum([p*np.log(delta/(c[1]-c[0])) if p>0 else 0 for c, p in pmf.items()])

def symbolicTable(df: pd.DataFrame, concepts=list) -> pd.DataFrame:

    sym_df = df.groupby(
        concepts
        ).agg(
            lambda x: SymbolicMultivalued(x) if x.dtype=='object' else SymbolicInterval(x)
            )
    
    return sym_df

# test

data = pd.read_csv("accidents_2017.csv")
data = data.drop(columns="Id")

num_vars = ["Day","Hour","Mild injuries","Serious injuries",
            "Victims", "Vehicles involved","Longitude",
            "Latitude"]
str_vars = [item for item in data.columns if item not in num_vars]

def findBestSymTable(data, concepts, num_vars, depth=2):

    combs = list(product(concepts, repeat=depth))
    combs = [list(comb) for comb in combs]

    lowest_entropy = None
    best_sym_table = None

    for comb in combs:
        sym_data = symbolicTable(data, comb)
        entropy = sum([intervalEntropy(intervalPDF(sym_data[x])) for x in num_vars])
        print(f"{comb}: {entropy}")
        if (lowest_entropy is None) or (entropy < lowest_entropy):
            lowest_entropy = entropy
            best_sym_table = sym_data
    
    return best_sym_table

print(findBestSymTable(data, str_vars, num_vars))


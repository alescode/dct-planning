#! /usr/bin/env python
import os
from dirs_all import *

problems = ["qbf"]

if __name__ == "__main__":

    for i in qbf_0:
        for j in qbf_1:
            for c in qbf_2:
                if int(i[:-1]) + int(j[:-1]) > int(c[:-1]):
                    continue
                os.system("mkdir -p solutions-soforall/qbfae/" + "/".join([i, j, c]))
                os.system("mkdir -p solutions-soforall/nqbfae/" + "/".join([j[:-1] + "a", ji[:-1] + "e", c]))
                os.system("mkdir -p solutions-soforall/qbfea/" + "/".join([j, i, c]))

        
        #QBF 3 EAE 
        
    for e1 in qbf3_e0:
        for a1 in qbf3_a0:
            for e2 in qbf3_e1:
                for c in qbf_2:
                    if int(a1[:-1]) + int(e1[:-1]) + int(e2[:-1]) > int(c[:-1]):
                        continue
                    os.system("mkdir -p solutions-soforall/qbf3eae/" + "/".join([e1, a1, e2, c]))
            
            #QBF 3 AEA
            
    for a1 in qbf3_a2:
        for e1 in qbf3_e2:
            for a2 in qbf3_a2:
                for c in qbf_2:
                    if int(a1[:-1]) + int(e1[:-1]) + int(a2[:-1]) > int(c[:-1]):
                        continue
                    os.system("mkdir -p solutions-soforall/qbf3aea/" + "/".join([a1, e1, a2, c]))




        
    print "Created solution directories"

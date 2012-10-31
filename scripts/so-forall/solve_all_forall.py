#! /usr/bin/env python
RUN = False
RUN = True

import os, re, sys, math

problems = "qbf3eae|qbf3aea|qbfae|qbfea"
limits = "ulimit -t 5400; ulimit -m 3000;"
plannerCommand = "planners/m/M"
output = ">"

def getDomain(problem):
    return re.search(problems, problem).group(0)

def qbfaeBounds(problem):
    problem_info = problem.split("_")
    n_soforall = int(problem_info[1][:-1])
    n_clauses = int(problem_info[3][:-1])
    # return (pow(2,n_soforall)*(n_clauses + 10) + 1, pow(2,n_soforall)*(n_clauses + 11) + 1)
    # return (int(math.floor(pow(2,n_soforall)*(n_clauses + 10) + 1 + (pow(2,n_soforall)*1/2))), pow(2,n_soforall)*(n_clauses + 11) + 1)
    return (pow(2,n_soforall)*(n_clauses + 11) + 1, pow(2,n_soforall)*(n_clauses + 11) + 1)
    
def qbfeaeBounds(problem):
    # print problem
    
    problem_info = problem.split("_")
    n_soforall = int(problem_info[2][:-1])
    n_clauses = int(problem_info[4][:-1])
    # print "N_for: " + str(n_soforall) + "N_clau: " + str(n_clauses)
    
    # return (pow(2,n_soforall)*(n_clauses + 10) + 1, pow(2,n_soforall)*(n_clauses + 11) + 1)
    # return (int(math.floor(pow(2,n_soforall)*(n_clauses + 10) + 1 + (pow(2,n_soforall)*1/2))), pow(2,n_soforall)*(n_clauses + 11) + 1)
    return (pow(2,n_soforall)*(n_clauses + 11) + 1 + 3, pow(2,n_soforall)*(n_clauses + 11) + 1 + 3)

def qbfeaBounds(problem):
    problem_info = problem.split("_")
    n_soforall = int(problem_info[2][:-1])
    n_clauses = int(problem_info[3][:-1])
    return (pow(2,n_soforall)*(n_clauses + 8) + 3, pow(2,n_soforall)*(n_clauses + 8) + 4)
    
def qbfaeaBounds(problem):
    # print problem
    
    problem_info = problem.split("_")
    n_soforall_2 = int(problem_info[1][:-1])
    n_soforall_1 = int(problem_info[3][:-1])
    n_clauses = int(problem_info[4][:-1])
    # print "N_for1: " + str(n_soforall_1) + "N_for2: " + str(n_soforall_2) + "N_clau: " + str(n_clauses)
    # return (pow(2,n_soforall_2)*(pow(2,n_soforall_1)*(n_clauses + 8) + 4 )+ 1, pow(2,n_soforall_2)*(pow(2,n_soforall_1)*(n_clauses + 8) + 5) + 1)
    
    return (pow(2,n_soforall_2)*(pow(2,n_soforall_1)*(n_clauses + 8) + 5 )+ 1, pow(2,n_soforall_2)*(pow(2,n_soforall_1)*(n_clauses + 8) + 5) + 1)

def stepSize(bounds):
    return "-S 1" # fixed for now, try every step

def showBounds(bounds):
    return "-F " + str(bounds[0]) + " -T " + str(bounds[1])

def parallelInstances(bounds):
    return "-A 1"
    # n = bounds[1] - bounds[0]
    # if n > 3:
    #     return "-A 4"
    # else:
    #     return "-A " + str(n+1)

def solveProblems(list, file = None):   
    # print list
    submit_file_M = open("condor_submits_M.submit", "w")
    submit_file_Mp = open("condor_submits_Mp.submit", "w")
    submit_file_Lama = open("condor_submits_Lama.submit", "w")
    
    submit_file_M.write("executable = /home-users/nlipo/blai/Aldo/dct-planning/planners/m/M\n")
    submit_file_Mp.write("executable = /home-users/nlipo/blai/Aldo/dct-planning/planners/m/Mp\n")
    submit_file_Lama.write("executable = /home-users/nlipo/seq-sat-lama-2011/src/plan-ipc\n")
    
    specification = "universe = vanilla\n" +\
                    "Requirements = Memory >= 1024\n"+\
                    "InitialDir = /home-users/nlipo/blai/Aldo\n"
    
    submit_file_M.write(specification)
    submit_file_Mp.write(specification)
    submit_file_Lama.write(specification)
    
    
    for problemFile in list:
        domain = getDomain(problemFile)
        domainFile = "problems-soforall/" + domain + "/" + domain + ".pddl"
        nameParts = problemFile.rpartition("/")
        solutionFile = "solutions-soforall/" + nameParts[0].partition("/")[2] + "/" + \
                       nameParts[2].rpartition(".")[0]
    
        if domain == "qbfae":
            bounds = qbfaeBounds(problemFile)
        elif domain == "qbfea":         
            bounds = qbfeaBounds(problemFile)
        elif domain == "qbf3eae":
            bounds = qbfeaeBounds(problemFile)
        elif domain == "qbf3aea":
            bounds = qbfaeaBounds(problemFile)
        else:
            raise ValueError
        
        experiment = "# Experiment " + problemFile + "\n\n" +\
                     "should_transfer_files = YES\n" +\
                     "when_to_transfer_output = ON_EXIT \n" +\
                     "transfer_input_files = \\\n" +\
                     "/home-users/nlipo/blai/Aldo/dct-planning/" + problemFile + ",\\\n"+\
                     "/home-users/nlipo/blai/Aldo/dct-planning/" + domainFile
                     
        experiment_m = experiment + "\n\n"
        experiment_lama = experiment + ",\\\n/home-users/nlipo/seq-sat-lama-2011/src/\n\n" 

        output = "output = /home-users/nlipo/blai/Aldo/dct-planning/" +\
                    solutionFile
    
        arguments_m = "arguments = -Q -t 5400 " + " ".join([showBounds(bounds), \
                      stepSize(bounds), parallelInstances(bounds),
                      domain + ".pddl", nameParts[2], "\n"])
                      
        arguments_lama = "arguments = seq-sat-lama-2011 " + domain + ".pddl " + nameParts[2] + " " + nameParts[2].rpartition(".")[0] + ".outlama\n" 
        error = "error = /home-users/nlipo/blai/Aldo/dct-planning/" +\
                solutionFile + ".error"
        end  = "queue\n\n"
        
        submit_file_M.write(experiment_m + output + ".outm\n" + arguments_m + error + "m\n" + end)
        submit_file_Mp.write(experiment_m + output + ".outmp\n" + arguments_m + error + "mp\n" + end)
        submit_file_Lama.write(experiment_lama + output + ".outlama\n" + arguments_lama + error + "lama\n" + end)
    submit_file_M.close()
    submit_file_Mp.close()
    submit_file_Lama.close()
    
        
        
find = """find problems-soforall | grep .pddl | grep -v qbfae.pddl | grep -v qbfea.pddl | grep -v qbf3aea.pddl | grep -v qbf3eae.pddl"""

if __name__ == "__main__":
    # this should be split in two processes! fork
    pipe = os.popen(find)
    p0_fileList = []
    for index, file in enumerate(pipe):
        p0_fileList.append(file.rstrip())
    pipe.close()
    solveProblems(p0_fileList)


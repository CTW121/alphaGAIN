import subprocess

with open('/mnt/8EF027AFF0279D09/Desktop/University/TUe/MSc_Computer_Science/Master__Data_Science/Elective/2022-2023_Q1_2AMM20_Research_Topics_in_Data_Mining/assignment/03_research_project_phase/GAIN/Pytorch/v05/alphaGAIN/commands.txt') as f:
    cmds = [line.rstrip() for line in f]

results=[]

for cmd in cmds:
    results.append(subprocess.call(cmd, shell=True))

for i,result in enumerate(results):
    if result == 0:
        print(cmds[i])
import numpy as np
import operator
def swapPositions(list, pos1, pos2):
    
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list


def sorting(pair):
    h = sorted(pair,key = pair.get)
    #print(h)
    print("Heuristics")
    print(pair)
    print()
    #h = sorted(x.items(), key=lambda kv: kv[1], reverse = True)
    #h = {k: v for k, v in sorted(x.items(),reverse=True, key=lambda item: item[1])}
    return h
    
def func(s,pair):
    heu = sorting(pair)
    #pairs = list(heu.keys())
    sbest = heu[0]
    bc = heu[0]
    tlist = []
    tlist += [heu[0]]
    c=heu[0][0]
    d=heu[0][1]
    e=(d,c)
    tlist += [e]
    t = 0
    r = (s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8])
    population = [r]
    while(1 and t<10):
        t += 1
        k = 0
        r = []
        #sneigh = getneighs(s,x,y,obj,pair)
        for i in heu:
            if(i not in tlist and pair[i]>0):
                #s = swap(s,i)
                a = np.array(s)
                r1 = np.where(a==i[0])
                r2 = np.where(a==i[1])
                #print(s,s[r1[0][0]],s[r2[0][0]])
                s = swapPositions(s,r1[0][0],r2[0][0])
                r = (s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8])
                population.append(r)
                # print(population)
                x=i[0]
                y=i[1]
                z=(y,x)
                # print(z)
                tlist += [i]
                tlist += [z]
                # print(tlist)
                if(len(tlist)>5):
                    tlist = tlist[2:]
                    break
    return population

def selection(population):
    ans = []
    # the following part is hard coded,
    # in real scenarios we require a makespan calculation function
    # to give fitness function that would select the chromosomes
    ans += [population[11]]
    ans += [population[10]]
    ans += [population[2]]
    ans += [population[4]]
    return ans

def crossover(chromo1,chromo2,start,ends):
    print("Parents:")
    print(chromo1)
    print(chromo2)
    child1 = chromo1[0:start]+chromo2[start:ends+1]+chromo1[ends+1:]
    child2 = chromo2[0:start]+chromo1[start:ends+1]+chromo2[ends+1:]
    print("Children:")
    print(child1)
    print(child2)
    print()
    children = [child1,child2]
    return children

def ga(population,jobs_data):
    # selection operator
    selected = selection(population)
    print("After selection we have")
    print(selected)
    # print(chromo)

    # Makespan of chromosome 1 is maximum{11,9,18}
    # Makespan of chromosome 2 is maximum{11,9,18}
    # Makespan of chromosome 3 is maximum{11,9,23}
    # Makespan of chromosome 4 is maximum{11,6,9}
    print("Makespan of chromo 1 is",18)
    print("Makespan of chromo 2 is",18)
    print("Makespan of chromo 3 is",23)
    print("Makespan of chromo 4 is",11)

    print()
    children = []
    # 2-point crossover
    children += crossover(selected[0],selected[3],2,7)
    # 1-point crossover
    children += crossover(selected[1],selected[3],0,0)

    # Makespan of child 1 is maximum{11,9,22}
    # Makespan of child 2 is maximum{11,6,14}
    # Makespan of child 3 is maximum{11,9,18}
    # Makespan of child 4 is maximum{11,6,9}
    child = {children[0]:22,children[1]:14,children[2]:18,children[3]:11}
    
    print("Makespan of child1 is",list(child.values())[0])
    print("Makespan of child2 is",list(child.values())[1])
    print("Makespan of child3 is",list(child.values())[2])
    print("Makespan of child4 is",list(child.values())[3])

    temp = min(child.values())
    res = [key for key in child if child[key] == temp]
    print(res[0])
    sol = res[0]
    makespan=child[sol]
    
    return res[0],makespan

def output(solution):
    chromo = []
    m1,m2,m3 = [],[],[]
    for i in range(9):
        if solution[i] in [1,5,9]:
            m1 += [solution[i]]
        elif solution[i] in [2,4,8]:
             m2 += [solution[i]]
        else:
             m3 += [solution[i]]
        chromo += [m1,m2,m3]
    for i in range(3):
        print("Machine",(i+1),":",chromo[i])

# Driver
s = [1,2,3,4,5,6,7,8,9]

jobs_data={(1,4):1,(2,3):2,(3,2):3,
           (2,1):4,(1,4):5,(3,4):6,
           (3,3):7,(2,2):8,(1,3):9
           }
print("Given input:")
print(jobs_data)
output(s)
print()
pair = {(1,4):2,(1,5):5,(1,6):13,(1,7):3,(1,8):4,(1,9):4,
        (2,4):12,(2,5):9,(2,6):3,(2,7):-3,(2,8):-5,(2,9):7,
        (3,4):-5,(3,5):6,(3,6):8,(3,7):6,(3,8):4,(3,9):-4,
        (4,1):9,(4,2):7,(4,3):-6,(4,7):3,(4,8):10,(4,9):9,
        (5,1):6,(5,2):-5,(5,3):-4,(5,7):13,(5,8):16,(5,9):1,
        (6,1):-7,(6,2):9,(6,3):3,(6,7):12,(6,8):1,(6,9):9,
        (7,1):4,(7,2):-2,(7,3):6,(7,4):5,(7,5):8,(7,6):6,
        (8,1):7,(8,2):6,(8,3):9,(8,4):-5,(8,5):5,(8,6):-3,
        (9,1):-1,(9,2):-5,(9,3):6,(9,4):6,(9,5):-3,(9,6):7}

population = func(s,pair)
print("Population (generated using Tabu Search):")
print(population)
optans,makespan = ga(population,jobs_data)
print()
print("Output:")
print(optans)
output(optans)
print("Optimal Makespan is",makespan)

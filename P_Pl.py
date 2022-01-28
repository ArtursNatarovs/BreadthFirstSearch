import csv
with open('input.txt') as f:
    lines = f.readlines()

#lines.append("15 1 16\n")#debug Lines
#lines.append("16 1 15\n")#debug Lines
lines

class Virsotne:
    numurs=""
    iezime=""
    source=""
    numursPecKartas=""
    neighbours=[]

    def __init__(self, numurs, neighbours):
        self.numurs = numurs
        self.neighbours = neighbours

counter=1
forest=[]
grafsDict={}
virsotnes=[]
first=int(lines[1].split()[0])
#first #debug Lines
#lines #debug Lines

#counter=1 #debug Lines
#grafsDict={} #debug Lines
#for line in lines[1:]: #debug Lines
    #grafs.append(Virsotne(int(line.split()[0]),[int(e) for e in line.split()[2:]])) #debug Lines

for line in lines[1:]:
    grafsDict[int(line.split()[0])]=Virsotne(int(line.split()[0]),[int(e) for e in line.split()[2:]])

#virsotnes=list(grafsDict.keys()) #debug Lines

#splits graph into components
congr=[]
for i in range(1,len(grafsDict)+1):
    congr.append(grafsDict[i].neighbours)
    congr[i-1].append(grafsDict[i].numurs)
#congr

while congr !=[]:
    if forest==[]:
        forest.append(congr.pop(0))

    for i in forest:
        for k in congr:
            if any(item in i for item in k):
                i.extend(k)
                congr.pop(congr.index(k))
                break
            else:
                forest.append(k)
                congr.pop(congr.index(k))
                break


for i in range(0,len(forest)):
    forest[i]=(list(set(forest[i])))
for i in range(0,len(forest)):
    forest[i].sort()


for line in lines[1:]:
    grafsDict[int(line.split()[0])]=Virsotne(int(line.split()[0]),[int(e) for e in line.split()[2:]])


forest[0].remove(first)
forest[0].insert(0,first)

def parlase2(graph, verticesToSee, verticesLeft, mark, parent):
    print("New loop ","toSee: ",verticesToSee," mark: ",mark," parent: ",parent)
    global counter

    newVerToSee=[]
    if verticesLeft==[]:
        return
    else:
        for vert in verticesToSee:
            if graph[vert].iezime=="":
                graph[vert].iezime=mark
                graph[vert].numursPecKartas = counter
                counter += 1
            if vert in verticesLeft:
                verticesLeft.remove(vert)
            for neighbour in graph[vert].neighbours:
                if neighbour in verticesLeft and graph[neighbour].source=="":
                    graph[neighbour].source=vert
                    newVerToSee.append(neighbour)
    newVerToSee.sort()  #debug Lines
    parlase2(graph, newVerToSee, verticesLeft, mark+1, vert)


for i in range(0,len(forest)):
    virsotnes2=forest[i].copy()
    print("\n")
    print("Koka[",i+1,"] virsotnes: ",virsotnes2)
    print("\n")
    if i==0:
        iezime=0
        parlase2(grafsDict, [first], virsotnes2, iezime, "s")
    else:
        iezime=0
        parlase2(grafsDict, [virsotnes2[0]], virsotnes2, iezime, "s")



header = ['Virsotne', 'Iezime', 'Atnaca_no', 'Nr.P.K.']


with open('output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    # write the data
    for i in range(1,len(grafsDict)+1):
        writer.writerow([grafsDict[i].numurs,grafsDict[i].iezime,grafsDict[i].source,grafsDict[i].numursPecKartas])

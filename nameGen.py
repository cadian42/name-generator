import random
from argparse import ArgumentParser


class nameGen(object):

    def __init__(self, fileName, blockSize):
            #on lit tout les noms du fichier
            with open(fileName) as f:
                self.listOfName = f.readlines()
            
            #on decoupe les noms en block de taille 'block'
            for name in self.listOfName:
                nameCopy = name
                newName = []

                while len(name) > blockSize:
                    newName.append(name[:blockSize])
                    name = name[blockSize:]

                #on ajoute le reste du mot si necessaire
                if len(name) > 1:
                    newName.append(name[:-1])

                self.listOfName[self.listOfName.index(nameCopy)] = newName

            self.matrix = {'begin':{}} #matrice temporaire pour la creation du finalArray
            self.finalArray = [] #tableau final a partir duquel on peut generer de nouveaux noms

    def generateMatrix(self):
        for name in self.listOfName:

            #on regarde la premiere lettre
            if name[0] not in self.matrix['begin']:
                self.matrix['begin'][name[0]] = 1.
            else:
                self.matrix['begin'][name[0]] += 1

            #on regarde les lettres du mot
            for i in range(0,len(name)-1):
                if name[i] not in self.matrix:
                    self.matrix[name[i]] = {name[i+1]:1}
                else:
                    if name[i+1] not in self.matrix[name[i]]:
                        self.matrix[name[i]][name[i+1]] = 1.
                    else:
                        self.matrix[name[i]][name[i+1]] += 1
        
            #on regarde la derniere lettre
            end = len(name)-1
            if name[end] not in self.matrix:
                self.matrix[name[end]] = {'end':1}
            else:
                if 'end' not in self.matrix[name[end]]:
                    self.matrix[name[end]]['end'] = 1.
                else:
                    self.matrix[name[end]]['end'] += 1
            
        #on convertit notre dictionnaire en list of list pour preparer le tirage au sort
        for value in self.matrix.iteritems():
            tempArray = []

            #on calcule la somme des valeurs pour trouver le pourcentage
            sum = 0
            for v in value[1].itervalues():
                sum += v

            #on ajoute les pourcentages cumulees
            sumOfProba = 0
            for v in value[1].iteritems():
                sumOfProba += v[1]/sum
                tempArray.append((v[0],sumOfProba))

            self.finalArray.append((value[0], tempArray))


    def generateName(self, maxLenghtOfName):
        currentLetter = 'begin'
        name = ""

        for i in range(maxLenghtOfName):
            x = random.random()

            #on recherce la lettre suivante
            for l in self.finalArray:
                if l[0] == currentLetter:
                    for l2 in l[1]:
                        if l2[1] > x:
                            nextLetter = l2[0]
                            break
            
            if nextLetter == 'end':
                break

            name += nextLetter 
            currentLetter = nextLetter

        return name
        

def main():

    parser = ArgumentParser()

    parser.add_argument("-n", action="store", dest="numberOfName", default=1)
    parser.add_argument("-min", action="store", dest="minLetters", default=5)
    parser.add_argument("-max", action="store", dest="maxLetters", default=15)
    parser.add_argument("-b", action="store", dest="blockSize", default=1)
    parser.add_argument("-f", action="store", dest="fileName", default="nameList.txt")

    args = parser.parse_args()

    myNameGen = nameGen(args.fileName, int(args.blockSize))
    myNameGen.generateMatrix()
    for i in range(int(args.numberOfName)):
        correctName = False
        while not correctName:
            name = myNameGen.generateName(int(args.maxLetters))
            if len(name) > int(args.minLetters):
                correctName = True
        print name

if __name__ == '__main__':
    main()

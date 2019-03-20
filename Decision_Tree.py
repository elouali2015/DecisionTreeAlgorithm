
#A decisionTree to progress in the reigh and left to get all possible combinaisions  
def DescisionTree(Tree,Maxvalue):
    if Tree==[] or Maxvalue==0:  

        result=(0,())

    elif Tree[0].getcost()>Maxvalue:
        result=(Tree[1:,],Tree[0].getcost())
    else:
        nextitem=Tree[0]
        #explore left 
        withval,withtotake = DescisionTree(Tree[1:],Maxvalue - nextitem.getcost())

        withval=withval+nextitem.getvalue() 
        #explore the other

        withoutval,withouttake=DescisionTree(Tree[1:],Maxvalue)

        if withval>withoutval:
            result=(withval,(withtotake+(nextitem,)))
        else:
            result=(withoutval,withouttake)

    return result
        


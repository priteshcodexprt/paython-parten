
class vector:
        def __init__ (self,vec):
            self.vec=vec

        def __str__(self) :
            str1=" "
            index=0
            for i in self.vec:
                str1+= f" {i}a{index} +"
                index +=1
            return str1 [:-1]

        def __add__ (self,vec2):
            newList=[]
            for i in range (len(self.vec)):
                newList.append(self.vac[i]+vec2.vec)
            return vector(newList)

v1=vector([1,4])
v2=vector([1,6])
print(v1+v2)
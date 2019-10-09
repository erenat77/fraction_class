class Fraction:
    def __init__(self,top=0,bottom=1):
         #denominator can not be zero
         if bottom==0:
                raise ZeroDivisionError("Den. can not be zero")
         if top == 0:
             self.num = 0
             self.den = 1
         else:
            #Determine regarding the sign of the numbers
            if (not isinstance(top,int) or not isinstance(bottom,int)):	
                raise TypeError("The numerator and denominator must be integers.")
            else:
                if (top<0 and bottom>0) or (top>0 and bottom<0):
                    sign=-1
                else:
                    sign=1
         #smallest fraction calculation
         a=abs(top)
         b=abs(bottom)
         while a%b !=0:
                tempA=a
                tempB=b
                a = tempB
                b = tempA % tempB
         self.num = abs(top)// b *sign
         self.den = abs(bottom)//b
    def __str__(self):
         return str(self.num)+"/"+str(self.den)

    def show(self):
         print(self.num,"/",self.den)

    def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)
        
    #subtract a fraction with another fraction
    def __sub__(self,otherfraction):
         newnum = self.num*otherfraction.den - self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)
    
    #multiply with another fraction
    def __mul__(self,otherfraction):
        return Fraction(self.num*otherfraction.num,self.den*otherfraction.den)

    def __eq__(self, otherfraction):
         firstnum = self.num * otherfraction.den
         secondnum = otherfraction.num * self.den
         return firstnum == secondnum
    
    # not equal operation
    def __ne__(self, otherfraction):
         return not self == otherfraction
    
    #pull denominator number alone
    def getDen(self):
        return str(self.den)
    
    def getNum(self):
        return str(self.num)
    #less or equal
    def __le__(self, other):
         return not other<self
    #less than    
    def __lt__(self, other):
         return ((self.num/self.num)<=(self.num/self.num))
    #greater than    
    def __gt__(self, other):
         return ((self.num/self.num)>(self.num/self.num))
    #greater or equal
    def __ge__(self, other):
         return ((self.num/self.num)>=(self.num/self.num))
    
    #floating show
    def __float__(self):
        return self.num/self.den
    
    def __repr__(self):
        #get a string representation of the fraction
        return str(str(self.num) + "/" +(str.den))

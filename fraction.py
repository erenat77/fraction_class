class Fraction:
  def __init__(self,top,bottom):
        self.num = top
        self.den = bottom  
        
  def __add__(self,otherfraction):
     newnum = self.num*otherfraction.den + self.den*otherfraction.num
     newden = self.den * otherfraction.den
     return Fraction(newnum,newden)

  def __str__(self):
    return str(self.num)+"/"+str(self.den)
    
  def show(self):
    print(self.num,"/",self.den)

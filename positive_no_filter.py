ls=[1,2,5,9,10,-56,-23]
lst=[]
def positive_list():
  for i in range(0,len(ls)):
   if(ls[i]>0):
     lst.append(ls[i])
  return lst;
print(positive_list())

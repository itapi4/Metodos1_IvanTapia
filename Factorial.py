def factorial(n:int)->int:
  res=1
  if n<0:return('Digite un numero positivo')
  for i in range(1,n+1):
    res=res*i
  return(int(res))

def permutacion(n:int,r:int)->int:
  res=factorial(n)//factorial(n-r)
  return(res)

def combinacion(n:int,r:int)->int:
  res=permutacion(n,r)//factorial(r)
  return(res)
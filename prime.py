prime<-function(n){
  if (n<=1)return("It is not prime")
  for (i in 2:sqrt(n)){
    if(n%%i==0)return("It is not prime")
  }
  return("It is prime")
}
prime(7)

factorial<-function(n){
  result<-1
  for (i in 1:n){
    result<-result*i
  }
  return(result)
}
factorial(5)

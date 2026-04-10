power<-function(n,p){
  result<-1
  for (i in 1:p){
    result<-result*n
  }
  return(result)
}
power(2,3)


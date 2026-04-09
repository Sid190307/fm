f1 <- expression(3*x^5-5*x^3)
f1

diff<-D(f1,'x')
diff

ddiff<-D(diff,'x')
ddiff

critical_points<-c(-1,0,1)

f<-function(x) (3*(5*(4*x^3)) - 5*(3*(2*x)))

critical_values<-sapply(critical_points,f) 
fun<-function(x) {3*x^5-5*x^3}

curve(fun, xlim=c(2,-2), ylim=c(-4,4), xlab="x", ylab="f(x)",main="Plot of 3x^5 - 5x^3")

points(critical_points, fun(critical_points), col='red',pch=19)

for(i in 1:length(critical_points)){
  point<-critical_points[i]
  value<-critical_values[i]
  
  label<-if(value>0){
    "relatie minimum"
  } else if(value<0){
    "relative maximum"
  } else{
    "Inconclusive"
  }
  cat("At x=",point,"=>f''(x)=",value, "=>",label,"\n")
  text(point,fun(point),labels = label, pos=4, cex=0.8, col="blue")
}

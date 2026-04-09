f1<-expression(2*x^3-15*x^2+36*x)
f1

dif<-D(f1,'x')
diff

polyroot(c(36,30,6))

fun<-function(x)(2*x^3-15*x^2+36*x)

f1<-fun(1)
f2<-fun(2)
f3<-fun(3)
f4<-fun(4)

cat("f1(1)=",f1,"\n")
cat("f2(2)=",f2,"\n")
cat("f3(3)=",f3,"\n")
cat("f4(4)=",f4,"\n")

f<-function(x){
  2*x^3-15*x^2+36*x
}

points_x<-c(1,2,3,4)
values<-c(f(1),f(2),f(3),f(4))

min_value<-min(values)
max_value<-max(values)
min_point<-points_x[which(values == min_value)]
max_point<-points_x[which(values == max_value)]

plot(seq(0, 6,by = 0.1), sapply(seq(0, 6,by = 0.1), f), type ="l",col="blue",
     lwd=2,xlab="x",ylab="f(x)",main="Plot of f(x)=2x^3-15x^2+36x")

points(points_x,values,col="red",pch=19)

text(min_point,max_value,labels=paste("Min=",min_value),pos=3,col="green",cex=0.8)
text(max_point,max_value,labels=paste("Max=",max_value),pos=3,col="purple",cex=0.8)

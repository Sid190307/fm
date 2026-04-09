f<-expression((x^2 * y^3) + (x^4 * y))
f

x<-as.numeric(readline(prompt = "Enter value for x: "))
y<-as.numeric(readline(prompt = "Enter value for y: "))

difx<-D(f,'x')
difx
cat("fx(",x,",",y,") =", eval(difx), "\n")

dify<-D(f,'y')
dify
cat("fx(",x,",",y,") =", eval(dify), "\n")

ddifx<-D(difx,'x')
ddifx
cat("fx(",x,",",y,") =", eval(ddifx), "\n")

ddify<-D(dify,'y')
ddify
cat("fx(",x,",",y,") =", eval(ddify), "\n")

difxy<-D(difx,'y')
difxy
cat("fx(",x,",",y,") =", eval(difxy), "\n")

difyx<-D(dify,'x')
difyx
cat("fx(",x,",",y,") =", eval(difyx), "\n")

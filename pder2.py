f<-expression((x^3 * y^5) - (2 * x^2 * y) + x)
f

x<-as.numeric(readline(prompt = "Enter value for x: "))
y<-as.numeric(readline(prompt = "Enter value for y: "))

fx<-D(f,'x')
fx
cat("fx(",x,",",y,") =", eval(fx), "\n")

fy<-D(f,'y')
fy
cat("fy(",x,",",y,") =", eval(fy), "\n")

fxx<-D(fx,'x')
fxx
cat("fxx(",x,",",y,") =", eval(fxx), "\n")

fyy<-D(fy,'y')
fyy
cat("fyy(",x,",",y,") =", eval(fyy), "\n")

fxy<-D(fx,'y')
fxy
cat("fxy(",x,",",y,") =", eval(fxy), "\n")

fyx<-D(fy,'x')
fyx
cat("fyx(",x,",",y,") =", eval(fyx), "\n")

fxxx<-D(fxx,'x')
fxxx
cat("fxxx(",x,",",y,") =", eval(fxxx), "\n")

fyyy<-D(fyy,'y')
fyyy
cat("fyyy(",x,",",y,") =", eval(fyyy), "\n")

fxxy<-D(fxx,'y')
fxxy
cat("fxxy(",x,",",y,") =", eval(fxxy), "\n")

fxyx<-D(fxy,'x')
fxyx
cat("fxyx(",x,",",y,") =", eval(fxyx), "\n")

fyxx<-D(fyx,'x')
fyxx
cat("fyxx(",x,",",y,") =", eval(fyxx), "\n")

fyyx<-D(fyy,'x')
fyyx
cat("fyyx(",x,",",y,") =", eval(fyyx), "\n")

fyxy<-D(fyx,'y')
fyxy
cat("fyxy(",x,",",y,") =", eval(fyxy), "\n")

fxyy<-D(fxy,'y')
fxyy
cat("fxyy(",x,",",y,") =", eval(fxyy), "\n")

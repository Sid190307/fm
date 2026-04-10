calc<-function(a,b)
{add<-a+b
 cat("addition is ",add)
 sub<-a-b
 cat("\nSubtraction is ",sub)
 mul<-a*b
 cat("\nmultiplication is ",mul)
 if(b!=0)
 {div<-a/b
  cat("\nDivision: ",div)}
 else
 {cat("\nDivision not possible!!")}
}
calc(5,2)

f1 <- expression(2*x^3 - 4*x)

f1

dif <- D(f1, 'x')
dif

polyroot(c(-4, 0, 6))

x = -1
eval(dif)

x = 0
eval(dif)

x = 1
eval(dif)

fun = function(x)(2*x^3 - 4*x)

curve(fun, xlim = c(-5,5), ylim = c(-5,5))

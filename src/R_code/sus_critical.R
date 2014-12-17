wolff <- read.table("temperature_sweep.dat",header=T)
attach(wolff)

steps = 14

sus.crit <- which.max(Susceptibility)

x1 = log(Temperature - Temperature[sus.crit])
y1 = log(Susceptibility)

plot(x1,y1,type="n",
    ylim = c(-20,-12),
    xlab = "Log(Temperature - Tc)",
    ylab = "Log(Susceptibility)",
    main = expression(paste("Susceptibility Exponent ",gamma," (tail)")))

grid()

colors = rainbow(steps)
tmps = seq(2, 3, length.out = steps)
for( i in steps:1 ){
    lines(log(Temperature - tmps[i]),log(Susceptibility),col=colors[i])
    }
#plots warm colors first, warm colors represent "guesses" < t_c
lines(x1,y1)

pow.rng <- which(-3 < x1 & x1 < -1)

sus.fit <- lm(y1[pow.rng] ~ x1[pow.rng])

abline(sus.fit,lty = 4)

detach(wolff)

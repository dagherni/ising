wolff <- read.table("temperature_sweep.dat",header=T)
attach(wolff)

steps = 14

mag.crit <- which.max(Susceptibility)

x1 = log(abs(Temperature - Temperature[mag.crit]))
y1 = log(Magnetization - Magnetization[mag.crit])

plot(x1,y1,type="n",
    xlim=c(-3.5,-1),
    ylim=c(-1,0),
    xlab = "Log(Temperature - Tc)",
    ylab ="Log(Magnetization)",
    main = expression(paste("Magnetic Exponent ",beta,sep=" ")))

grid()

bound = c(120,120)
tc.guesses = Temperature[seq(mag.crit - bound[1], mag.crit + bound[2],
    length.out = steps)]

mag.guesses= Magnetization[seq(mag.crit - bound[1], mag.crit + bound[2],
    length.out = steps)]

colors = rainbow(steps)
colors[7] = "black"

for(i in 1:steps ){
    d1 = log(-Temperature + tc.guesses[i])
    d2 = log(Magnetization)

    lines(d1,d2,col = colors[i])

    fitrange = which(-3.5 < d1 & d1 < -2)

    fit = lm(d2[fitrange]~d1[fitrange])
    print(fit)

    if (i == 7) abline(fit, col = colors[i],lty = 4)
    print(paste(i,tc.guesses[i]))
}



lines(log(-Temperature + tc.guesses[7]),d2)
fit <- lm(d2[fitrange] ~ log(-Temperature + tc.guesses[7])[fitrange])
abline(fit,lty = 4)

detach(wolff)

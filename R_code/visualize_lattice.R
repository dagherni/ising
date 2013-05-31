spin.file <- "array.dat" 
#change to path of spin output file

spin.colors <- c("purple","red","green") #downspin, upspin
spin.matrix <- as.matrix(read.table(spin.file))

par(mar=c(1,1,3,1)+.1)

image(spin.matrix,col=spin.colors,axes=FALSE)
title(main="Wolff Cluster Algorithm")

#axis(1,at=seq(0,1,by=(1/(dim(spin.matrix)[1]-1))*1),labels=F)
#axis(2,at=seq(0,1,by=(1/(dim(spin.matrix)[2]-1))*1),labels=F)
box()
dev.copy2pdf(file="vis_lattice.pdf") #uncomment to generate output file

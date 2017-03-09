data.table <- read.table("result.txt",sep=",")
names(data.table) <- c("rod1","rod2","rod3","X","Y","z_height")
data.table
rms <- function(x) sqrt(sum(x^2)/length(x))
res<-aggregate(z_height~rod1+rod2+rod3,data.table,rms) 
res<-res[order(res$z_height),]
write.csv(res,file="rms.csv")

goods=d[d$rod1==-3&d$rod2==0&d$rod3==3,]
write.csv(goods,file="good.csv)

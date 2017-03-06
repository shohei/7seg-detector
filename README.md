# 7seg detector

## 戦略
目標座標トリミング→学習器と比較→数値出力
Golangでやりたいけど、Python+OpenCVでも可


![](target.jpg)

# fswebcam
``` 
$  fswebcam --no-timestamp --no-banner -r 1280x1024 image.jpg
``` 

# トリミング後
![](dst.jpg)

# 2値化
![](bwimage.jpg)

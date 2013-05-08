class juxing:
    def jx(self,first,second):
        self.first=first
        self.second=second
        self.s1=(self.first*self.second)
        print "矩形面积大小为：%d." %  self.s1
        return self.s1       
class zfxing:
    def zfx(self,side):
        self.side=side
        self.s2=self.side**2
        print "正方形面积大小为：%d" %  self.s2
        return self.s2
class sjxing:
    def sjx(self,bottom,height):
        self.bottom=bottom
        self.height=height
        self.s3=((self.bottom*self.height)/2)
        print "三角形面积大小为：%d" %  self.s3
        return self.s3
class yuanxing:
    def yx(self,r):
        self.r=r
        self.s4=(3.14*(self.r*self.r))
        print "圆形面积大小为：%f" % self.s4
        return self.s4
class tuoyuan:
    def ty(self,a,b):
        self.a=a
        self.b=b
        self.s5=(3.14*a*b)
        print "椭圆面积为：%f" % self.s5
        return self.s5
side=int(raw_input("请输入正方形边长:"))
szfxing=zfxing()
t1=szfxing.zfx(side)    
length=int(raw_input("请输入矩形的长："))
width=int(raw_input("请输入矩形的宽："))
sjuxing=juxing()
t2=sjuxing.jx(length,width)  
bottom=int(raw_input("请输入三角形底长："))
height=int(raw_input("请输入三角形的高："))
ssjxing=sjxing()
t3=ssjxing.sjx(bottom,height)
r=float(raw_input("请输入圆形半径:"))
syuanxing=yuanxing()
t4=syuanxing.yx(r)
a=float(raw_input("请输入椭圆半长轴："))
b=float(raw_input("请输入椭圆半短轴："))
stuoyuan=tuoyuan()
t5=stuoyuan.ty(a,b)
t=t1+t2+t3+t4+t5
e=t/5
print "总面积为：%f" % t
print "平均面积为:%f" % e


   

    	

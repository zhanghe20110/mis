class juxing:
    def jx(self,first,second):
        self.first=first
        self.second=second
        self.s1=(self.first*self.second)
        print "���������СΪ��%d." %  self.s1
        return self.s1       
class zfxing:
    def zfx(self,side):
        self.side=side
        self.s2=self.side**2
        print "�����������СΪ��%d" %  self.s2
        return self.s2
class sjxing:
    def sjx(self,bottom,height):
        self.bottom=bottom
        self.height=height
        self.s3=((self.bottom*self.height)/2)
        print "�����������СΪ��%d" %  self.s3
        return self.s3
class yuanxing:
    def yx(self,r):
        self.r=r
        self.s4=(3.14*(self.r*self.r))
        print "Բ�������СΪ��%f" % self.s4
        return self.s4
class tuoyuan:
    def ty(self,a,b):
        self.a=a
        self.b=b
        self.s5=(3.14*a*b)
        print "��Բ���Ϊ��%f" % self.s5
        return self.s5
side=int(raw_input("�����������α߳�:"))
szfxing=zfxing()
t1=szfxing.zfx(side)    
length=int(raw_input("��������εĳ���"))
width=int(raw_input("��������εĿ�"))
sjuxing=juxing()
t2=sjuxing.jx(length,width)  
bottom=int(raw_input("�����������ε׳���"))
height=int(raw_input("�����������εĸߣ�"))
ssjxing=sjxing()
t3=ssjxing.sjx(bottom,height)
r=float(raw_input("������Բ�ΰ뾶:"))
syuanxing=yuanxing()
t4=syuanxing.yx(r)
a=float(raw_input("��������Բ�볤�᣺"))
b=float(raw_input("��������Բ����᣺"))
stuoyuan=tuoyuan()
t5=stuoyuan.ty(a,b)
t=t1+t2+t3+t4+t5
e=t/5
print "�����Ϊ��%f" % t
print "ƽ�����Ϊ:%f" % e


   

    	

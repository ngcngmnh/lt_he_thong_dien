import array
import math
import chuong_1
import chuong_2
def qn1(q1,q2,r1,r2,r3):
    return q1,q2,(r2+r3)/(r1+r2+r3),r3/(r1+r2+r3)
def qn2(q1,q2,r1,r2,r3):
    return q1,q2,r1/(r1+r2+r3),(r2+r1)/(r1+r2+r3) 
def z_cp():
    return 0.255*600,60*0.005*8760,'27.27(3.93(13.44-Q_b1)^2+3.93(13.56-Q_b1)^2+7.57(0.815(13.44-Q_b1)+0.41(13.56-Q_b2))^2+16.83(0.185(13.44-Q_b1)+0.59(13.56-Q_b2))^2+16.58(3.072+0.185Q_b1-0.41Q_b2)^2)'
def z_cp3():
    return (0.1+0.125)*600,60*8760*0.005,'274.56*(13.9 - Q_b3)^2'
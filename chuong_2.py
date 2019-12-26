import array
import math
from chuong_1 import load_1,load_2,load_3

def ap_tai_dien():
    global load_1,load_2,load_3
    load_1.append(4.34*math.sqrt(load_1[7]+0.016*load_1[0]*1000))
    load_2.append(4.34*math.sqrt(load_2[7]+0.016*load_2[0]*1000))
    load_3.append(4.34*math.sqrt(load_3[7]+0.016*load_3[0]*1000))
    print('Ap tai dien [U_1,U_2,U_3]:',load_1[8],load_2[8],load_3[8])
    print('Lựa chọn tải 110kV để truyền điện áp đến các phụ tải')
    print()

def loai_phu_tai():
    print('Tai 3: don\nTai 1, Tai 2: tam giac')
    print()

def dong_cho_phep():
    print('Chọn tiết diện tiêu chuẩn, nhiệt độ tiêu chuẩn của môi trường xung quanh lúc chế tạo là 25oC, môi trường xung quanh thực thế là 35oC, hệ số hiệu chỉnh nhiệt độ là 0.88\nDòng cho phép dẫn đạt giá trị : 0.88×220= 193.6 (A)')
    print()

def t_max_tb():
    global j_kt
    t_max_tb = (load_1[0]*load_1[3] + load_2[0]*load_2[3] + load_3[0]*load_3[3])/(load_1[0]+load_2[0]+load_3[0])
    if t_max_tb <= 3000:
        j_kt = 1.3
    elif t_max_tb <= 5000:
        j_kt = 1.1
    else:
        j_kt = 1.0
    print('T_max_tb =',t_max_tb)
    print('==> j_kt =',j_kt)
    print()

def day_don(p,c,j_kt):
    i_max = math.sqrt((p*1000000)**2+((p*1000000)*math.tan(math.acos(c)))**2)/(math.sqrt(3)*110000)
    f_kt = i_max/j_kt
    print('I_max',i_max)
    print('F_kt',f_kt)
    print('==> Chon day: AC-120')
    print()

def day_kep(p,c,j_kt):
    i_max = math.sqrt((p*1000000)**2+((p*1000000)*math.tan(math.acos(c)))**2)/(math.sqrt(3)*110000)
    f_kt = (i_max/2)/j_kt
    print('I_max',i_max)
    print('F_kt',f_kt)
    input('==> Chon day: AC-120')
    print()

def day_tam_giac(p1,c1,p2,c2,l1,l2,l3,j_kt):
    global s_1,s_2,s_3,s_a,s_b
    s_a = complex(p1,p1*math.tan(math.acos(c1)))
    s_b = complex(p2,p2*math.tan(math.acos(c2)))
    s_1 = (s_a*(l2+l3) + s_b*l3)/(l1+l2+l3)
    s_3 = (s_a*l1 + s_b*(l1+l2))/(l1+l2+l3)
    s_2 = s_b - s_3
    f_1_kt = abs(s_1)*10**3/(math.sqrt(3)*110*j_kt)
    f_2_kt = abs(s_2)*10**3/(math.sqrt(3)*110*j_kt)
    f_3_kt = abs(s_3)*10**3/(math.sqrt(3)*110*j_kt)
    print('S_a =',s_a)
    print('S_b =',s_b)
    print('S_1 =',s_1)
    print('S_3 =',s_3)
    print('S_2 =',s_2)
    print('\nNguon-->L1: F_1_kt =',f_1_kt)
    print('==> Chon day: AC-150')
    print('\nNguon-->L2: F_2_kt =',f_2_kt)
    print('==> Chon day: AC-70')
    print('\nL1-->L2: F_3_kt =',f_3_kt)
    print('==> Chon day: AC-95')
    print()

def chon_tru():
    print('Deu la lo don: ==> Chon tru Y110-1')
    print()

def tru_don():
    global d_m
    d_m = 6.64
    print('D_m =',d_m)
    print()

def tro_khang(r0,l):
    return r0*l

def cam_khang(d_m,r,rr,l): #r la ban kinh day dan
    r_ = r*rr
    x_0 = 0.144*math.log10(d_m/(r_/1000))+0.016
    X = x_0*l
    return x_0,X
def dung_khang(d_m,r,l):
    b_0 = 7.58/1000000/math.log10(d_m/(r/1000))
    Y= b_0*l
    return b_0,Y

def cong_suat_dQ(y):
    return 0.5*(110**2)*y

def cong_suat_nut(dQ):
    global s_1_,s_2_
    s_1_ = complex(s_a,(-dQ[1]-dQ[0]))
    s_2_ = complex(s_b,(-dQ[2]-dQ[0]))
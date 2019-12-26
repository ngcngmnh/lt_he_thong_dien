import array
import math
import chuong_1
import chuong_2
def bien_ap_t1():
    s_max=abs(chuong_2.s_a)
    s_dm_B=s_max/1.4
    d_p_n=260
    d_p_0=100
    u_n=14
    i_0=0.045
    r_b1=d_p_n*110**2/20000**2*10**3
    z_b1=u_n*110**2/20000*10
    x_b1=math.sqrt(z_b1**2-r_b1**2)
    d_q_FE=i_0*20000/100
    print('S_ptmax1:',s_max,'\nS_dm_B>=',s_dm_B)
    print('==> Chon 2 may bien ap 20000/110 kV')
    print('R_B1:',r_b1)
    print('Z_B1:',z_b1)
    print('X_B1:',x_b1)
    print('ΔQ_FE:',d_q_FE)
    print()

def bien_ap_t2():
    s_max=abs(chuong_2.s_b)
    s_dm_B=s_max/1.4
    d_p_n=260
    d_p_0=100
    u_n=14
    i_0=0.045
    r_b1=d_p_n*110**2/20000**2*10**3
    z_b1=u_n*110**2/20000*10
    x_b1=math.sqrt(z_b1**2-r_b1**2)
    d_q_FE=i_0*20000/100
    print('S_ptmax2:',s_max,'\nS_dm_B>=',s_dm_B)
    print('==> Chon 2 may bien ap 20000/110 kV')
    print('R_B2:',r_b1)
    print('Z_B2:',z_b1)
    print('X_B2:',x_b1)
    print('ΔQ_FE:',d_q_FE)
    print()
def bien_ap_t3():
    s_max=chuong_1.load_3[0]/chuong_1.load_3[2]
    d_p_n=220
    d_p_0=115
    u_n=14
    i_0=0.042
    r_b1=d_p_n*110**2/31500**2*10**3
    z_b1=u_n*110**2/31500*10
    x_b1=math.sqrt(z_b1**2-r_b1**2)
    d_q_FE=i_0*31500/100
    print('S_ptmax3:',s_max,'\nS_dm_B>=',s_max)
    print('==> Chon 1 may bien ap 31500/110 kV')
    print('R_B3:',r_b1)
    print('Z_B3:',z_b1)
    print('X_B3:',x_b1)
    print('ΔQ_FE:',d_q_FE)
    print()
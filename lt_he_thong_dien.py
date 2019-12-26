import chuong_1
import chuong_2
import chuong_3
import chuong_5
import chuong_7

chuong_1.so_lieu_ban_dau()
chuong_1.can_bang_cong_suat_td()
chuong_1.can_bang_cong_suat_pk()
chuong_2.ap_tai_dien()
chuong_2.loai_phu_tai()
chuong_2.t_max_tb()
chuong_2.day_don(chuong_1.load_3[0],chuong_1.load_3[2],chuong_2.j_kt)
chuong_2.day_tam_giac(chuong_1.load_1[0],chuong_1.load_1[2],chuong_1.load_2[0],chuong_1.load_2[2],chuong_1.load_1[7],chuong_1.load_2[7],117.05,chuong_2.j_kt)
chuong_2.chon_tru()
chuong_2.tru_don()

r0=[]
r0.append(0.33)
r0.append(0.21)
r0.append(0.46)
r0.append(0.27)

x0=[]
x0.append(chuong_2.cam_khang(chuong_2.d_m,6.75,0.726,117.05)[0])
x0.append(chuong_2.cam_khang(chuong_2.d_m,8.5,0.768,chuong_1.load_1[7])[0])
x0.append(chuong_2.cam_khang(chuong_2.d_m,5.7,0.726,chuong_1.load_2[7])[0])
x0.append(chuong_2.cam_khang(chuong_2.d_m,7.6,0.768,chuong_1.load_3[7])[0])

b0=[]
b0.append(chuong_2.dung_khang(chuong_2.d_m,6.75,117.05)[0])
b0.append(chuong_2.dung_khang(chuong_2.d_m,8.5,chuong_1.load_1[7])[0])
b0.append(chuong_2.dung_khang(chuong_2.d_m,5.7,chuong_1.load_2[7])[0])
b0.append(chuong_2.dung_khang(chuong_2.d_m,7.6,chuong_1.load_3[7])[0])

R=[]
R.append(chuong_2.tro_khang(r0[0],117.05))
R.append(chuong_2.tro_khang(r0[1],chuong_1.load_1[7]))
R.append(chuong_2.tro_khang(r0[2],chuong_1.load_2[7]))
R.append(chuong_2.tro_khang(r0[3],chuong_1.load_3[7]))

X=[]
X.append(chuong_2.cam_khang(chuong_2.d_m,6.75,0.726,117.05)[1])
X.append(chuong_2.cam_khang(chuong_2.d_m,8.5,0.768,chuong_1.load_1[7])[1])
X.append(chuong_2.cam_khang(chuong_2.d_m,5.7,0.726,chuong_1.load_2[7])[1])
X.append(chuong_2.cam_khang(chuong_2.d_m,7.6,0.768,chuong_1.load_3[7])[1])

Y=[]
Y.append(chuong_2.dung_khang(chuong_2.d_m,6.75,117.05)[1])
Y.append(chuong_2.dung_khang(chuong_2.d_m,8.5,chuong_1.load_1[7])[1])
Y.append(chuong_2.dung_khang(chuong_2.d_m,5.7,chuong_1.load_2[7])[1])
Y.append(chuong_2.dung_khang(chuong_2.d_m,7.6,chuong_1.load_3[7])[1])

print('=== L1L2 ===')
print('1 lo\tAC-95\tl=',117.05,'\tr0=',r0[0],'\tx_0=',x0[0],'\tb_0=',b0[0],'\tR=',R[0],'\tX=',X[0],'\tY=',Y[0])
print('----------------------')

print('=== N-L1 ===')
print('1 lo\tAC-150\tl=',chuong_1.load_1[7],'\tr0=',r0[1],'\tx_0=',x0[1],'\tb_0=',b0[1],'\tR=',R[1],'\tX=',X[1],'\tY=',Y[1])
print('----------------------')

print('=== N-L2 ===')
print('1 lo\tAC-70 \tl=',chuong_1.load_2[7],'\tr0=',r0[2],'\tx_0=',x0[2],'\tb_0=',b0[2],'\tR=',R[2],'\tX=',X[2],'\tY=',Y[2])
print('----------------------')

print('=== N-L3 ===')
print('1 lo\tAC-120\tl=',chuong_1.load_3[7],'\tr0=',r0[3],'\tx_0=',x0[3],'\tb_0=',b0[3],'\tR=',R[3],'\tX=',X[3],'\tY=',Y[3])
print('----------------------')
print()


print('Tinh ton that CS va sut ap')
dQ=[]
dQ.append(chuong_2.cong_suat_dQ(Y[0])) #ΔQ_12
dQ.append(chuong_2.cong_suat_dQ(Y[1])) #ΔQ_1
dQ.append(chuong_2.cong_suat_dQ(Y[2])) #ΔQ_2
chuong_2.cong_suat_nut(dQ)

z=[]
z.append(complex(R[0],X[0]))
z.append(complex(R[1],X[1]))
z.append(complex(R[2],X[2]))
print(z)
S_N_=[]
S_N_.append((chuong_2.s_2_*z[2]+chuong_2.s_1_*(z[0]+z[2]))/(z[0]+z[1]+z[2]))
S_N_.append((chuong_2.s_1_*z[1]+chuong_2.s_2_*(z[0]+z[1]))/(z[0]+z[1]+z[2]))

S_N=[]
S_N.append(complex(S_N_[0].real,-S_N_[0].imag))
S_N.append(complex(S_N_[1].real,-S_N_[1].imag))
S_21=S_N[1]-chuong_2.s_2_

print('ΔQ_1 =',dQ[1])
print('ΔQ_2 =',dQ[2])
print('ΔQ_12 =',dQ[0])
print('\nCong suat o cac nut:')
print('S\'_1',chuong_2.s_1_)
print('S\'_2',chuong_2.s_2_)
print('\nDong CS day noi voi nguon:')
print('S*_N1: ',S_N_[0])
print('S_N1: ',S_N[0])
print('S*_N2: ',S_N_[1])
print('S_N2: ',S_N[1])
print('S\'_21 =',S_21)

print('\n--> Chuong 3 <--\n')
chuong_3.bien_ap_t1()
chuong_3.bien_ap_t2()
chuong_3.bien_ap_t3()

print('\n--> Chuong 5 <--\n')
q_n_1=chuong_5.qn1(chuong_2.s_a.imag,chuong_2.s_b.imag,R[1],R[0],R[2])
q_n_2=chuong_5.qn2(chuong_2.s_a.imag,chuong_2.s_b.imag,R[1],R[0],R[2])
print('Q_N1:',q_n_1[2],'* (',q_n_1[0],'- Q_b1 )','+',q_n_1[3],'* (',q_n_1[1],'- Q_b2 )')
print('Q_N2:',q_n_2[2],'* (',q_n_2[0],'- Q_b1 )','+',q_n_2[3],'* (',q_n_2[1],'- Q_b2 )')
print('Z_1 =',chuong_5.z_cp()[0],'*(Q_b1+Q_b2)','\nZ_2 =',chuong_5.z_cp()[1],'*(Q_b1+Q_b2)','\nZ_3 =',chuong_5.z_cp()[2])
print('\nTai 3\n')
print('Z_1 =',chuong_5.z_cp3()[0],'*Q_b3','\nZ_2 =',chuong_5.z_cp3()[1],'*Q_b3','\nZ_3 =',chuong_5.z_cp3()[2])
print('Q_b3 =',6.65)

chuong_7.ch7()
import array as arr
import math
cos_nguon = 0.8
u_thanh_cai = [1.1 , 1.05, 1.1] #[phu tai cuc dai, phu tai cuc tieu, su co]
u_thu_cap = 22 #kV
do_lech_u = 0.05
load_1 = []
load_2 = []
load_3 = []

def so_lieu_ban_dau():

    global load_1,load_2,load_3

    # open file and read the content in a list
    with open('load_1.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            load_1.append(float(currentPlace))

    # open file and read the content in a list
    with open('load_2.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            load_2.append(float(currentPlace))

    # open file and read the content in a list
    with open('load_3.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            load_3.append(float(currentPlace))
    print('So lieu ban dau [Pmax, Pmin, cos, Tmax, LT/KLT(1/0), x, y, l]')
    print('Tai 1:',load_1)
    print('Tai 2:',load_2)
    print('Tai 3:',load_3)
    print()
    
#     print('Tai 1:')
#     load_1[0]=float(input('P_max (MW): '))
#     load_1[1]=load_1[0]*40/100
#     print('P_min (MW): ',load_1[1])
#     load_1[2]=float(input('cos_: '))
#     load_1[3]=float(input('T_max: '))
#     load_1[4]=input('Yeu cau cung cap dien (KLT/LT): ')

#     print('\nTai 2:')
#     load_2[0]=float(input('P_max (MW): '))
#     load_2[1]=load_2[0]*40/100
#     print('P_min (MW): ',load_2[1])
#     load_2[2]=float(input('cos_: '))
#     load_2[3]=float(input('T_max: '))
#     load_2[4]=input('Yeu cau cung cap dien (KLT/LT): ')

#     print('\nTai 3:')
#     load_3[0]=float(input('P_max (MW): '))
#     load_3[1]=load_3[0]*40/100
#     print('P_min (MW): ',load_3[1])
#     load_3[2]=float(input('cos_: '))
#     load_3[3]=float(input('T_max: '))
#     load_3[4]=input('Yeu cau cung cap dien (KLT/LT): ')

#     print()

def vi_tri_tai():
    global leng,x_load,y_load
    leng = [0,0,0] #vi tri tai
    x_load = [0,0,0]
    y_load = [0,0,0]
    for m in range (0,3):
        print('\nVi tri Tai',m+1,':')
        x_load[m] = float(input('x (km)= '))
        y_load[m] = float(input('y (km)= '))
        leng[m] = math.sqrt(x_load[m]*x_load[m]+y_load[m]*y_load[m])
        print('leng_',m+1,'= ',leng[m],'(km)')
    print()

def can_bang_cong_suat_td():
    global tong_p_f,tong_p_pt,tong_p_md
    tong_p_pt = load_1[0]+load_2[0]+load_3[0] #tong phu tai
    tong_p_md = 1*0.09*tong_p_pt
    tong_p_f = tong_p_pt + tong_p_md
    print('Tong_P_pt =',tong_p_pt)
    print('Tong_P_md =',tong_p_md)
    print('Tong_P_F =',tong_p_f)
    print()

def can_bang_cong_suat_pk():
    global tong_q_f, tong_q_pt,tong_dq_b, q_bu
    tong_q_f = tong_p_f*round(math.tan(math.acos(cos_nguon)),2)
    tong_q_pt = load_1[0]*math.tan(math.acos(load_1[2])) + load_2[0]*math.tan(math.acos(load_2[2])) +load_3[0]*math.tan(math.acos(load_3[2]))
    tong_dq_b = 0.1*math.sqrt(tong_p_f**2+tong_q_pt**2)
    q_bu=1*tong_q_pt+tong_dq_b-tong_q_f
    print('Tong_Q_F =',tong_q_f,'\nTong_Q_pt =',tong_q_pt,'\nTong_dQ_B =',tong_dq_b,'\nQ_bu =',q_bu)
    if q_bu < 0:
        print('==> Khong can lap tu bu')
    else:
        print('==> Can lap tu bu')
    print()

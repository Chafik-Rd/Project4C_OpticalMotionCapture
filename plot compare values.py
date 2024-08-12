import numpy as np
import pickle
import matplotlib.pyplot as plt
import Detect_color
import csv
import pandas

with open("D:/Project4C/coding/Video_Test/65-03-28/ค่าตำแหน่งจริง/KT20.WPOS", "rb") as file:
    G_real_idx, G_real_pos,Y_real_idx, Y_real_pos,P_real_idx, P_real_pos = pickle.load(file) 
# print(G_real_idx, G_real_pos)
# print(P_real_idx, P_real_pos)
# print(Y_real_idx, Y_real_pos)
with open("D:/Project4C/coding/Video_Test/65-03-28/KT/KTF20.exp", 'r') as file:
    sampling_rate = float(file.readlines()[3].split('\t')[0])


df = pandas.read_csv("D:/Project4C/coding/Video_Test/65-03-28/KT/KTF20.exp", sep='\t', skiprows=range(8))

# df['Frame #'] = df['Frame #'].apply(lambda x: x/sampling_rate) 
s = 86      #start frame
f = 333     #stop frame
sec_mahidol = (df['Frame #'][s:f]-df['Frame #'][s])/sampling_rate
aperture_mahidol = df['Aperture'][s:f]*1000
transport_mahidol = df['Result Transport vel'][s:f]*1000
level_mahidol = df['Transport Z'][s:f]*1000

fig0 = plt.figure()
x, y = Detect_color.th_in_dist(G_real_pos, G_real_idx, P_real_pos, P_real_idx)

ax1 = fig0.add_subplot(311)
ax1.plot(np.array(x)/60,np.array(y)-20)
ax1.scatter(np.array(x)/60,np.array(y)-20)
# ax1.plot(sec_mahidol,aperture_mahidol)
# ax1.scatter(sec_mahidol,aperture_mahidol)
ax1.set_ylabel('Distance(mm)')

wrist_index, v = Detect_color.velocity(Y_real_idx, Y_real_pos)
ax2 = fig0.add_subplot(312)
ax2.plot(np.array(wrist_index)/60,np.array(v)*60)
ax2.scatter(np.array(wrist_index)/60,np.array(v)*60)
ax2.plot(sec_mahidol,transport_mahidol)
ax2.scatter(sec_mahidol,transport_mahidol)
ax2.set_ylabel('Velocity(mm/sec)')

ax3 = fig0.add_subplot(313)
ax3.plot(Y_real_idx/60, (Y_real_pos[:, 2])+90)
ax3.scatter(Y_real_idx/60, (Y_real_pos[:, 2])+90)
ax3.plot(sec_mahidol, level_mahidol)
ax3.scatter(sec_mahidol, level_mahidol)
ax3.set_xlabel('Time(Sec)')
ax3.set_ylabel('Level(mm)')

plt.show()

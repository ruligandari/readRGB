import numpy as np

# Menentukan nilai o1 dan seterusnya
# jika ada 2 output sisanya bisa dikomentar atau dihapus
o1 = 805.836
o2 = 2417.508
o3 = 4029.18
o4 = 1611.672
o5 = 3223.344

# Menghitung eksponensial dari setiap keluaran dan mengurangi dengan nilai maksimum
exp_o1 = np.exp(o1 - np.max([o1, o2, o3, o4, o5]))
exp_o2 = np.exp(o2 - np.max([o1, o2, o3, o4, o5]))
exp_o3 = np.exp(o3 - np.max([o1, o2, o3, o4, o5]))
exp_o4 = np.exp(o4 - np.max([o1, o2, o3, o4, o5]))
exp_o5 = np.exp(o5 - np.max([o1, o2, o3, o4, o5]))

# Menghitung total eksponensial
total_exp = exp_o1 + exp_o2 + exp_o3 + exp_o4 + exp_o5

# Menghitung probabilitas setiap keluaran menggunakan softmax
s1 = exp_o1 / total_exp
s2 = exp_o2 / total_exp
s3 = exp_o3 / total_exp
s4 = exp_o4 / total_exp
s5 = exp_o5 / total_exp

# Menampilkan hasil
print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)
print("s5 =", s5)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fungsi Produktivitas
def produktivitas(x, y):
    return 0.4 * x**2 - 0.2 * y**2 + 0.5 * x * y + 5

# Turunan Parsial
def turunan_x(x, y):
    return 0.8 * x + 0.5 * y

def turunan_y(x, y):
    return 0.4 * y + 0.5 * x

# Antarmuka Streamlit
st.title("Pengaruh Media Sosial terhadap Produktivitas Gen Z")

x = st.slider("Durasi Penggunaan (jam/hari)", 0, 24, 4)
y = st.slider("Frekuensi Membuka Aplikasi (kali/hari)", 0, 50, 20)

# Evaluasi Fungsi
f_val = produktivitas(x, y)
df_dx = turunan_x(x, y)
df_dy = turunan_y(x, y)

st.write(f"**Skor Produktivitas**: {f_val:.2f}")
st.write(f"**∂f/∂x** (terhadap durasi): {df_dx:.2f}")
st.write(f"**∂f/∂y** (terhadap frekuensi): {df_dy:.2f}")

# Visualisasi 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(0, 24, 30)
Y = np.linspace(0, 50, 30)
X, Y = np.meshgrid(X, Y)
Z = produktivitas(X, Y)

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.scatter(x, y, f_val, color='black', s=50)  # Titik evaluasi

# Bidang singgung
x_range = np.linspace(x-3, x+3, 10)
y_range = np.linspace(y-3, y+3, 10)
x_plane, y_plane = np.meshgrid(x_range, y_range)
z_plane = f_val + df_dx * (x_plane - x) + df_dy * (y_plane - y)
ax.plot_surface(x_plane, y_plane, z_plane, color='red', alpha=0.3)

ax.set_xlabel('Durasi (jam)')
ax.set_ylabel('Frekuensi (kali)')
ax.set_zlabel('Produktivitas')

st.pyplot(fig)
 
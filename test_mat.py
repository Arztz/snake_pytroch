import matplotlib.pyplot as plt

plt.ion()
plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show(block=True)  # บังคับให้รอเปิดหน้าต่าง
input("Press Enter to exit...")

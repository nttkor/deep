import numpy as np
import matplotlib
matplotlib.use('Agg')  # 화면 없이 저장
import matplotlib.pyplot as plt

# x1 값을 0~1.4까지 정함
x1 = np.linspace(0, 1.4, 100)
# 위의 식에서 x2 = 1.4 - x1로 변형
x2 = 1.4 - x1

plt.plot(x1, x2, label='-0.5x1 - 0.5x2 + 0.7 = 0')
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(0, 1.5)
plt.ylim(0, 1.5)
plt.title('perceptron decision boundary for XOR')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('xor_perceptron_boundary.png')

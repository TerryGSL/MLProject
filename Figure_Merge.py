import matplotlib.pyplot as plt
from matplotlib.image import imread

# 读取四张图片
img1 = imread('epoch_50.png')
img2 = imread('epoch_100.png')
img3 = imread('epoch_150.png')
img4 = imread('epoch_200.png')

# 将四张图片合并到一张大图中
fig, axes = plt.subplots(nrows=2, ncols=2)
ax = axes.ravel()

for i in range(4):
    ax[i].imshow(eval(f'img{i+1}'), cmap='gray')
    ax[i].set_title(f'Epoch {i*50+50}')
    ax[i].axis('off')
    ax[i].set_aspect('equal')

fig.set_size_inches(8, 8)
fig.tight_layout()

# 保存合并后的图片
plt.savefig('merged_img.png')
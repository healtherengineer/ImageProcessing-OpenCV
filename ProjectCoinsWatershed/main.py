import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import watershed, expand_labels
from skimage.color import label2rgb
from skimage import data, exposure
#from skimage.viewer import ImageViewer

coins = data.coins()
#Orjinal görüntüye Açma uyguladım(Erozyon , Dilate)
coins = cv2.morphologyEx(coins ,cv2.MORPH_OPEN , (3,3))
#Gama ile yükselttim
gamma1 = 1.2
coins = np.array(255 * ((coins/255) ** gamma1),dtype='uint8')
#Burda kabartma denedim olmadı

# kenar bulma ve watershed ile bölütleme.
edges = sobel(coins)
#gama lazım


#burda kabartma da uygularız!
#Kabartma olmadı
#Keskinleştirme denedik
kernel_sharpen_1 = np.array([[-1,-1,-1,-1,-1],
                             [-1, 2, 2, 2,-1],
                             [-1, 2, 8, 2,-1],
                             [-1, 2, 2, 2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0
edges = cv2.filter2D(edges , -1,kernel_sharpen_1)
#Sobel görüntüyü de yükselttim
gamma = 0.6
edges = np.array(255 * ((edges/255) ** gamma),dtype='uint8')


cv2.imshow("sobel", edges)
# bazı arka plan ve ön plan piksellerini yoğunluk değerlerine bakarak etiketleme.
# bu etiketleme watershed algoritması için temel teşkil edecek.
markers = np.zeros_like(coins)
foreground, background = 1, 2
markers[coins < 30.0] = background
markers[coins > 150.0] = foreground
# cv2.imshow("eşikleme", markers)
ws = watershed(edges, markers)
seg1 = label(ws == foreground)
expanded = expand_labels(seg1, distance=6)
# sonuçları gösterme
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(13, 5), sharex=True, sharey=True)
axes[0].imshow(coins)
axes[0].set_title('Orijinal')
color1 = label2rgb(seg1, image=coins, bg_label=0)
axes[1].imshow(color1)
axes[1].set_title('Sobel+Watershed')
color2 = label2rgb(expanded, image=coins, bg_label=0)
axes[2].imshow(color2)
axes[2].set_title('Genişletilen etiketler')
for a in axes:
    a.axis('off')
    fig.tight_layout()
    plt.show()

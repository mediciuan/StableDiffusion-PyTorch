#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import matplotlib.image as mpimg


# In[1]:


import os

print(os.path.exists('data/generated_digit.png'))


# In[ ]:


import torch
import torchvision.utils as vutils
import os

# 1채널, 28x28 크기의 랜덤 이미지 (예: MNIST와 유사)
generated_image = torch.randn(0, 1, 2, 9)

# 'data' 폴더 생성 (없으면)
os.makedirs('data', exist_ok=True)

# 이미지 저장
vutils.save_image(generated_image, 'data/generated_digit.png')


# In[ ]:


os.path.exists('generated_digit.png')


# In[ ]:


import torchvision


# In[ ]:


import torch
from PIL import Image
import torchvision.transforms as T

with torch.no_grad():
    # VAE로 원본 하나 풀어보기
    original = imgs[0].unsqueeze(0).to('cuda')  # (1, 1, 28, 28)
    reconstructed = vae.encode_decode(original)
    reconstructed = reconstructed.clamp(-1, 1)
    reconstructed = (reconstructed + 1) / 2  # [-1,1] -> [0,1]

# Tensor -> PIL로 변경하기
to_pil = T.ToPILImage()

original_img = to_pil(imgs[0] * 0.5 + 0.5)
reconstructed_img = to_pil(reconstructed[0].cpu())    

# PNG로 저장하기
original_img.save("original.png")
reconstructed_img.save("reconstructed.png")

print("original.png, reconstructed.png로 저장되었습니다.")

import os

print("현재 작업 디렉토리:", os.getcwd())
print("파일 존재 여부:", os.path.exists("original.png"))


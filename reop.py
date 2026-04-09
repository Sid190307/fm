import numpy as np
from PIL import Image
def imgresize(im,sz):
    pil_im=Image.fromarray(np.uint8(im))
    return np.array(pil_im.resize(sz))

a=Image.open("man.jpg")

b=Image.open("woman.jpg")

a.show()
b.show()

i1= np.asarray(a)
i2= np.asarray(b)

print("co-ordinates of img1\n",i1)
print("co-ordinates of img1\n",i2)

r1=imgresize(i1,(145,220))
r2=imgresize(i1,(145,220))

x=8
y=2
lc=x*r1+y*r2
print("coordinates of lc\n",lc)
lc=Image.fromarray(lc)
lc.show()

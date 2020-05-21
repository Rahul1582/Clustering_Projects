import numpy as np
import cv2
    
img=cv2.imread('E:\img.jpg')

print(img.shape)
# Reshaping the images 
img_new=img.reshape((-1,3))

img_new= np.float32(img_new)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

#K=4
  
images=[]



for i in range(1,10):
    
    ret,label,center=cv2.kmeans(img_new,i,None,criteria,10,cv2.KMEANS_PP_CENTERS)

# Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    images.append(res2)


print(len(images))

img_res=[]

for image in images:
    scale_percent = 30# percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
   # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    img_res.append(resized)
 
j=1   

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


for j in range(1,2):
    im_tile = concat_tile([[img_res[j],img_res[j+1],img_res[j+2],img_res[j+3]],
                       [img_res[j+4],img_res[j+5],img_res[j+6],img_res[j+7]]])   
    
 
cv2.imshow('Image',im_tile)
cv2.waitKey(0)       
 
    
     
    


    
# pip install ngraph-core ngraph-onnx opencv-python 

# import onnx
# import ngraph as ng
# from ngraph_onnx.onnx_importer.importer import import_onnx_file
import cv2
import numpy as np

def preprocess(img_data):
    mean_vec = np.array([0.485, 0.456, 0.406])
    stddev_vec = np.array([0.229, 0.224, 0.225])
    norm_img_data = np.zeros(img_data.shape).astype('float32')
    for i in range(img_data.shape[0]):  
        norm_img_data[i,:,:] = (img_data[i,:,:]/255 - mean_vec[i]) / stddev_vec[i]
    return norm_img_data

# function = import_onnx_file('/home/tomek/Downloads/models/resnet50v2.onnx')
# backend = ng.runtime(backend_name="CPU")
# resnet50 = backend.computation(function)

print("--> Opening an image with cv2")
img = cv2.imread('/home/tomek/ngraph.png')
print("- Shape of the image imported with cv2: ", img.shape)
input()
print("--> Transposing the input image tensor (moving channels dimension to the first position)")
img = img.transpose(2, 0, 1)
print("- Current input shape: ", img.shape)
input()
print("--> Adding the batch dimension to the input image tensor")
img = img.reshape(1, 3, 224, 224)
print("- Current input shape: ", img.shape)
input()
print("--> Preprocessing the image (normalization)")
img = preprocess(img)
print("- Image ready to be classified")
input()

# result = resnet50(img)[0]
# print(np.argmax(result))
# print(np.argsort(result)[0][-5:])

# https://github.com/microsoft/onnxjs-demo/blob/master/src/data/imagenet.ts

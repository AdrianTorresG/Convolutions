import matplotlib.pyplot as plt
import argparse
from scipy import ndimage
from PIL import Image

#Se importan las funciones para generar los kernels
from LIB import *

if __name__ == "__main__":
    
    #Obtencion de la imagen
    parser = argparse.ArgumentParser()
    parser.add_argument("imageFile")
    args = parser.parse_args()
    Is = Image.open(args.imageFile);
    
    #Adaptacion de la imagen
    I = Is.convert('L');
    I = numpy.asarray(I);
    I = I / 255.0;
    
    #Generacion del padding
    I = numpy.pad(I, 10, pad_with, padder=1)
    
    #Preparacion de los kernels
    k0 = gaussianBlur(0.84089642,7)
    k1 = laplacianOfGaussian(1.4,5)
    k2 = simpleBoxBlur(10)
    k3 = horizontalLineDetection(3)
    k4 = verticalLineDetection(3)
    
    #Generacion de las convoluciones
    J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
    J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
    J2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
    J3 = ndimage.convolve(I, k3, mode='constant', cval=0.0)
    J4 = ndimage.convolve(I, k4, mode='constant', cval=0.0)
    
    #Preparacion  e impresion de las imagenes
    plt.figure(figsize = (15,15))
    plt.suptitle('Convoluciones con Paddings')
    
    plt.subplot(2,3,1)
    plt.imshow(Is)
    plt.title('Imagen Original')

    plt.subplot(2,3,2)
    plt.imshow(J0)
    plt.title('Gaussian Blur')
    
    plt.subplot(2,3,3)
    plt.imshow(J1)
    plt.title('Laplacian of Gaussian')
    
    plt.subplot(2,3,4)
    plt.imshow(J2)
    plt.xlabel('Simple Box Blur')
    
    plt.subplot(2,3,5)
    plt.imshow(J3)
    plt.xlabel('Horizontal Line Detection')
    
    plt.subplot(2,3,6)
    plt.imshow(J4)
    plt.xlabel('Vertical Line Detection')
    
    plt.grid(False)
    plt.show()

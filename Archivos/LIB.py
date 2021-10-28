import numpy
from math import ceil

#Funciones que generan los kernels para las convoluciones

#Gaussian blur
def gaussianBlur(sigma, k):
    matrix = numpy.zeros((k,k))
    #A cada valor de la matriz se le aplica la formula
    for x in range(0,k):
        for y in range(0,k):
            euler = numpy.exp(-((x**2) + (y**2))/(2*(sigma**2)))
            matrix[x][y] = (1/(2 * numpy.pi*(sigma**2)))*euler
    
    return matrix

#The Laplacian of Gaussian
def laplacianOfGaussian(sigma, k):
    matrix = numpy.zeros((k,k))
    #A cada valor de la matriz se le aplica la formula
    for x in range(0,k):
        for y in range(0,k):
            euler = numpy.exp(-((x**2) + (y**2))/(2*(sigma**2)))
            middle = 1 - ((x**2) + (y**2)) / (2*(sigma**2))
            matrix[x][y] = (1/(numpy.pi*(sigma**4)))*middle*euler
    
    return matrix

#Simple box blur
def simpleBoxBlur(k):
    #Matriz cuya suma de elementos siempre da uno
    matrix = numpy.full((k,k), 1/(k**2))
    
    return matrix

#Horizontal line detection with image convolutions
def horizontalLineDetection(k):
    #Se asegura que las dimensiones de la matriz no sean impares
    if (k % 2 == 0):
        k += 1
        
    matrix = numpy.full((k,k), -1)
    middle = ceil(k/2) - 1
    
    #Se cambian unicamente los valores horizontales del centro
    for x in range(0, k):
        matrix[middle][x] = 2
        
    return matrix

#Vertical line detection with image convolutions
def verticalLineDetection(k):
    #Se asegura que las dimensiones de la matriz no sean impares
    if (k % 2 == 0):
        k += 1
        
    matrix = numpy.full((k,k), -1)
    middle = ceil(k/2) - 1
    
    #Se cambian unicamente los valores verticales del centro
    for y in range(0, k):
        matrix[y][middle] = 2
        
    return matrix

#Funcion para la preparacion del padding
def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

# -*- coding: utf-8 -*-
"""Aula_9_ini.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bob-qAWAib3lm3fsFpA4mw7Np7RP1gCE
"""

import matplotlib.pyplot as plt
import numpy as np


def f (Fa,freq,ta):
  # Exemplo de função seno
  #Fa = 100  #frequencia de amostragem

  ##ta = 1.0/Fa  #periodo - intervalo entre amostras
  t = np.arange(0,1,ta)

  #freq = 1.
  x1=np.sin(2*np.pi*freq*t)

  plt.figure(figsize=(3,3))
  plt.title('sin(2*pi*t)')
  plt.plot(t,x1,color='red')
  #plt.show()

#f(100,2,1/100)
#f(100,1,1/100)
#f(100,3,1/100)
#f(100,4,1/100)
Fa= 100
freq = 1.
ta = 1.0/Fa  #periodo - intervalo entre amostras
t = np.arange(0,1,ta)
x1=np.sin(2*np.pi*freq*t)
# Exemplo de transformada fft
X1 = np.fft.fft(x1)
abs_X1 = np.abs(X1/Fa)

N = len(X1)   # As nossas 100 amostras
n = np.arange(N)   # Cria um vetor de 0:N:1
ts = N/Fa    # Tempo em segundos
freq = n/ts

plt.figure(figsize=(3,3))
plt.title('sin(2*pi*t)')
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
#plt.stem(freq,abs_X1,'r', markerfmt =" ")
#plt.show()



# Para a pergunta 6 e seguintes
from scipy.io import wavfile

from IPython.display import Audio, display

sampFreq, sound = wavfile.read('tom.wav')


print("sampFreq: ",sampFreq)
print("sound: ",sound.shape)

print("tempo em segundos: ",sound.shape[0]/sampFreq)

print("tipo variavel: ",sound.dtype)

sound = sound/2**15
print("sound22: ",sound)

esq = sound[:,0]
dir = sound[:,1]

plt.figure(figsize=(1,2))
plt.title('Tom.wav')
plt.plot(esq,color='red') 
plt.plot(dir,color='blue')  
plt.show()


time = np.arange(0,sound.shape[0]/sampFreq,1/sampFreq)

plt.subplot(121)
plt.rcParams['figure.figsize'] = (6,2)
plt.plot(time[6000:7000],esq[6000:7000])
plt.xlabel('Time (s)')
plt.ylabel('canal esqiuerdo')
plt.show()

plt.subplot(1,2,2)
plt.plot(time[6000:7000],esq[6000:7000])
plt.xlabel('Time (s)')
plt.ylabel('canal esqiuerdo')
plt.show()

esq = np.fft.rfft(esq)
print(esq)


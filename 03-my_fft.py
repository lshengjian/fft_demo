from typing import List
import numpy as np
tau=np.pi*2
eps=1e-6
im=0+1j
def FFT(P:List[complex]):
    n=len(P)
    half=n//2
    if n==1:
        #print(P)
        return P
    w0=np.exp(tau*im/n)
    Pe,Po=P[::2],P[1::2]
    ye,yo=FFT(Pe),FFT(Po)
    y=[0]*n
    w=1+0j
    for j in range(half):
        y[j]=ye[j]+yo[j]*w
        y[j+half]=ye[j]-yo[j]*w
        w*=w0
    #print(y)
    return y
def IFFT(P:List[complex]):
    n=len(P)
    half=n//2
    if n==1:
        return P
    w0=np.exp(0-tau*im/n)
    Pe,Po=P[::2],P[1::2]
    ye,yo=IFFT(Pe),IFFT(Po)
    y=[0]*n
    w=1+0j
    for j in range(half):
        y[j]=ye[j]+yo[j]*w
        y[j+half]=ye[j]-yo[j]*w
        w*=w0
    #print(y)
    return y


def main():
    p1=[5,3,2,1]
    y=FFT(p1)
    print(y)
    p2:List[complex]=IFFT(y)
    for p in p2:
        p/=len(p2)
        print(p.real)
    
    print('*'*10)
    p1=[1,0,2]+[0]*5
    p2=[2,3,1]+[0]*5
    y1=FFT(p1)
    y2=FFT(p2)
    y=[0+0j]*8

    for i in range(len(y)):
        y[i]=y1[i]*y2[i]
    p2:List[complex]=IFFT(y)
    for p in p2:
        p/=len(p2)
        print(p.real)

if __name__ == "__main__":
    main()
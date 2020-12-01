from django.shortcuts import render
from django.http import HttpResponse
from .forms import SetupForm

# Create your views here.
def index(requset):
    # return HttpResponse('Hello World')
    params = {
        'title': 'ようこそ',
        'msg' : '計算をするWebアプリです。',
        'next' : '計算ページへ'
    }
    return render(requset, 'calcu/index.html' , params)

def calcu(requset):
    # return HttpResponse('Hello World')
    params = {
        'title': '計算実行プログラム',
        'msg' : 'ここからが計算できます。',
        'param_title' : 'パラメータ設定',
        'setup' : SetupForm()
    }
    return render(requset, 'calcu/calcu.html' , params)

def result(requset):

    nx = requset.POST['nx']
    xmax = requset.POST['xmax']
    c = requset.POST['c']
    alpha = requset.POST['alpha']


    params = {
        'title': '計算実行プログラム',
        'msg' : 'ここからが計算できます。',
        'param_title' : 'パラメータ設定',
        'setup' : SetupForm(),
        'nx':nx,
        'xmax':xmax,
        'c':c,
        'alpha':alpha
    }


    params['title'] = '計算結果'
    params['setup'] = SetupForm(requset.POST)

    AdvectionEquation(nx, xmax ,c , alpha)

    # setup ={
    #     'nx': 'nx',
    #     'xmax':'xmax',
    #     'c': 'c',
    #     'alpha': 'alpha'
    # }
    
    return render(requset, 'calcu/result.html', params)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def AdvectionEquation(nx, xmax ,c , alpha):
    nx = int(nx)
    xmax = int(xmax)
    dx = float(xmax) / (float(nx)-1)
    nt = 100
    c = float(c)
    alpha = float(alpha)
    dt = 0.25 #alpha * (dx/c) 
    
    x = np.linspace(0,2,nx)
    
    un = []
    u = np.ones(nx)
    u[int(.5 / dx+1):int(1 / dx + 25/dx)] = 2
    
    fig = plt.figure(figsize=(8,4))
    ims=[]
    for n in range(nt): 
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        if (nt%1==0):
            im = plt.plot(x,u, "r")
            ims.append(im)
    
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("u(m/s)")   
    anim = animation.ArtistAnimation(fig, ims)
    anim.save('movie_reesult.gif', fps=5)
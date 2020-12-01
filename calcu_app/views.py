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
    params = {
        'title': '計算実行プログラム',
        'msg' : 'ここからが計算できます。',
        'param_title' : 'パラメータ設定',
        'setup' : SetupForm()
    }

    nx = requset.POST['nx']
    xmax = requset.POST['xmax']
    c = requset.POST['c']
    alpha = requset.POST['alpha']

    params['title'] = '計算結果'
    params['setup'] = SetupForm(requset.POST)

    AdvectionEquation(nx, xmax ,c , alpha)

    setup ={
        'nx': 'nx',
        'xmax':'xmax',
        'c': 'c',
        'alpha': 'alpha'
    }
    
    return render(requset, 'calcu/result.html', params, setup)

import numpy as np
import matplotlib.pyplot as plt
 
def AdvectionEquation(nx, xmax ,c , alpha):
    nx = nx
    xmax = xmax
    dx = xmax / (nx-1)
    nt = 25
    c = c
    alpha = alpha
    dt = alpha * (dx/c) 
    
    x = np.linspace(0,2,nx)
    
    un = []
    u = np.ones(nx)
    u[int(.5 / dx):int(1 / dx + 1)] = 2
    
    
    for n in range(nt): 
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
    
    u_final = u.copy()
    
    u_initial  = np.ones(nx)
    u_initial[int(.5 / dx):int(1 / dx + 1)] = 2
    
    plt.plot(x,u_initial,label = 'initial')
    plt.plot(x,u_final, label = 'final')
    plt.legend()
    plt.grid()
    # plt.show()
    plt.savefig('figure01.jpg')
    plt.close()
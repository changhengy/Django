from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    # 1 . 直接返回
    # return HttpResponse("Hello world ! ")
    # 2. 直接返回一个 html
    # return render(request, 'base.html')
    # 3. 在html 中欧你设置变量 从context 赋值
    context = {}
    context ["key"] = "欧德郎测试"
    context ["user"] = 2
    # return render(request, 'base.html', context)
    return render(request, 'child.html', context)

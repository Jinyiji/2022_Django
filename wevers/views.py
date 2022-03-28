from django.shortcuts import render

# Create your views here.

def show_정국(request):
    context2 = {
        'name': '전정국',
        'img_src': 'https://img.theqoo.net/img/sWbom.png',
    }
    return render(request, 'wevers/멤버.html', context=context2)


def show_태형(request):
    context3 = {
        'name': '김태형',
        'img_src': 'http://theviewers.co.kr/Files/30/News/202106/2890_20210628124206724.JPG',
    }
    return render(request, 'wevers/멤버.html', context=context3)


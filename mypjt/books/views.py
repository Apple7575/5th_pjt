from django.shortcuts import render

def index(request):
    return render(request, 'books/index.html')

def create(request):
    # 아직 기능이 완성되지 않았다면 임시로 pass를 적거나 빈 페이지를 렌더링하도록 둘 수 있습니다.
    pass
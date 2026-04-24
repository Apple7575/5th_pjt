from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# 1. 전체 도서 조회 (GET 요청만 허용)
@require_safe
def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/index.html', context)

# 2. 도서 데이터 생성 (GET, POST 요청 허용)
@login_required  # 로그인한 사용자만 접근할 수 있도록 제한
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid(): # 유효성 검사 통과 시
            book = form.save()
            return redirect('books:detail', book.pk) # 상세 페이지로 리다이렉트
    else:
        form = BookForm()
    
    # POST 요청이 유효하지 않은 경우, 입력했던 데이터와 에러 메시지를 담은 form이 반환됨
    context = {'form': form}
    return render(request, 'books/create.html', context)

# 3. 단일 도서 상세 조회 (GET 요청만 허용)
@require_safe
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book': book}
    return render(request, 'books/detail.html', context)

# 4. 도서 데이터 수정 (GET, POST 요청 허용)
@login_required  # 로그인된 사용자만 사용 가능
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # 1. 수정할 대상 도서 데이터를 데이터베이스에서 가져옵니다.
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # 2. POST 요청: 사용자가 수정한 데이터를 폼에 넣습니다.
        # 핵심! instance=book 을 넣어줘야 기존 데이터에 덮어쓰기가 됩니다.
        form = BookForm(request.POST, instance=book)
        
        if form.is_valid():
            form.save()
            # 3. 유효한 데이터일 경우 저장 후 상세 페이지로 리다이렉트
            return redirect('books:detail', book.pk)
    else:
        # 4. GET 요청: 폼을 보여줄 때 기존 도서 데이터(instance=book)를 미리 채워 넣습니다.
        form = BookForm(instance=book)
        
    context = {'form': form, 'book': book}
    return render(request, 'books/update.html', context)

# 5. 도서 데이터 삭제 (POST 요청만 허용)
@login_required  # 로그인된 사용자만 접근 가능
@require_POST    # POST 요청만 허용 (GET 요청으로 삭제하는 것을 방지)
def delete(request, pk):
    # 1. 삭제할 대상 도서 데이터를 가져옵니다.
    book = get_object_or_404(Book, pk=pk)
    
    # 2. 데이터를 데이터베이스에서 삭제합니다.
    book.delete()
    
    # 3. 삭제가 완료되면 메인 페이지(index)로 돌아갑니다.
    return redirect('books:index')
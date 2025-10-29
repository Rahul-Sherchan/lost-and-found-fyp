from django.shortcuts import render
from django.http import HttpResponse
from .models import LostItem, FoundItem
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    return render(request, 'lf_app/index.html', {'lost_items': lost_items, 'found_items': found_items})

# Public views - anyone can see (no login required)
def home(request):
    recent_lost = LostItem.objects.filter(is_resolved=False).order_by('-date_posted')[:5]
    recent_found = FoundItem.objects.filter(is_returned=False).order_by('-date_posted')[:5]
    
    return render(request, 'lf_app/home.html', {
        'recent_lost': recent_lost,
        'recent_found': recent_found
    })

def lost_items_list(request):
    items = LostItem.objects.filter(is_resolved=False).order_by('-date_posted')
    return render(request, 'lf_app/lost_items.html', {'items': items})

def found_items_list(request):
    items = FoundItem.objects.filter(is_returned=False).order_by('-date_posted')
    return render(request, 'lf_app/found_items.html', {'items': items})

def item_detail(request, item_type, item_id):
    if item_type == 'lost':
        item = get_object_or_404(LostItem, id=item_id)
        template = 'lf_app/lost_item_detail.html'
    else:
        item = get_object_or_404(FoundItem, id=item_id)
        template = 'lf_app/found_item_detail.html'
    
    return render(request, template, {'item': item})

# Protected views - require login
@login_required
def report_lost_item(request):
    return render(request, 'lf_app/report_lost.html')

@login_required
def report_found_item(request):
    return render(request, 'lf_app/report_found.html')

@login_required
def my_reports(request):
    lost_items = LostItem.objects.filter(reporter=request.user)
    found_items = FoundItem.objects.filter(finder=request.user)
    return render(request, 'lf_app/my_reports.html', {
        'lost_items': lost_items,
        'found_items': found_items
    })

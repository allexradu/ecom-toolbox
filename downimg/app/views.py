from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import forms
from downimg.tasks import process_file, process_split, keyv_process_file
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'app/index.html', {'nav_bar_link_active_index': True})


def keyv(request):
    keyv_form = forms.KeyVForm()
    
    if request.method == 'POST':
        keyv_form = forms.KeyVForm(request.POST, request.FILES)
        
        if keyv_form.is_valid():
            xl_file = request.FILES['d_file']
            f_key_column = request.POST['first_key_column']
            l_value_column = request.POST['last_value_column']
            f_empty_column = request.POST['first_empty_column']
            fs = FileSystemStorage()
            xl_file_name = fs.save(xl_file.name, xl_file)
            return HttpResponseRedirect(
                reverse('keyv_process',
                        args = [f_key_column, l_value_column, f_empty_column, xl_file_name]))
    
    return render(request, 'app/keyv.html', {'nav_bar_link_active_key': True, 'keyv_form': keyv_form})


def keyv_process(request, f_key_column, l_value_column, f_empty_column, xl_file_name):
    task = keyv_process_file.delay(f_key_column, l_value_column, f_empty_column, xl_file_name)
    return render(request, 'app/keyv_result.html', {
        'task_id': task.task_id
    })


def split(request):
    split_form = forms.SplitForm()
    
    if request.method == 'POST':
        split_form = forms.SplitForm(request.POST, request.FILES)
        
        if split_form.is_valid():
            xl_file = request.FILES['d_file']
            split_value = request.POST['split_value']
            fs = FileSystemStorage()
            xl_file_name = fs.save(xl_file.name, xl_file)
            return HttpResponseRedirect(
                reverse('split_process',
                        args = [split_value, xl_file_name]))
    
    return render(request, 'app/split.html', {'nav_bar_link_active_split': True, 'split_form': split_form, })


def split_process(request, split_value, xl_file_name):
    task = process_split.delay(split_value, xl_file_name)
    return render(request, 'app/split_result.html', {
        'task_id': task.task_id
    })


def download(request):
    form = forms.UploadForm()
    
    if request.method == 'POST':
        form = forms.UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            xl_file = request.FILES['d_file']
            url_cell_start = request.POST['url_cell_start']
            url_cell_end = request.POST['url_cell_end']
            write_cell_start = request.POST['write_cell_start']
            write_cell_end = request.POST['write_cell_end']
            fs = FileSystemStorage()
            xl_file_name = fs.save(xl_file.name, xl_file)
            return HttpResponseRedirect(
                reverse('process',
                        args = [url_cell_start, url_cell_end, write_cell_start, write_cell_end, xl_file_name]))
    
    return render(request, 'app/download.html', {'form': form, 'nav_bar_link_active_download': True})


def process(request, url_cell_start, url_cell_end, write_cell_start, write_cell_end, xl_file_name):
    task = process_file.delay(url_cell_start, url_cell_end, write_cell_start, write_cell_end, xl_file_name)
    return render(request, 'app/result.html', {
        'task_id': task.task_id
    })

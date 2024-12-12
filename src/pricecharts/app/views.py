from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden, JsonResponse
from wsgiref.util import FileWrapper

from .data.logmanager import LogManager
from .data.datamanager import DataManager
from .data.fileuploadprocessor import FileUploadProcessor


@login_required
def auth(_) -> HttpResponse:
    return HttpResponse(status=200)


def healthcheck(_) -> JsonResponse:
    return JsonResponse({'status': 'ok'})


@login_required
def custom_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/')


@login_required
def logs(request: HttpRequest) -> HttpResponse:
    manager = LogManager()
    if request.method == 'POST':
        manager.delete_messages()
    return render(request, 'logs.html', context={'messages': manager.get_messages()})


@login_required
def filesets(request: HttpRequest) -> HttpResponse:
    manager = DataManager()
    if request.method == 'POST':
        fileset_name = request.POST.get('fileset_name', None)
        file_paths, file_names = FileUploadProcessor().process_upload(request)
        manager.create_fileset_from_files(file_paths, file_names, fileset_name, request.user)
    return render(request, 'filesets.html', context={'filesets': manager.get_filesets(request.user)})


@login_required
def fileset(request: HttpRequest, fileset_id: str) -> HttpResponse:
    manager = DataManager()
    action = None
    if request.method == 'GET':
        fs = manager.get_fileset(fileset_id)
        action = request.GET.get('action', None)
        if action == 'download':
            zip_file_path = manager.get_zip_file_from_fileset(fs)
            with open(zip_file_path, 'rb') as f:
                response = HttpResponse(FileWrapper(f), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="{}.zip"'.format(fs.name)
            return response
        elif action == 'delete':
            manager.delete_fileset(fs)
            return render(request, 'filesets.html', context={'filesets': manager.get_filesets(request.user)})
        elif action == 'rename':
            fs = manager.rename_fileset(fs, request.GET.get('new_name'))
        elif action == 'make-public':
            fs = manager.make_fileset_public(fs)
        elif action == 'make-private':
            fs = manager.make_fileset_public(fs, public=False)
        else:
            pass
        return render(request, 'fileset.html', context={'fileset': fs, 'files': manager.get_files(fs)})
    return HttpResponseForbidden(f'Wrong method ({request.method}) or action ({action})')
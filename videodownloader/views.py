# from django.template import loader, RequestContext
# from django.shortcuts import render, render_to_response

# import os.path
# # from django.contrib import messages
# from django.http import HttpResponse
# # Descarga 
# import pafy
# # AJAX petition
# from django.http import JsonResponse
# # from django.core.exceptions import SuspiciousOperation

# from celery import shared_task, task
# from celery_progress.backend import ProgressRecorder
# import time

# def index(request):
#     if request.method == 'POST':
#         url = request.POST.get('link')
#         video = pafy.new(url)
#         formatos = video.streams
#         return render(request, 'index.html', {'video': video, 'streams': formatos})
#     return render(request,'index.html')
   
# def mycb(total, recvd, ratio, rate, eta):
#     print(recvd, ratio, eta)

# def download_By_Itag(request):
#     if request.method == 'GET':
#         itag = request.GET.get('itag')
#         id_video = request.GET.get('id-video')
#         url = 'https://www.youtube.com/watch?v=' + id_video
#         video = pafy.new(url)
#         streams = video.streams
#         home_dir = os.path.expanduser('~')
#         dir_final = home_dir + '/Downloads/'
#         for s in streams:
#             if(s.itag == itag):
#                 print("Descargando: " + video.title + '.' + s.extension)
#                 print("Stream: " + s.itag)
#                 s.download(filepath = dir_final, callback = mycb)
#                 break
#             else:
#                 print("No se encontro el Stream")

#         data = {'valueNew': "Iniciando Descarga"}
#         return JsonResponse(data)

# @task
# def my_task():

#     print("step: 1")
#     i = 0
#     while(i < 1000):
#         print("step: 2")
#         i = i + 1
#     print("Finish")

#     return 'work is complete'

# def prueba(request):
#     if request.method == 'GET':
#         print("I'am entering...")
#         my_task.delay()
#         print("I'am leaving...")
    
#         # result = my_task.delay(10)
#         data = {'valueNew': "Iniciando Descarga"}
#         return JsonResponse(data)
#         # return HttpResponse('work kicked off!')


# from time import sleep
# from celery import shared_task, current_task
# from celery import task

# # @shared_task
# @task
# def timer_working():
#     print("ENTRE")
#     i = 0
#     while(i <= 10000000):
#         # process_percent = int(100 * float(i) / float(n))
#         i += 1
#         # current_task.update_state(state='PROGRESS',
#         # meta={'process_percent': process_percent})
#         # print(process_percent)
#         print(i)
#         sleep(1)
#     return ("Done")

# def timer(request):
#     print("VOY A ENTRAR")
#     timer_working.delay()
#     print("SALÍ")
#     return render(request, 'timer.html')
#     # , {'text' : 'Iniciated work'}
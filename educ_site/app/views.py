import os
import shutil
import tempfile
import zipfile 
from zipfile import ZipFile
from io import BytesIO
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from .models import Learning, Videos, Activity
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def activity_grade_1(request):
    activity = Activity.objects.all()
    quiz = Videos.objects.all()
    learning = Learning.objects.all()

    context = {
        'activities': activity,
        'quizzes': quiz,
        'learnings':learning,
        'activities_exist': activity.exists(),
        'quizzes_exist': quiz.exists(),
        'learnings_exist': learning.exists(),
    }

    return render(request,'grade_1-2.html',context)

def activity_grade_3(request):
    activity = Activity.objects.filter(grade_level__in=[3, 4])
    quiz = Videos.objects.filter(grade_level__in=[3, 4])
    learning = Learning.objects.filter(grade_level__in=[3, 4])

    context = {
        'activities': activity,
        'quizzes': quiz,
        'learnings':learning,
        'activities_exist': activity.exists(),
        'quizzes_exist': quiz.exists(),
        'learnings_exist': learning.exists(),
    }

    return render(request,'grade_3-4.html',context)

def activity_grade_5(request):
    activity = Activity.objects.filter(grade_level__in=[5, 6])
    quiz = Videos.objects.filter(grade_level__in=[5, 6])
    learning = Learning.objects.filter(grade_level__in=[5, 6])

    context = {
        'activities': activity,
        'quizzes': quiz,
        'learnings':learning,
        'activities_exist': activity.exists(),
        'quizzes_exist': quiz.exists(),
        'learnings_exist': learning.exists(),
    }

    return render(request,'grade_5-6.html',context)
    

def download_education(request):
    # Create a temporary directory to hold the files
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'Education_Folder')
    os.makedirs(temp_dir, exist_ok=True)

    # Define grade levels and their folder names
    grade_levels = {
        '1-2': range(1, 3),
        '3-4': range(3, 5),
        '5-6': range(5, 7),
    }

    # Copy files for each model and grade level to the appropriate subfolder
    for grade_folder, grades in grade_levels.items():
        grade_dir = os.path.join(temp_dir, f'Grade_{grade_folder}')
        os.makedirs(grade_dir, exist_ok=True)
        for model_class in [Learning, Videos, Activity]:
            model_folder_name = model_class.__name__
            model_dir = os.path.join(grade_dir, model_folder_name)
            os.makedirs(model_dir, exist_ok=True)
            objects = model_class.objects.filter(grade_level__in=grades)
            for obj in objects:
                try:
                    file_name = str(obj.content).split('/')[-1]  # Extract the file name from the URL
                    file_path = os.path.join(model_dir, file_name)
                    with open(file_path, 'wb') as file:
                        file.write(obj.content.read())  # Write the file content to the temporary directory
                    print(f"Saved file {file_name} to {model_folder_name} in Grade {grade_folder}")
                except Exception as e:
                    print(f"Error processing file for {model_folder_name} in Grade {grade_folder}: {e}")

    # Create a zip file from the temporary directory
    zip_file_path = os.path.join(settings.MEDIA_ROOT, 'Education_Folder.zip')
    with ZipFile(zip_file_path, 'w') as zip_file:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, temp_dir))

    # Serve the zip file for download
    with open(zip_file_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="Education_Folder.zip"'

    # Clean up the temporary directory and zip file
    shutil.rmtree(temp_dir)
    os.remove(zip_file_path)

    return response

def view_activity(request, activity_id):
    try:
        activity = Activity.objects.get(id=activity_id)
        file_path = activity.content.path
        file_name = activity.content.name.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{file_name}"'
        return response
    except Activity.DoesNotExist:
        raise Http404("Activity not found")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)


def download_activity(request, activity_id):
    try:
        activity = Activity.objects.get(id=activity_id)
        file_path = activity.content.path
        file_name = activity.content.name.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    except Activity.DoesNotExist:
        raise Http404("Activity not found")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

def view_quiz(request, quiz_id):
    try:
        quiz = Videos.objects.get(id=quiz_id)
        file_path = quiz.content.path
        file_name = quiz.content.name.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = f'inline; filename="{file_name}"'
        return response
    except Activity.DoesNotExist:
        raise Http404("Activity not found")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)


def download_quiz(request, quiz_id):
    try:
        quiz = Videos.objects.get(id=quiz_id)
        file_path = quiz.content.path
        file_name = quiz.content.name.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    except Activity.DoesNotExist:
        raise Http404("Activity not found")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

def view_learning(request, learning_id):
    try:
        learning = Learning.objects.get(id=learning_id)
        file_path = learning.content.path
        file_name = learning.content.name.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{file_name}"'
        return response
    except Activity.DoesNotExist:
        raise Http404("Activity not found")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)


def download_learning(request, learning_id):
    try:
        learning = Learning.objects.get(id=learning_id)
        file_path = learning.content.path
        file_name = learning.content.name.split('/')[-1]
        response = FileResponse(open(file_path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    except Activity.DoesNotExist:
        raise Http404("Activity not found")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

def search(request):
    query = request.GET.get('q', '')
    activities = Activity.objects.filter(name__icontains=query)
    quizzes = Videos.objects.filter(name__icontains=query)
    learnings = Learning.objects.filter(name__icontains=query)
    
    context = {
        'query': query,
        'activities': activities,
        'quizzes': quizzes,
        'learnings': learnings,
        'activities_exist': activities.exists(),
        'quizzes_exist': quizzes.exists(),
        'learnings_exist': learnings.exists(),
    }

    return render(request, 'grade_1-2.html', context)

def readMore(request):
    return render(request, 'readMore.html')
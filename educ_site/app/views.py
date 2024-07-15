import os
import shutil
import tempfile
import zipfile 
from zipfile import ZipFile
import io
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from .models import Learning, Videos, Activity
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def filipinoPageG1AndG2(request):
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
    return render(request,'Filipino_g1-2.html',context)

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

def filipinoPageG3AndG4(request):
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
    return render(request,'Filipino_g3-4.html',context)

def activity_grade_3(request):
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

    return render(request,'grade_3-4.html',context)

def filipinoPageG5AndG6(request):
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
    return render(request,'Filipino_g5-6.html',context)

def activity_grade_5(request):
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

    return render(request,'grade_5-6.html',context)
    

def download_education(request):
      # Create an in-memory bytes buffer
    in_memory_zip = io.BytesIO()

    # Define grade levels and their folder names
    grade_levels = {
        '1-2': range(1, 3),
        '3-4': range(3, 5),
        '5-6': range(5, 7),
    }

    # Define the subjects
    subjects = ['English', 'Filipino']

    with ZipFile(in_memory_zip, 'w') as zip_file:
        # Copy files for each grade level and subject to the appropriate subfolder in the zip
        for grade_folder, grades in grade_levels.items():
            for subject in subjects:
                objects = Learning.objects.filter(grade_level__in=grades, subject=subject)
                for obj in objects:
                    if obj.subject in subjects:  # Ensure the subject is valid
                        try:
                            file_name = str(obj.content).split('/')[-1]  # Extract the file name from the URL
                            file_content = obj.content.read()  # Read the file content
                            # Create a file path within the zip
                            file_path = f'Grade_{grade_folder}/{subject}/{file_name}'
                            zip_file.writestr(file_path, file_content)
                            print(f"Added file {file_name} to zip in Grade {grade_folder} under {subject}")
                        except Exception as e:
                            print(f"Error processing file for Learning in Grade {grade_folder} under {subject}: {e}")

    # Prepare the response
    in_memory_zip.seek(0)
    response = HttpResponse(in_memory_zip.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="Education_Files.zip"'
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

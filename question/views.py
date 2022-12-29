from django.shortcuts import render, redirect
from .models import *
from .forms import *



def home_view(request):
    
    # get all subjects
    subjects = Subject.objects.all()
    # get questions order by id last first
    questions = Question.objects.all().order_by('-id')
    # question count
    question_count = questions.count()

    context = {
        'page_subject': "home",
        'subjects_list': subjects,
        'questions': questions,
        'question_count': question_count,
    }


    return render(request, 'questions.html', context)


def subject_view(request, subject_id):
    # get all subjects
    subjects = Subject.objects.all()
    # get questions from the first subject
    questions = Question.objects.filter(subject=subject_id)
    subject =  Subject.objects.get(id=subject_id)
    # question count
    question_count = questions.count()

    context = {
        'page_subject': subject.name,
        'subjects_list': subjects,
        'questions': questions,
        'question_count': question_count,
    }


    return render(request, 'questions.html', context)

def question_view(request, question_id):
    # get all subjects
    subjects = Subject.objects.all()
    # get questions from the first subject
    questions = Question.objects.filter(id=question_id)

    context = {
        'subjects_list': subjects,
        'questions': questions,
    }


    return render(request, 'questions.html')

def add_question(request):
    if request.POST:
        questionForm = QuestionForm(request.POST, request.FILES)
        if questionForm.is_valid():
            questionForm.save()
            return redirect('home')

    else:
        questionForm = QuestionForm()
        context = {
            'page_subject': "Add Question",
            'questionForm': questionForm,
            'subjects_list': Subject.objects.all(),
        }
        return render(request, 'form.html', context)


def add_subject(request):
    if request.POST:
        subjectForm = SubjectForm(request.POST)
        if subjectForm.is_valid():
            subjectForm.save()
            return redirect('home')

    else:
        subjectForm = SubjectForm()
        context = {
            'page_subject': "Add Subject",
            'questionForm': subjectForm,
            'subjects_list': Subject.objects.all(),
        }
        return render(request, 'form.html', context)


def edit_question(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.POST:
        questionForm = QuestionForm(request.POST, request.FILES, instance=question)
        if questionForm.is_valid():
            questionForm.save()
            return redirect('home')

    else:
        questionForm = QuestionForm(instance=question)
        context = {
            'page_subject': "Edit Question",
            'questionForm': questionForm,
            'subjects_list': Subject.objects.all(),
        }
        return render(request, 'form.html', context)


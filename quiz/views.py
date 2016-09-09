from django.shortcuts import render

from quiz.models import Quiz


def startpage(request):
	context = {
	    	"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    	"question": "Which is the most hipster city in the world?",
		"answer1": "Stockholm, Sweden",
	   	"answer2": "Williamsburg, Brooklyn, New York",
	    	"answer3": "Barcelona, Spain",
	    	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def completed(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)



# Create your views here.

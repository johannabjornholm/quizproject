from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "WWHD – what would hipsters do?",
	   	"description": "So, are the hipsters the ones who would only buy the cheapest drinks? Or are they the ones that are all into computers and tech? Or what was it… Well, give these questions a try and see how good you are!"
	},
	{
		"quiz_number": 2,
   	   	"name": "Where do they go?",
	   	"description": "So all these cool hipsters, where are they!?"
	},
	{
		"quiz_number": 3,
   	    	"name": "Hipster beards",
	    	"description": "The hipster beard is a big trend these days and should stick around at least for the winter.  If you're unsure what a hipster beard is, you have seen it, I promise! Try to think about it for a minute and then try the quiz. You will rock!"	},
]


def startpage(request):
	context = {
		"quizzes": quizzes,
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

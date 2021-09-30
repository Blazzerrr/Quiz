# from django.shortcuts import render
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Answer, Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

class QuizView(APIView):
    def get(self, request):
        quizes = Quiz.objects.all()
        serializer = QuizSerializer(quizes, many=True)

        return Response({"quizes": serializer.data})


class QuestionView(APIView):
    def get(self, request):
        quiz_id = request.data.get('quiz_id')

        # If quiz_id is uncorrect
        if quiz_id is None:
            return Response({"error": "quiz_id undefined"}, status=400)

        # Get all questions from quiz
        questions = Question.objects.filter(quiz_id=quiz_id)
        serializer = QuestionSerializer(questions, many=True)

        return Response({"questions": serializer.data})


class AnswerView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        question_id = request.data.get('question_id')
        text = request.data.get('text')

        # If user don't send one of the required data
        if (user_id is None) or (question_id is None) or (text is None): 
            return Response({"error": "undefined value, check what you are sending user_id, question_id and text"}, status=400)

        # Try get question from Question
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist: # If question_id is uncorrect
            return Response({"error": "not valid question_id"}, status=400)

        # Try get answer from Answer that check if the user has already sent a response
        try:
            answer = Answer.objects.get(user_id=user_id, question_id=question_id)
            return Response({"error": "you already sent a reply"}, status=400)
        except Answer.DoesNotExist: # If user didn't respond, just skip it 
            pass

        serializer = QuestionSerializer(question, many=False)
        quiz_id = serializer.data['quiz_id'] # Get quiz_id for save answer
        type = serializer.data['type'] # Get type for check what the user send

        # Get quiz for check date_ended and date_started
        quiz = Quiz.objects.get(id=quiz_id)
        serializer = QuizSerializer(quiz, many=False)
        date_started = serializer.data['date_started']
        date_ended = serializer.data['date_ended']
        date_now = datetime.now()

        # Convert str to datetime
        date_started = datetime.strptime(date_started, '%d-%m-%Y')
        date_ended = datetime.strptime(date_ended, '%d-%m-%Y')

        if date_now < date_started: # If quiz not started
            return Response({"error": "quiz not started yet"}, status=400)
        elif date_now > date_ended: # If quiz alreade ended
            return Response({"error": "quiz has already ended"}, status=400)

        # If the answer to the question can only be numeric    
        if type == '2' or type == '3':
            if text.isdigit() is False: # If the text is not a numeric
                return Response({"error": "question supports only numeric answer"}, status=400)

        # Add answer
        answer = Answer(user_id=user_id, quiz_id=quiz_id, question_id=question_id, text=text)
        answer.save()

        return Response({"success": "answer added"})


class UserView(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        quiz_id = request.data.get('quiz_id')

        # If user don't send one of the required data
        if (user_id is None) or (quiz_id is None): 
            return Response({"error": "undefined value, check what you are sending user_id and quiz_id"}, status=400)

        # Get all answers from Answer
        answers = Answer.objects.filter(user_id=user_id, quiz_id=quiz_id)
        serializer = AnswerSerializer(answers, many=True)

        return Response({"answers": serializer.data})
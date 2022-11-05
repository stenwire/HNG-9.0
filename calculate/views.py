
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

add_words = ['+', 'add', 'addition']
sub_words = ['-', 'subtract', 'minus', 'takeaway', 'subtraction']
div_words = ['/', 'divide', 'division']
mult_words = ['*', 'multiply', 'multiplication']

class Calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

class CalculateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            x = request.data.get("x")
            y = request.data.get("y")
            operation_type = request.data.get("operation_type")
            operation_list = operation_type.split()
        except:
            message = {"message": "Invalid Request"}
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

        for op in operation_list:
            if op in add_words:
                op_type = op
                result = Calculator.add(x, y)
            if op in sub_words:
                op_type = op
                result = Calculator.subtract(x, y)
            if op in div_words:
                op_type = op
                result = Calculator.divide(x, y)
            if op in mult_words:
                op_type = op
                result = Calculator.multiply(x, y)

        res = {
            "slackUsername": "Rougue_Astronaut",
            "result": int(result),
            "operation_type": op_type
        }

        return JsonResponse(res, status=status.HTTP_200_OK)

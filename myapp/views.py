from django.shortcuts import render
import joblib
# Create your views here.

def index(request):
    return render(request, 'myapp/index.html', {})

def result(request):
    age = int(request.POST.get("age"))
    gender = int(request.POST.get("gender"))
    input_data = [age,gender]
    model = joblib.load("muzika.joblib")
    prediction = model.predict([input_data])
    return render(request,'myapp/index.html',{'age':age,'gender':gender,'prediction':prediction[0]})



from django.shortcuts import render
import joblib
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



model = joblib.load('spam_model.pkl')

@csrf_exempt
def predict_spam(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            prediction = model.predict([message])[0]

            return JsonResponse({'spam':bool(prediction)})  

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'index.html')

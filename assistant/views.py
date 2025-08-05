from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import os
from dotenv import load_dotenv
 
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-2.5-pro")



def chat_interface(request):
    return render(request, 'assistant/chat_interface.html')

@csrf_exempt
def ask_gpt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code', '')

        prompt = f"Debug or explain this Python code:\n\n{code}"

        # try:
        #     response = model.generate_content(
        #         model="gpt-3.5-turbo",
        #         messages=[
        #             {"role": "user", "content": prompt}
        #         ]
        #     )
        #     reply = response['choices'][0]['message']['content']
        #     return JsonResponse({'reply': reply})
        # except Exception as e:
        #     return JsonResponse({'reply': f"Error: {str(e)}"})
        try:
            response = model.generate_content(prompt)
            reply = response.text
            return JsonResponse({'reply': reply})
        except Exception as e:
            return JsonResponse({'reply': f"Error: {str(e)}"})


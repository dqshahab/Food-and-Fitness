from django.shortcuts import render
from django.http import HttpResponse
import json
import os

# View for rendering the category selection form
def category_selection(request):
    return render(request, 'workout.html')

# View for displaying workout plan based on selected category
def display_workout(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        # Logic to fetch workout data based on selected category
        # This could be replaced with actual data retrieval from a database
        print(os.path)
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'workout_data.json')

        with open(data_path) as js:
            data= json.loads(js.read())
        workout_data = data['categories']
        for i in workout_data:
            if i['category_name'] == category:
                workouts=i['workout_plan']
                break
        else:
            workouts=[]
        return render(request, 'day.html', {'category': category, 'workouts': workouts})
    else:
        return HttpResponse('Invalid request')

from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from charts.models import Data
from .serializer import DataSerializer
from rest_framework.views import APIView
from django.views import View
import pandas as pd
import numpy as np
import json

# Create your views here.
    
class MoviesClass(APIView):
    
    def preprocess(self,category,replace_val):
        try:
            category.fillna(replace_val, inplace=True)
            categories = list(category)
            return categories
        except Exception as e:
            return {"error": f"Error running CCExtractor: {str(e)}"}

    def post(self,request):
        main = MoviesClass()
        df = pd.read_csv("data/assignment_movies.csv")
        movies = main.preprocess(df['MOVIES'],'empty')
        year = main.preprocess(df['YEAR'],0)
        gener = main.preprocess(df['GENRE'],'empty')
        rating = main.preprocess(df['RATING'],0)
        one_line = main.preprocess(df['ONE-LINE'],'empty')
        stars = main.preprocess(df['STARS'],'empty')
        votes = main.preprocess(df['VOTES'],0)
        run_time = main.preprocess(df['RunTime'],0)
        gross = main.preprocess(df['Gross'],0)

        i = 0
        for movie in movies:
            gross_uv = str(gross[i]) # gross updated value
            gross_str = gross_uv.replace('$', '').replace(',', '')
            # Check if the value ends with 'M' or 'B'
            if gross_str.endswith('M'):
                gross_value = float(gross_str[:-1]) * 1e6  # Convert million to numeric value
            elif gross_str.endswith('B'):
                gross_value = float(gross_str[:-1]) * 1e9  # Convert billion to numeric value
            else:
                gross_value = float(gross_str)  # Handle other cases directly
            
            votes_str = str(votes[i])
            votes_int = int(votes_str.replace(',', ''))
            new_data = Data(movies=movies[i], year=year[i], genre=gener[i], rating=rating[i], one_line=one_line[i], stars=stars[i], votes=votes_int, run_time=run_time[i], gross=gross_value)
            new_data.save()
            i = i+1
        return render(request, 'index.html')

    def get(self,request):
        qs = Data.objects.all()
        year = None
        apps = None
        limit = 5
        print(request.query_params)
        if request.query_params.get('year'):
            year = request.query_params.get('year')
            qs = qs.filter(year=year).order_by('-gross')[:limit]
        elif request.query_params.get('votes'):
            qs = qs.order_by('-votes')[:limit].values()
        elif request.query_params.get('ratingyear'):
            year = request.query_params.get('ratingyear')
            limit = 10
            qs = qs.filter(year=year).order_by('-rating')[:limit].values()
        
        apps = qs.values()
        categories = {}
        if apps is not None:
            for i in range(1, limit):
                try:
                    categories[i] = apps[i]
                except IndexError:
                    print(f"Index {i} is out of range")
            context = {"categories": json.dumps(categories)}
        else:
            context = {"categories": categories}
        return Response(context)
    

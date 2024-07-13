from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def proxy_api_request(request):
    # Proxy API request to server running on port 8000
    url = 'http://localhost:8080' + request.path
    response = requests.request(request.method, url, headers=request.headers, data=request.body)
    
    # Return the response from the API server
    return response.content, response.status_code
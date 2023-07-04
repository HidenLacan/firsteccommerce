# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>This part of code must be a new page</h1>
        
        </body>
    </html>
    '''
    return HttpResponse(html)
from django.shortcuts import render

# Create your views here.
from .models import Document

def editor(request):
    docid=int(request.GET.get('docid',0))
    documents=Document.objects.all()
    context={
        'docid':docid,
        'documents':documents
    }
    print(docid)
    return render(request,'editor.html',context)
    

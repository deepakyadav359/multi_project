from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

peoples = [
    {'name':'Abhijeet Gupta','age':26},
    {'name':'Rohan Sharma','age':23},
    {'name':'Vicky Kaushal','age':17},
    {'name':'Deepanshu Chaurasiya','age':16},
    {'name':'Sandeep','age':63},
]

text="""
Lorem, ipsum dolor sit amet consectetur adipisicing elit. In illum at eius perferendis laboriosam doloremque, veniam voluptatem debitis illo ducimus ipsa quibusdam. Adipisci similique nihil laboriosam ab laudantium nemo placeat sequi et possimus sit maxime suscipit, iste exercitationem incidunt laborum dolorum pariatur vel quas corrupti fuga ipsum dolores maiores! Cupiditate molestiae deleniti a iure, expedita aliquam earum itaque sunt cum aperiam hic nobis voluptas debitis natus ab in officia tempore assumenda repellendus magni. Aliquid eius nam recusandae labore praesentium explicabo dolorum suscipit optio voluptate perferendis cumque voluptatibus, totam possimus unde laudantium distinctio eum odit corporis atque eveniet? Consequatur, accusamus? Explicabo!
"""
vegetables=['pumpkin','tomato','potato']

def home(request):
     
     return render(request ,"home/index.html",context ={'page': 'django tutorial','peoples': peoples,'text':text , 'vegetables':vegetables})

def contact(request):
     context={'page':'contact'}
     
     return render(request ,"home/contact.html" , context) 

def about(request):
     context={'page':'about'}
     return render(request ,"home/about.html" , context) 


def success_page(request):
    print("*"*10)
    return HttpResponse("<h1> Hey this is a Success page</h1>")
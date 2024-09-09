import markdown2, random
from django import forms
from django.shortcuts import render
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def isEmpty(obj):
    if obj == None:
        return True
    return len(obj) == 0

def error(request, message):
    return render(request,"encyclopedia/error.html", {"message" : message} )

def mdToHtml(mdFile):
     if mdFile != None:
        return markdown2.Markdown().convert(mdFile)
     return None

def getEntry(request, entryName):
     entry = util.get_entry(entryName)
     if entry != None:
          content = mdToHtml(entry)
          return render(request, "encyclopedia/title.html", {"content" : content, "title": entryName})
     return error(request, "Page was not found!")

def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        if isEmpty(query):
            return error(request, "Search query cannot be empty!")
        possibleResults = []
        for entry in util.list_entries():
            if entry == query:
                return getEntry(request, query)
            elif query in entry:
                possibleResults.append(entry)
        return render(request, "encyclopedia/search.html", {
            "results" : possibleResults
        })
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if isEmpty(title) or isEmpty(content):
            return error(request, "content and title cannot be empty!")
        if not isEmpty(util.get_entry(title)):
            return error(request, "Page with the same title already exists!")
        else:
            util.save_entry(title, content)
            return getEntry(request, title)
    return render(request, "encyclopedia/create.html")

def edit(request, pageTitle):
        if request.method =="POST":
            content = request.POST["content"]
            if isEmpty(content):
                return error(request, "content cannot be empty!") 
            util.save_entry(pageTitle, content)
            return getEntry(request, pageTitle)  
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": pageTitle, 
                "content" :util.get_entry(pageTitle)
            })
def rndm(request):
    pages = util.list_entries()
    length = len(pages)
    randomNumber = random.randint(1, length - 1)
    return getEntry(request, pages[randomNumber])



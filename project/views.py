from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, IdeaForm
from .models import Idea
#from django.contrib.auth.decorators import login_required
# Create your views here.

#view to go to index page
def index(request):
	#return index page
	return render(request, 'project/index.html', {})

#view to logout
@login_required
def logout (request):
    #log user out and return to index
    logout(request,'project/index.html')
    return render(request, 'project/index.html',{})

#view to login user
def login_user(request):
    #TODO fix login error messages
    login_error = False 
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:		            	
                login(request, user)
            else:
                login_error = False
        else:
            login_error = True
    
    return render(request, 'project/index.html', {'login_error':login_error})


#meant for testing purposes returns html that prins hello world
def blank(request):

		return render(request, 'project/blank.html', {})

#view to register user
def register(request):

    #boolean to check if user is registered
    registered = False

    if request.method == 'POST':
        #obtain user's info after they fill in their data
        user_form = UserForm(data=request.POST)
        #check if user enter valid data
        if user_form.is_valid():
            #save user data
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            #authenticate after signup
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect (index)	
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'project/registration.html', {'user_form': user_form , 'registered': registered} )
@login_required
def likeIdea(request, pk):
	idea = get_object_or_404(Idea, pk=pk)
	idea.likes += 1
	idea.save()
	return redirect(ideaListing)
@login_required
def dislikeIdea (request, pk):
	idea = get_object_or_404(Idea, pk=pk)
	idea.dislikes +=1
	idea.save()
	return redirect(ideaListing)

#view after submitting an Idea
@login_required
def submittedIdea (request):
	return render(request, 'project/submittedidea.html')
#Lists pages of Ideas
def ideaListing(request):
    idea_list = Idea.objects.all()
    paginator = Paginator(idea_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        ideas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ideas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ideas = paginator.page(paginator.num_pages)

    return render(request, 'project/idealist.html', {"ideas": ideas})

#Idea submission view
def idea(request):
	if request.user.is_authenticated():
		idea_form=IdeaForm(data=request.POST)
		if idea_form.is_valid():
			idea= idea_form.save(commit=False)
			# ensure the idea is associated with the user logged in
			idea.author= request.user
			idea.save()
			return redirect(submittedIdea)
		else:
			print (idea_form.errors)
	else:
		idea_form= IdeaForm()
	return render(request, 'project/ideasubmission.html', {'idea_form': idea_form})
			
			
			
			
			
			
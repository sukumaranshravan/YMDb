from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from app_admin.models import *
import datetime
import random

# Create your views here.
def home(request):
    my_id=request.session['yourself']
    user=RegisterTb.objects.filter(id=my_id)
    all_reviews=ReviewTb.objects.all()
    reviews=ReviewTb.objects.all()[:1]
    return render(request,'user/home.html',{'see':user,'post':reviews})

def shows(request):
    shows=ShowTb.objects.filter()
    return render(request,'user/shows.html',{'see':shows})

def sign_out(request):
    request.session.flush()
    return redirect('start_up')

def add_show(request):
    categories=CategoryTb.objects.filter()
    return render(request,'user/add_show.html',{'key':categories})

def add_showaction(request):
    title=request.POST['title']         
    poster=request.FILES['poster']             
    user_id=request.session['yourself']   
    category=request.POST['category'] 
    genre=request.POST['genre'] 
    released=request.POST['released'] 
    language=request.POST['language'] 
    rating=request.POST['rating'] 
    director=request.POST['director'] 
    story=request.POST['story'] 
    add_show=ShowTb(title=title,poster=poster,genre=genre,released=released,language=language,rating=rating,director=director,story=story,category_id=category,user_id_id=user_id)
    add_show.save()
    messages.add_message(request,messages.INFO,"show added successfulluy.")
    return redirect('add_show')

def review(request):
    return render(request,'user/review.html')

def post_review(request):
    my_id=request.session['yourself']
    title=request.POST['title']
    content=request.POST['content']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    poster=request.FILES['poster']
    post_me=ReviewTb(title=title,content=content,date=date,time=time,poster=poster,user_id_id=my_id)
    post_me.save()
    return redirect('home')

def view_review(request):
    reviews=ReviewTb.objects.filter().order_by('-time')
    return render(request,'user/view_review.html',{'see':reviews})

def show_details(request,id):
    details=ShowTb.objects.filter(id=id)
    return render(request,'user/show_details.html',{'see':details})

def my_reviews(request):
    my_id=request.session['yourself']
    my_review=ReviewTb.objects.filter(user_id_id=my_id)
    if my_review.count()>0:
        return render(request,'user/my_reviews.html',{'see':my_review})
    else:
        show_msg="You have'nt reviewed a show yet."
        return render(request,'user/my_reviews.html',{'msg':show_msg})

def edit_review(request,id):
    change=ReviewTb.objects.filter(id=id)
    return render(request,'user/edit_review.html',{'update':change})

def update_review(request):
    id=request.POST['id']    
    title=request.POST['title']
    content=request.POST['content']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    try:
        poster=request.FILES['poster']
        ReviewTb.objects.filter(id=id).update(title=title,content=content,date=date,time=time,poster=poster)      
        return redirect('my_reviews')
    except:
        ReviewTb.objects.filter(id=id).update(title=title,content=content,date=date,time=time)       
        return redirect('my_reviews')
    

def delete_review(request,id):
    ReviewTb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Selected review has been deleted.")
    return redirect('my_reviews')

def add_to_watchlist(request):
    show_id=request.POST['id']
    my_id=request.session['yourself']
    check_list=WatchlistTb.objects.filter(user_id_id=my_id,show_id_id=show_id)
    if check_list.count()>0:
        messages.add_message(request,messages.INFO,"This Show is already in your watchlist.")
        return redirect('shows')
    else:
        create=WatchlistTb(show_id_id=show_id,user_id_id=my_id)
        create.save()
        messages.add_message(request,messages.INFO,"Added to your Watchlist.")
        return redirect('shows')

def watchlist(request):
    my_id=request.session['yourself']
    my_watchlist=WatchlistTb.objects.filter(user_id_id=my_id)
    if my_watchlist.count()>0:
        return render(request,'user/watchlist.html',{'see':my_watchlist})
    else:
        show_msg="You have'nt created a watchlist yet,"
        return render(request,'user/watchlist.html',{'msg':show_msg})

def remove_from_watchlist(request,id):
    WatchlistTb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Show removed from your watchlist")
    return redirect('watchlist')

def personal(request):
    my_id=request.session['yourself']
    me=RegisterTb.objects.filter(id=my_id)
    return render(request,'user/personal.html',{'see':me})

def edit_personal(request):
    my_id=request.session['yourself']
    name=request.POST['name']
    mail=request.POST['email']
    phone=request.POST['mobile']
    password=request.POST['password']
    RegisterTb.objects.filter(id=my_id).update(name=name,email=mail,mobile=phone,password=password)
    messages.add_message(request,messages.INFO,"Details updated.")
    return redirect('home')

def delete_account(request):
    my_id=request.session['yourself']
    # # to save my show we need to update the user_id of me as any other number
    # ShowTb.objects.filter(user_id_id=my_id).update(user_id_id=0)
    RegisterTb.objects.filter(id=my_id).delete()
    messages.add_message(request,messages.INFO,"Your Account has been permenantly Deleted!!")
    return render(request,'admin/start_up.html')

def search(request):
    key_word=request.POST['search']
    results=ShowTb.objects.filter(title__istartswith=key_word) |ShowTb.objects.filter(genre__istartswith=key_word) |ShowTb.objects.filter(released__istartswith=key_word)|ShowTb.objects.filter(director__istartswith=key_word)
    if results.count()>0:
        return render (request,'user/shows.html',{'see':results})
    else:
        msg="Sorry No Results Found."
        return render (request,'user/shows.html',{'show':msg})
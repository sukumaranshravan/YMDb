from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name="home"),
     path('shows/',views.shows,name="shows"),
    path('add_show/',views.add_show,name="add_show"),
    path('add_showaction/',views.add_showaction,name="add_showaction"),
    path('sign_out/',views.sign_out,name="sign_out"),
    path('review/',views.review,name="review"),
    path('post_review/',views.post_review,name="post_review"),
    path('view_review/',views.view_review,name="view_review"),
    path('show_details<int:id>/',views.show_details,name="show_details"),
    path('my_reviews/',views.my_reviews,name="my_reviews"),
    path('edit_review<int:id>/',views.edit_review,name="edit_review"),
    path('delete_review<int:id>/',views.delete_review,name="delete_review"),
    path('update_review/',views.update_review,name="update_review"),
    path('add_to_watchlist/',views.add_to_watchlist,name="add_to_watchlist"), 
    path('watchlist/',views.watchlist,name="watchlist"), 
    path('remove_from_watchlist<int:id>/',views.remove_from_watchlist,name="remove_from_watchlist"),   
    path('personal/',views.personal,name="personal"), 
    path('edit_personal/',views.edit_personal,name="edit_personal"), 
    path('delete_account/',views.delete_account,name="delete_account"), 
    path('search/',views.search,name="search"),


]
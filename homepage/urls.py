from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  
    path("", views.index, name="login"),
    path('loggedin/', views.loggedIn, name="loggedin" ),
    path('logout/', views.logoutUser, name="logout" ),
    path('register/', views.registerUser, name="register" ),
    path('about/', views.abbouthome, name="about" ),
    # path('feedback/', views.feedback, name="feedback" )
    
]


#Backend Customer, Main App - Sreyans ::Worked on Making Models, Views and Urls of these app
#Backend Homepage App, App VendorPortal - Saptaswa ::Worked on Making Models, Views and Urls of these app
#Tester/Debugger  - Subham ::Worked on Url testing , Running Unit Test Cases
#Schema and Architecture Development - Esha ::Proper Functing of Application, Integration frontend and Backend 
#Graphics and Html - Samparpita :: Worked on Creating forms and Gathering Graphics 
#Graphics and HTML - Naina :: Worked on Styling on Fronted and Defining UseCases
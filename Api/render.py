from .views import *
from .models import *
from .serializer import *


class HomeApiView(RegisterSerializer, APIView,):
    def post(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password != password2:
                return Response({'Password':'Does not match'})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
            elif User.objects.filter(first_name=first_name).exists():
                messages.info(request, 'First Name already Taken')
            elif User.objects.filter(last_name=last_name).exists():
                messages.info(request, 'Last Name already Taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password2)
                user.save()
                return user

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        email = request.POST['email']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(email=email, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'login.html')
            # messages.info(request, 'User Logged In')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect Email and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')
                
from .serializer import MessageSerializer, MessageModel
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        new_user = MessageModel(email=email, subject=subject, name=name, phone=phone, message=message)
        if MessageModel.objects.filter(email=email).exists():
            messages.info(request, 'User already exists')
        else:
            new_user.save()
    return render(request, 'contact.html')
    # else:
    #     messages.info(request, 'Details already have been there')
           

def about(request):
    return render(request, 'about.html')

def homepage(request):
    return render(request,'homepage.html')

def home(request):
    all_user=UploadImages.objects.all()
    data = {'all_user':all_user,}
    print(data)
    print(all_user)
    return render(request, 'index.html', data)

def services(request):
    return render(request, 'services.html')

#Delete the User Account from HTML template
class delete_user(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'delete_user_confirm.html'
    success_message = 'User has been deleted successfully'
    success_url = reverse_lazy('index.html')


class user_delete(APIView):
    model = User
    def delete(self, request, id):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            model(email=email, password=password)
            if model.objects.filter(email=email).exists():
                model.delete()
                return render (request, 'index.html')
            else:
                messages.info(request, 'User is not been found')
        else:
            return reverse_lazy('homepage.html')


# def UserDeleteInformation(request, pk):
#     if request.method == 'DELETE':

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        new_user = authenticate(email=email, password=password)
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        new_user = User(email=email, first_name=firstname, last_name=lastname)
        if password != confirm_password and User.objects.filter(email=email).exists:
            return render(request, 'signup.html')
        else:
            new_user.save()
    return render(request, 'signup.html')

def about(request):
    return reverse_lazy (request, 'about.html')

def services(request):
    return reverse_lazy (request, 'services.html')
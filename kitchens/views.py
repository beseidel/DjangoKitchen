



#queryset based
#
# from django.shortcuts import render
# from .models import Post
#
#
# def index(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'index.html', context)
#
#
# def about(request):
#     return render(request, 'about.html', {'title': 'About'})
#

#
# *****************************************************

from django.shortcuts import render
from .models import Kitchen

# Create your views here.

from django.http import HttpResponse

# function based
# def index(request):
#     return HttpResponse ('<h1>kitchens home<h1>')
#
# def about(request):
#     return HttpResponse ('<h1>kitchens about<h1>')


# ******************************************
#
# posts = [
#      {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 1',
#       'content': 'first post content',
#       'date_posted': 'August 27, 2019',
#
#       },
#
#       {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 2',
#       'content': 'Second post content',
#       'date_posted': 'August 28, 2019',
#
#       }
#  ]
# # # template based
# def home(request):
#      context = {
#           'posts': posts
#        }
#
#      return render (request, 'home.html', context)
#
# def index(request):
#      context = {
#           'posts': posts
#       }
#
#      return render (request, 'index.html', context)
#
# def about(request):
#      return render (request, 'about.html', {'title': 'About' } )
#
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('kitchens-home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})
#
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('kitchens-home'))
#         form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('kitchens-home'))
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)
#
#
# #
# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('kitchens-home'))
#
#
# @app.route("/account")
# @login_required
# def account():
#     return render_template('account.html', title='Account')

#
# ************
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Use this for builtin class based views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Kitchen

# Function based views below
def home(request):
    context = {
        'kitchens': Kitchen.objects.all()
    }
    return render(request, 'kitchens/home.html', context)


# class based views and inherit from ListView  looks for a templatename <app?/<modle?.html  so we need to set template name for class views
class KitchenListView(ListView):
    model = Kitchen

    # need to set template = to be home.html in order to work
    template_name = 'kitchens/home.html'  # could name template this but we can convert here  <app>/<model>_<viewtype>.html

    # need to set the object = to posts here which the template is looping over
    # or change the template looping variable posts to object
    context_object_name = 'kitchens'

    # need to reorder the posts which can be done by setting the variable ordering to -dateposted
    ordering = ['-date_posted']


class UserKitchenListView(ListView):
    model = Kitchen
    template_name = 'kitchen/user_kitchens.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'kitchens'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Kitchen.objects.filter(author=user).order_by('-date_posted')



# This is a typical class view using
class KitchenDetailView(DetailView):
    model = Kitchen


class KitchenCreateView(LoginRequiredMixin, CreateView):
    model = Kitchen
    fields = ['title', 'content']

# Need to override the form
    def form_valid(self, form):
        # run the form method to the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class KitchenUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Kitchen
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        kitchen = self.get_object()
        if self.request.user == kitchen.author:
            return True
        return False


class KitchenDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Kitchen
    success_url = '/'

    # Function to make sure author is the registered user to do the deleting
    def test_func(self):
        post = self.get_object()
        if self.request.user == kitchen.author:
            return True
        return False

def about(request):
    return render(request, 'kitchens/about.html', {'title': 'About'})



# queryset based
#
# from django.shortcuts import render
# from .models import Kitchen
#
#
# def index(request):
#     context = {
#         'kitchens': Post.objects.all()
#     }
#     return render(request, 'index.html', context)
#
#
# def about(request):
#     return render(request, 'about.html', {'title': 'About'})
#

#
# *****************************************************

# from django.shortcuts import render
# from .models import Post

# Create your views here.

from django.http import HttpResponse

# function based
# def index(request):
#     return HttpResponse ('<h1>kitchens home<h1>')
#
# def about(request):
#     return HttpResponse ('<h1>kitchens about<h1>')


#
# posts = [
#      {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 1',
#       'content': 'first post content',
#       'date_posted': 'August 27, 2019',
#
#       },
#
#       {
#
#       'author': 'Barbara Seidel',
#       'title': 'Blog Post 2',
#       'content': 'Second post content',
#       'date_posted': 'August 28, 2019',
#
#       }
#  ]
# # # template based
# def home(request):
#      context = {
#           'posts': posts
#        }
#
#      return render (request, 'home.html', context)
#
# def index(request):
#      context = {
#           'posts': posts
#       }
#
#      return render (request, 'index.html', context)
#
# def about(request):
#      return render (request, 'about.html', {'title': 'About' } )

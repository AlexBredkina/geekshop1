from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from basketapp.models import Basket


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    # total_quantity =0
    # for basket in Basket.objects.filter(user = request.user):
    #     total_quantity+=1
    # total_sum = 0
    # for basket in Basket.objects.filter(user=request.user):
    #     total_sum+=basket.sum()
    context = {
        'title': 'Профиль', 'form': form,
        'baskets': Basket.objects.filter(user=request.user),
        # 'total_quantity': total_quantity,
        # 'total_sum': total_sum,
        # 'total_quantity': sum(basket.quantity for basket in Basket.objects.filter(user = request.user)),
        # 'total_sum': sum(basket.sum() for basket in Basket.objects.filter(user = request.user)),

    }
    return render(request, 'authapp/profile.html', context)

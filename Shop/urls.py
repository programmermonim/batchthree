from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth import views as auth_views
from Shop import views
urlpatterns = [
    path('', views.ProductView.as_view(), name ="home" ),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchangedone.html'),name='passwordchangedone'),


#start_reset_password

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Shop/password_reset.html',form_class=MyPasswordResetForm), name= 'password-reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Shop/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Shop/password_reset_confirm.html', form_class =MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Shop/password_reset_complete.html'), name='password_reset_complete'),

#end_reset_password

    path('lehenga/', views.lehenga, name='lehenga'),
    path('lehenga/<slug:data>',views.lehenga, name='lehengaitem'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form=LoginForm), name='login'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
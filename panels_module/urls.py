from django.urls import path
from panels_module import views
from panels_module import APIView

urlpatterns = [
    path('recover-password', views.recover_password, name='recover-password-page'),
    path('recover-password-api', APIView.RecoverPassword.as_view(), name='recover-password-api'),
    path('ACP/<code>-api', APIView.ACP.as_view(), name='ACP-api'),
    path('ACP/<code>', views.ACP, name='ACP-page'),
    # -------------------------------------------------------------------------------------------
    path('<slug:panel_slug>', views.panel, name='panel-page'),
    path('<slug:panel_slug>/edit-account', views.edit_account, name='edit-account-page'),
    path('<slug:panel_slug>/delete-account', views.delete_account, name='delete-account-page'),
    path('<slug:panel_slug>/email-verification', views.email_verification, name='email-verification-page'),
    path('<slug:panel_slug>/email-verification/<code>', views.email_verification_code, name='email-verification-code'),

    # api :
    path('<slug:panel_slug>/edit-account-api', APIView.EditAccount.as_view(), name='edit-account-api'),
    path('<slug:panel_slug>/delete-account-api', APIView.DeleteAccount.as_view(), name='delete-account-api'),
    path('<slug:panel_slug>/email-verification-api', APIView.EmailVerification.as_view(), name='email-verification-api'),
    path('<slug:panel_slug>/delete-image-api', APIView.DeleteImage.as_view(), name='delete-image-api'),
    path('<slug:panel_slug>/get-info-api', APIView.GetUserInfo.as_view(), name='get-info-api'),
    path('<slug:panel_slug>/logout-api', APIView.LogOut.as_view(), name='logout-api')
]

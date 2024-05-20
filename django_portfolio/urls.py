from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views as portfolio_views
from portfolio.views import login_view, logout_view, create_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-project/', create_project, name='create_project'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

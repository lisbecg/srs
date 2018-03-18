from django.conf.urls import url
from django.contrib import admin
from srs import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as view_auth

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin$', RedirectView.as_view(url='/admin'), name='admin'),
    url(r'^$', views.welcome_text, name='welcome'),
	url(r'^create_account/', views.create_account, name='create_account'),
	url(r'^login/', view_auth.login, name="login"),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
	url(r'^srs/$', views.selection_view, name='selection_view'),
	url(r'^srs/notefile_list', views.notefile_list, name='notefile_list'),
	url(r'^srs/notefile/(?P<pk>\d+)/$', views.notefile_detail, name='notefile_detail'),
	url(r'^srs/notecard_list/(?P<pk>\d+)/$', views.notecard_list, name='notecard_list'),
	url(r'^srs/import_notecard/(?P<pk>\d+)/$', views.import_notecard, name='import_notecard'),
	url(r'^srs/export_notecard/(?P<pk>\d+)/$', views.export_notecard, name='export_notecard'),
	url(r'^srs/notecard/(?P<pk>\d+)/$', views.notecard_detail, name='notecard_detail'),
	url(r'^srs/create_notefile/(?P<pk>\d+)/$', views.notefile_new, name='create_notefile'),
	url(r'^srs/directory_list/$', views.home_directory, name='home_directory'),
	url(r'^srs/create_directory/(?P<pk>\d+)/$', views.create_directory, name='create_directory'),
	url(r'^srs/directory_list/(?P<pk>\d+)/$', views.directory_content, name='directory_content'),
	url(r'^srs/create_notecard/(?P<pk>\d+)/$', views.create_notecard, name='create_notecard'),
    url(r'^srs/edit_notecard/(?P<pk>\d+)/$', views.edit_notecard, name='edit_notecard'),
    url(r'^srs/delete_notecard/(?P<pk>\d+)/$', views.delete_notecard, name='delete_notecard'),
    url(r'^srs/activate_notecard/(?P<pk>\d+)/$', views.activate_notecard, name='activate_notecard'),
    url(r'^srs/duplicate_notecard/(?P<pk>\d+)/$', views.duplicate_notecard, name='duplicate_notecard'),
	url(r'^srs/create_video/(?P<pk>\d+)/$', views.create_video, name='create_video'),
	url(r'^srs/create_audio/(?P<pk>\d+)/$', views.create_audio, name='create_audio'),
	url(r'^srs/create_document/(?P<pk>\d+)/$', views.create_document, name='create_document'),
	url(r'^srs/create_equation/(?P<pk>\d+)/$', views.create_equation, name='create_equation'),
	url(r'^srs/create_image/(?P<pk>\d+)/$', views.create_image, name='create_image'),
	url(r'^srs/video_archive/$', views.video_list, name='video_list'),
	url(r'^srs/audio_archive/$', views.audio_list, name='audio_list'),
    url(r'^srs/document_archive/$', views.document_list, name='document_list'),
	url(r'^srs/image_archive/$', views.image_list, name='image_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

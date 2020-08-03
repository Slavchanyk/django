from django.contrib import admin
from .models import Orders, Users
from django.http import HttpResponseRedirect
from django.conf.urls import url
# Register your models here.
admin.site.register(Orders)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    change_list_template = "admin/upload_from_csv_button.html"
    def get_urls(self):
        urls = super(UsersAdmin, self).get_urls()
        custom_urls = [
        url('^import/$', self.process_import, name='process_import'),]
        return custom_urls + urls
    def process_import(self, request):
        return HttpResponseRedirect("/upload-csv")
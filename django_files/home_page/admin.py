from django.contrib import admin
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'email', 'timestamp', 'updated']
	list_display_links = ['username']
	list_filter = ['username', 'timestamp', 'updated']
	search_fields = ['username', 'email']

	class Meta:
		model = SignUp


admin.site.register(SignUp, SignUpAdmin)	

# Register your models here.

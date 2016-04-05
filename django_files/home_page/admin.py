from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UserProfile
from .forms import UserChangeForm, UserCreationForm


# class UserProfileInline(admin.StackedInline):
# 	model = UserProfile
# 	can_delete = False


# class UserProfileAdmin(UserAdmin):
# 	inlines = [UserProfileInline, ]

# 	def stars(self, obj):
# 		# if UserProfile.objects.filter(user__id = request.id):
# 		# 	return UserProfile.objects.get(user__id = request.id).stars
# 		# else:
# 		# 	return None
# 		try:
# 			return obj.profile.stars
# 		except UserProfile.DoesNotExist:
# 			return ''

# 	list_display = UserAdmin.list_display +  ('stars', )

# admin.site.register(User, UserProfileAdmin)	



# class UserProfileAdmin(admin.ModelAdmin):
# 	class Meta:
# 		can_delete = False
# 	list_display = ('username', 'email', 'user_mobile', 'stars')

# admin.site.register(UserProfile, UserProfileAdmin)

# Register your models here.

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'stars', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('stars',)}),
    )


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = BaseUserAdmin.list_display+ ('user_mobile', 'stars')
#     fieldsets = BaseUserAdmin.fieldsets
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = BaseUserAdmin.add_fieldsets
#     search_fields = BaseUserAdmin.search_fields + ('user_mobile',)
#     ordering = ('id',)
#     filter_horizontal = ()

# # Now register the new UserAdmin...
admin.site.register(UserProfile, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
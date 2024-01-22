from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrStaff(BasePermission):
    def has_permission(self, request, view):
       return bool (request.method in SAFE_METHODS and 
        request.user and 
        request.user.is_superuser)
    

class IsAuthenticated(BasePermission):
   def has_permission(self, request, view):
      if request.method in SAFE_METHODS:
         return True
      return bool(request.user.is_authenticated or request.user.is_superuser)
    

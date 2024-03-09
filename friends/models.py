from reguser.models import CustomUser
from djongo import models

# Create your models here.

class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user', on_delete=models.CASCADE)
    created_date1 = models.DateTimeField(auto_now_add=True)


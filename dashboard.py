from .models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_update(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "accounts/profile_update.html", {"form": form})

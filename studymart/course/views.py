from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentRegistration


# Create your views here.
def free_course(request):
    course1 = "free course"
    course2 = "paid course"
    course3 = "free course"
    course4 = "paid course"
    course_details = {
        "c1": course1,
        "c2": course2,
        "c3": course3,
        "c4": course4,
    }
    return render(request, "resources/free_course.html", course_details)

def student_info(request):
    sdetails=Student.objects.all()
    return render(request, "courses/student_info.html", {"student_details": sdetails})



def show_form(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)

        if form.is_valid():
            print("=" * 50)
            print("✓ Form is valid")
            print("=" * 50)

            for field, value in form.cleaned_data.items():
                print(f"{field}: {value}")

            print("=" * 50)

            form.save()
            return redirect("success")

        print("✗ Form errors:", form.errors)

    else:
        form = StudentRegistration(
            auto_id=True,
            label_suffix=" = ",
            initial={"email": "rif@gmail.com"},
        )
        form.order_fields(
            ["first_name", "last_name", "email", "password", "batch", "textarea", "payment", "django"]
        )

    return render(request, "courses/forms.html", {"form": form})
    


def show_success(request):
    return render(request, "courses/success.html")



 
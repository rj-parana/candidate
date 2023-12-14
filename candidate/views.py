from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import PersonalDetails, EducationDetails
from .forms import PersonalDetailsForm, EducationDetailsForm


def create(request):
    email = None
    personal = None
    lenth = None

    if request.method == 'POST':
        email = request.POST.get('email')
        lenth = request.POST['totallength']

        if PersonalDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist')
            return redirect('candidate:candidate-create')

        personal = PersonalDetails.objects.create(
            honorific=request.POST.get('honorific'),
            f_name=request.POST.get('f_name'),
            l_name=request.POST.get('l_name'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob'),
            email=request.POST.get('email'),
            country_code=request.POST.get('country_code'),
            mobile=request.POST.get('mobile'),
            country=request.POST.get('country'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            pin_code=request.POST.get('pin_code'),
            skills=request.POST.get('skills'),
            hobbies=request.POST.get('hobbies'),
            interests=request.POST.get('interests'),
            image=request.POST.get('image')
            )

        if personal is None:
            messages.error(request, 'Personal Detail is required')
            return render(request, 'index.html')

        elif personal and lenth:
            if request.POST:
                i = 0
                for index in range(i, int(lenth)):
                    level = ""
                    school_name = ""
                    course = ""
                    year_of_passing = ""
                    complited = ""
                    is_detail = 0
                    if 'level'+str(index) in request.POST:
                        level = request.POST['level'+str(index)]
                        is_detail = 1
                    if 'school_name'+str(index) in request.POST:
                        school_name = request.POST['school_name'+str(index)]
                        is_detail = 1
                    if 'course'+str(index) in request.POST:
                        course = request.POST['course'+str(index)]
                        is_detail = 1
                    if 'year_of_passing'+str(index) in request.POST:
                        year_of_passing = request.POST['year_of_passing'+str(index)]
                        is_detail = 1
                    if 'complited'+str(index) in request.POST:
                        complited = request.POST['complited'+str(index)]
                        is_detail = 1

                    if is_detail == 1:

                        EducationDetails.objects.create(
                            personal_detail = personal,
                            level = level,
                            school_name = school_name,
                            course = course,
                            year_of_passing = year_of_passing,
                            complited = complited
                            )

            messages.success(request, 'Both Form Submitted Successfully')
            return redirect('candidate:candidate-update', pk=personal.id)

        else:
            messages.success(request, 'Form Submitted Successfully')
            return redirect('candidate:candidate-update', pk=personal.id)

    else:
        messages.error(request, 'Something went wrong')
        return render(request, 'index.html')


def update(request, pk):
    educations = None
    totallength = 0
    context = {}
    sub_context ={}
    honorific = ""
    f_name = ""
    l_name = ""
    gender = ""
    dob = ""
    email = ""
    country_code = ""
    mobile = ""
    country = ""
    state = ""
    city = ""
    address = ""
    pin_code = ""
    skills = ""
    hobbies = ""
    interests = ""
    image = ""
    level = ""
    school_name = ""
    course = ""
    year_of_passing = ""
    complited = ""

    personal = get_object_or_404(PersonalDetails, id=pk)
    educations = EducationDetails.objects.filter(personal_detail=personal).all()
    educations = list(educations.values())
    totallength = int(len(educations))
    
    if request.method == 'POST':
        print('pooooooooooooooooooooooooooooooooost')

        # for (key, value) in personal_detail.items():
        #     if hasattr(PersonalDetails, key):
        #         setattr(personal_detail, key, value)
    
        # if form.is_valid():
        #     if 'email' in request.data:
        #         messages.error(request, 'Email can\'t be change')
        #         return redirect('update')
        #     else:
        # personal_detail.save()
        # messages.success(request, 'Details Updated Successfully')
        # return redirect('update', pk=personal_detail.id)
    # else:
        # form = PersonalDetailsForm(instance=personal_detail)
        
        return redirect('candidate:candidate-update', pk=personal.id)
    else:
        if personal.honorific:
            honorific = personal.honorific
        if personal.f_name:
            f_name = personal.f_name
        if personal.l_name:
            l_name = personal.l_name
        if personal.gender:
            gender = personal.gender
        if personal.dob:
            dob = personal.dob
        if personal.email:
            email = personal.email
        if personal.country_code:
            country_code = personal.country_code
        if personal.mobile:
            mobile = personal.mobile
        if personal.country:
            country = personal.country
        if personal.state:
            state = personal.state
        if personal.city:
            city = personal.city
        if personal.address:
            address = personal.address
        if personal.pin_code:
            pin_code = personal.pin_code
        if personal.skills:
            skills = personal.skills
        if personal.hobbies:
            hobbies = personal.hobbies
        if personal.interests:
            interests = personal.interests
        if personal.image:
            image = personal.image

        context = {'honorific':honorific, 'f_name':f_name, 'l_name':l_name, 'gender':gender, 'dob':dob, 'email':email, 'country_code':country_code, 'mobile':mobile, 'country':country, 'state':state, 'city':city, 'address':address, 'pin_code':pin_code, 'skills':skills, 'hobbies':hobbies, 'interests':interests, 'image':image, 'totallength':str(totallength), 'educations':educations}
        # if educations is not None:
        #     i = 0
        #     for index in range(i, totallength):
        #         for key, value in educations[index].items():
        #             is_detail = 0
        #             if key == 'level':
        #                 level = value
        #                 is_detail = 1
        #             if key == 'school_name':
        #                 school_name = value
        #                 is_detail = 1
        #             if key == 'course':
        #                 course = value
        #                 is_detail = 1
        #             if key == 'year_of_passing':
        #                 year_of_passing = value
        #                 is_detail = 1
        #             if key == 'complited':
        #                 complited = value
        #                 is_detail = 1

        #             if is_detail == 1:
        #                 context[key+str(index)] = value
                # sub_context = {'level'+str(index):level, 'school_name'+str(index):school_name, 'course'+str(index):course, 'year_of_passing'+str(index):year_of_passing, 'complited'+str(index):complited}


        print(context,'7777777777777777777777777777777777777777')
    return render(request, 'index.html', context)
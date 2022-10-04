from django.shortcuts import render
from .models import *
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
def home(request):
    context = {'amenities': Amenities.objects.all}
    return render(request,'home.html',context)

def get_hotel(request):
    try:
        hotel_objects = Hotel.objects.all()
        
        # get value by sorting of hotel price by asc or desc value
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                hotel_objects = hotel_objects.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                hotel_objects = hotel_objects.order_by('-hotel_price')

        # get value by sorting of hotel price by entering value/price
        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            hotel_objects = hotel_objects.filter(hotel_price__lte = amount)

        # get values of amenities
        if request.GET.get('amenities'):
            amenities = request.GET.get('amenities')
            amenities=str(amenities).split(',')
            amen = []
            for amenity in amenities:
                amen.append(int(amenity))
                print(amen)
            hotel_objects = hotel_objects.filter(amenities__in = amen).distinct()

        # get all values from hotel
        payload = []
        for hotel_obj in hotel_objects:
            payload.append({
                
                    'hotel_name': hotel_obj.hotel_name,
                    'hotel_price': hotel_obj.hotel_price,
                    'hotel_description': hotel_obj.hotel_description,
                    'banner_image': '/media/' + str(hotel_obj.banner_image ),
                    'amenities':hotel_obj.get_amenities()
                
            })
        return JsonResponse(payload,safe=False)

    except Exception as e:
        print(e)

    return JsonResponse({'message':'Something went wrong '})
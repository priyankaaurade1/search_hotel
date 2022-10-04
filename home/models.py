from django.db import models

# Create your models here.
class Amenities(models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    upload_at = models.DateField(auto_now=True)

    

    def __str__(self) -> str:
        return self.amenity

    # or 
    # class Meta:
    #     model = Amenities
    #     fields = ('amenity')


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    banner_image = models.ImageField(upload_to="hotels")
    created_at = models.DateField(auto_now_add=True)
    upload_at = models.DateField(auto_now=True)

    def get_amenities(self):
        payload = []

        for amenity in self.amenities.all():
            payload.append({'id':amenity.id,
                            'amenity':amenity.amenity})
        return payload

    def __str__(self) -> str:
        return self.hotel_name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    upload_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.hotel
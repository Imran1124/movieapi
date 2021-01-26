from django.db import models

class CountryModel(models.Model):
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    country_status = models.CharField(max_length=255, default='Active')
    class Meta:
        db_table = 'tbl_country'
    
    def __str__(self):
        return self.country_name

class StateModel(models.Model):
    state_name = models.CharField(max_length=200)
    state_code = models.CharField(max_length=200)
    state_status = models.CharField(max_length=200, default='Active')
    country_id = models.ForeignKey('CountryModel', on_delete=models.CASCADE, default=True, blank=True,)
    class Meta:
        db_table = 'tbl_state'

    def __str__(self):
        return self.state_name

class CityModel(models.Model):
    city_name = models.CharField(max_length=200)
    city_code = models.CharField(max_length=200)
    city_status = models.CharField(max_length=200, default='Active')
    state_id = models.ForeignKey('StateModel', on_delete=models.CASCADE, null=True, blank=True,)
    class Meta:
        db_table = 'tbl_city'

    def __str__(self):
        return self.city_name

class SingupModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    country = models.ForeignKey('CountryModel', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey('StateModel', on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey('CityModel', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'tbl_singup'

    def __str__(self):
        return self.name
    



class MovieModel(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    desc=models.TextField()
    imdb=models.CharField(max_length=200)
    image=models.ImageField(upload_to='imagefolder', null=True)
    video=models.FileField(upload_to='videofolder' ,null=True)



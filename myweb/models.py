from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

#################################################################################################################

#class Zone(models.Model): #ภาค
#    zone_text = models.CharField(max_length=200) #ประเภทของภาค
#    def __str__(self):
#        return f'{self.zone_text}'

class Place(models.Model):
    #zone_p = models.ForeignKey(Zone, on_delete=models.CASCADE) #ภาค
    province = models.CharField(max_length=200)  #จังหวัด
    name_p = models.CharField(max_length=400)  #ชื่อ
    rate = models.IntegerField(default=0, max_length=10) #ระดับ
    #def __str__(self):
    #    return f'{self.zone_p.zone_text} - {self.province} - {self.name} - {self.rate} rate.'
    def __str__(self):
         return f'{self.province} - {self.name} - {self.rate}'

#################################################################################################################

#class People(models.Model): #ประเภคบุคค
#    people_text = models.CharField(max_length=200) # นักท่องเที่ยว บุคคทั่วไป
#    def __str__(self):
#        return f'{self.people_text}'

class Person(models.Model):
    #type_n = models.ForeignKey(People, on_delete=models.CASCADE) #ประเภคบุคคล
    type_n = models.CharField(max_length=200)
    name = models.CharField(max_length=200)  #ชื่อ
    career = models.CharField(max_length=200)  #อาชีพ
    age = models.IntegerField(default=0, max_length=100) #อายุ
    def __str__(self):
        #return f'{self.type_n.people_text} - {self.name} - {self.career} - {self.age} age.'
        return f'{self.type_n} - {self.name} - {self.career} - {self.age}'

#################################################################################################################

class importplace(models.Model):
    urlimg = models.CharField(max_length=200) #url รูป
    nameimg = models.CharField(max_length=200)  #ชื่อ
    detail = models.CharField(max_length=20000)  #เนื้อหา
    rating = models.IntegerField(default=0, max_length=10) #ระดับ
    def __str__(self):
        #return f'{self.type_n.people_text} - {self.name} - {self.career} - {self.age} age.'
        return f'{self.urlimg} - {self.nameimg} - {self.detail} - {self.rating}'

#################################################################################################################







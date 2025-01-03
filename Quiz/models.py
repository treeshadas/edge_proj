from django.db import models
import uuid
# Create your models here.baseModel
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4)
    create_at=models.DateField(auto_now_add=True)
    updates_at=models.DateField(auto_now=True)    
    class Meta:
        abstract=True

class Category(BaseModel):
    category_name=models.CharField(max_length=100)
class Question(BaseModel):
    Category=models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    masks=models.IntegerField(default=5)
class Answer(BaseModel):
    question=models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)  
    answer=models.CharField(max_length=100) 
    is_correct=models.BooleanField(default=False) 
    
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
  
    def __str__(self):
        return self.question
        
from django.db import models

# Create your models here.
# Database of questions
class Question(models.Model):
    """This class makes a database called question:
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        """This method returns the text of the question:
        """
        return self.question_text

 # Database of choices   
class Choice(models.Model):
    """This class makes a database called choice:
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        """This method returns the text of the choice:
        """
        return self.choice_text


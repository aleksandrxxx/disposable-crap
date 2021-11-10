from django.db.models import (
    Model, CharField, TextField, DateField, IntegerField, ManyToManyField, ForeignKey, CASCADE
)

class Poll(Model):
    '''
    Poll has title, description and contains questions.
    Start/end dates define duration of the poll.
    Once a poll is created, its start_date cannot be changed.
    '''
    title = CharField(max_length=255)
    description = TextField()
    start_date = DateField(auto_now_add=True)  # XXX this logic was requested but it's probably wrong:
                                               # creation of record does not mean start of poll,
                                               # simply because questions aren't created yet
    end_date = DateField()  # XXX validate, must be > start_date
    questions = ManyToManyField('Question', blank=True)

    def __str__(self):
        return self.title

class Choice(Model):
    '''
    Choice for poll questions.
    '''
    text = CharField(max_length=255)

    def __str__(self):
        return self.text

class Question(Model):
    '''
    Poll question.
    There are three types of questions:
     * plain text answer
     * single choice
     * multiple choices
    '''
    text = CharField(max_length=255)
    question_type = IntegerField(choices=[
        (1, 'Plain Text'),
        (2, 'Single Choice'),
        (3, 'Multiple Choices')
    ])
    choices = ManyToManyField(Choice, blank=True)  # XXX needs custom validation depending on type

    def __str__(self):
        return self.text

class Answer(Model):
    '''
    Answer to a question.
    XXX anonymous answers have user_id set to NULL???
    '''
    question = ForeignKey(Question, on_delete=CASCADE)
    user_id = IntegerField(null=True)  # XXX not referring to User model for now, assume users know their IDs
    text = CharField(max_length=255)
    choices = ManyToManyField(Choice, blank=True)

    def __str__(self):
        return self.text

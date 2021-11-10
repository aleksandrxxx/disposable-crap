'''
Create sample polls for demo purposes.
'''

from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polls.settings')

import django
django.setup()

from django.utils import timezone

from polls.api.models import Poll, Question, Choice

q1 = Question(text="How is Django?", question_type=2)  # XXX here we need a constant
q1.save()
c1 = Choice(text="Oh, it's a fantastic thing!")
c1.save()
c2 = Choice(text="It's so so...")
c2.save()
c3 = Choice(text="It's a total crap!")
c3.save()
q1.choices.add(c1, c2, c3)

q2 = Question(text="Would you use Django for new projects?", question_type=2)
q2.save()
c1 = Choice(text="Surely, I would!")
c1.save()
c2 = Choice(text="It depends...")
c2.save()
c3 = Choice(text="Only by a court order!")
c3.save()
q2.choices.add(c1, c2, c3)

q3 = Question(text="How could we make Django even better?", question_type=2)
q3.save()
c1 = Choice(text="We could donate!")
c1.save()
c2 = Choice(text="Sit and fix its quirks.")
c2.save()
c3 = Choice(text="Nothing can make it better. They have screwed everything up!")
c3.save()
q3.choices.add(c1, c2, c3)


poll = Poll(title='Django questionnaire', description='A few questions about Django web framework',
            start_date=timezone.now(), end_date=timezone.now() + timedelta(days=1))
poll.save()
poll.questions.add(q1, q2, q3)

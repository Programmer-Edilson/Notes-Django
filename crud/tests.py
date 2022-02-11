from django.test import TestCase, Client
from crud.models import Note
from django.contrib.auth.models import User

# Create your tests here.

class CrudModelTestCase(TestCase):
    """ Testing crud's Model """

    def setUp(self):
        user1 = User.objects.create(username="userone", password="userone")
        note1 = Note.objects.create(title="noteone", description="mynoteone", status=-1, user=user1)
        note2 = Note.objects.create(title="notetwo", description="mynotetwo", status=-1, user=user1)

        user2 = User.objects.create(username="usertwo", password="usertwo")
        note3 = Note.objects.create(title="notethree", description="mynotethree", status=0, user=user2)
        note4 = Note.objects.create(title="notefour", description="mynotefour", status=1, user=user2)
    
    def testNoteUser(self):
        """ Check if a note belongs a certain user """
        
        user = User.objects.get(username="usertwo")
        note = Note.objects.get(title="notefour")
        note_user = note.user
        self.assertEqual(note_user, user)


    
    def testUserNotesCount(self):
        """ Test how many notes a user has """

        user = User.objects.get(username="userone")
        notes = Note.objects.filter(user=user).count()
        self.assertEqual(notes, 2)

    def testNoteTitle(self):
        """ Test note's title """

        note = Note.objects.get(status=1)
        title = str(note.title)
        self.assertEqual(title, "notefour")

    def testNoteDescription(self):
        """ Test note's description """

        note = Note.objects.get(title="noteone")
        description = str(note.description)
        self.assertEqual(description, "mynoteone")

    def testNoteStatus(self):
        """ Test note's status """

        note = Note.objects.get(description="mynotethree")
        status = int(note.status)
        self.assertEqual(status, 0)

import unittest
from app.models import Pitch,User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.user_kets = User(username = 'ketsia',email = 'iraketsia@yahoo.com',secure_password = 'unity',bio= 'The greatest minds are capable of the greatest vices as well as of the greatest virtues. ', profile_pic_path='https://cdn.britannica.com/s:250x250,c:crop/62/176962-050-4BC9F588/Rene-Descartes.jpg')
        self.new_pitch = Pitch(id=12,title='Psychic',pitch="philosophy is all about perspective",category='hobbies',user_id= self.user_kets.id, time="2010/2/3 13:20" )

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,12
        self.assertEquals(self.new_pitch.title,'Psychic')
        self.assertEquals(self.new_pitch.pitch,"philosophy")
        self.assertEquals(self.new_pitch.category,'hobbies')
        self.assertEquals(self.new_pitch.user_id,self.user_kets.id)
        self.assertEquals(self.new_pitch.time,'2010/2/3 13:20')

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()    
from django.test import TestCase

from cv.models import basicinfo,skills,interest,eduexperience,certificate,selfcomment


class basicinfoModelTest(TestCase):
    def setUp(self):
        basicinfo.objects.create(college="schooljust type typejust type typejust type typejust type typejust type typejust type typejust type typejust type type",age=223,email="12345687@qq.com")

    def test_success(self):
        college = basicinfo.objects.get(id=1)
        #self.assertEqual(college.getcollege(),'schoo')
        self.assertTrue(len(college.getcollege()) < 100)
        #self.assertEqual(college.getage(),23)
        self.assertTrue(college.getage() < 100 )
        self.assertTrue(college.getage() > 0 )
        self.assertTrue(college.getemail().find("@"))



class skillsModelTest(TestCase):
    def setUp(self):
        skills.objects.create(skills="just type type")

    def test_skills(self):
        skill = skills.objects.get(id=1)
        self.assertTrue(len(skill.getskills()) < 100)

class interestModelTest(TestCase):
    def setUp(self):
        interest.objects.create(interest="just type type")

    def test_skills(self):
        inte = interest.objects.get(id=1)
        self.assertTrue(len(inte.getinterest()) < 100)


class eduexperienceModelTest(TestCase):
    def setUp(self):
        eduexperience.objects.create(school="school",start="201321553138")

    def test_edu(self):
        edu = eduexperience.objects.get(id=1)
        self.assertTrue(len(edu.getschool()) < 100 )
        self.assertTrue(len(edu.getstart()) < 11 )

class certificateModelTest(TestCase):
    def setUp(self):
        certificate.objects.create(time="2013843848646552313184653135468523121",name="just type type")

    def test_cer(self):
        cer = certificate.objects.get(id=1)
        self.assertTrue(len(cer.gettime()) < 20 )
        self.assertTrue(len(cer.getname()) < 100)


class selfcommentModelTest(TestCase):
    def setUp(self):
        selfcomment.objects.create(comment="just type type")

    def test_comment(self):
        comment = selfcomment.objects.get(id=1)
        self.assertTrue(len(comment.getcomment()) < 200 )
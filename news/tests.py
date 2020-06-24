from django.test import TestCase
from .models import Editor,Article,tag
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.brian= Editor(first_name = 'brian', last_name ='Kiiru', email ='kiirubrian21@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.brian,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.brian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.brian= Editor(first_name = 'brian', last_name ='kiiru', email ='kiirubrian21@gmail.com')
        self.brian.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tag(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.brian)
        self.new_article.save()

        self.new_article.tag.add(self.new_tag)

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

  

    def test_get_news_by_date(self):
        test_date = '2020-06-24'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) > 0)

    def tearDown(self):
        Editor.objects.all().delete()
        tag.objects.all().delete()
        Article.objects.all().delete()
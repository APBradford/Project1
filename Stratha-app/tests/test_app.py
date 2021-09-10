from flask import url_for
from flask_testing import TestCase, LiveServerTestCase
from application import app, db
from application.models import Training_week, Cycling
from application.forms import addCycleForm, editCycleForm
from datetime import datetime
from selenium import webdriver
from os import getenv

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY= getenv('DB_SECRET'),
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()
        testTime = datetime(2012, 3, 3, 10, 10, 10)
        testCycle = Cycling(training_week=1, date=testTime, distance=45.5, trSession="Easy", comment="Went well")
        testTraining = Training_week(training_week_id=1, cycle_distance=45.5)
        testTraining2 = Training_week(training_week_id=2, cycle_distance=45.5)
        db.session.add(testCycle)
        db.session.add(testTraining)
        db.session.add(testTraining2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestPages(TestBase):
    def test_homepage(self):
        response = self.client.get(url_for('homepage'))
        self.assertEqual(response.status_code, 200)
        #Tests homepageHTML
        self.assertIn(b'Welcome to Sratha', response.data)
        #Tests Read functionality of the Training_week table
        self.assertIn(b'45.5', response.data)
    
    def test_cyclingpage(self):
        response = self.client.get(url_for('cyclepage'))
        self.assertEqual(response.status_code, 200)
        #Tests cyclepageHTML
        self.assertIn(b'Enter a cycle', response.data)
        #Tests Read functionality of the cycling table
        self.assertIn(b'Easy', response.data)
    
    def test_editCylingPage(self):
        response = self.client.get(url_for('editCycle', id=1))
        self.assertEqual(response.status_code, 200)
        #Tests editCycleHTML
        self.assertIn(b'Editing cycle', response.data)
    
    def test_deleteCylePage(self):
        response = self.client.get(url_for('deleteCycle', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_addCycle(self):
        testTime = datetime(2014, 3, 3, 10, 10, 10)
        form = addCycleForm()
        form.trWeek.data = 2
        form.date.data = testTime
        form.distance.data = 51
        form.trSession.data = "Tempo"
        form.comment.data = "Added Cycle"
        response = self.client.post(
            url_for('cyclepage'),
            data = form.data,
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('cyclepage'))
        self.assertIn(b'Added Cycle', response.data)
    
    def test_editCycle(self):
        testTime = datetime(2014, 3, 3, 10, 10, 10)
        form = editCycleForm()
        form.trWeek.data = 2
        form.date.data = testTime
        form.distance.data = 51
        form.trSession.data = "Tempo"
        form.comment.data = "Edited Cycle"
        response = self.client.post(
            url_for('editCycle', id=1),
            data = form.data,
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('cyclepage'))
        self.assertIn(b'Edited Cycle', response.data)

class IntTestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE2_URI')
        app.config['SECRET_KEY'] = getenv('DB_SECRET')
        return app

    def setUp(self):
        #driver = webdriver.Chrome(executable_path='/usr/bin/')
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)
        db.create_all()
        self.driver.get(f'http://localhost:5000/')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

class TestCycling(IntTestBase):
    def testFormValidation(self):
        self.driver.get(f'http://localhost:5000/Cycling')
        
        #Test whether a blank input for date returns the correct error message
        date_input = self.driver.find_element_by_xpath('//*[@id="date"]')
        date_input.send_keys(' ')

        distance_input = self.driver.find_element_by_xpath('//*[@id="distance"]')
        distance_input.send_keys('40')

        comment_input = self.driver.find_element_by_xpath('//*[@id="comment"]')
        comment_input.send_keys("Input Testing")

        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        errorText = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/span[1]').text
        self.assertIn("Date: This field is required", errorText)
        
        

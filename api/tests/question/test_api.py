from api.models import Question, Category
from rest_framework.test import APITestCase


def get_category():
    return Category.objects.create(name="Testing Category")


def get_category_url(category_id=None):
    if category_id:
        return "/api/categories/{category_id}/"
    else:
        category = get_category()
        return "/api/categories/" + str(category.id) + "/"


class TestQuestionList(APITestCase):

    def test_returns_empty(self):
        response = self.client.get('/api/questions/')
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual('[]', response.data)

    def test_returns_instance(self):
        Question.objects.create(name="first question", category_id=get_category().id)
        response = self.client.get('/api/questions/')
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual(
            '[{' +
            '"url":"http://testserver/api/questions/1/","pk":1,"name":"first question",' +
            '"answer":"","sequence":1,"rows":1,"category":"http://testserver/api/categories/1/"' +
            '}]', response.data)

    def test_returns_many_instances(self):
        category_id = get_category().id
        Question.objects.create(name="first question", category_id=category_id)
        Question.objects.create(name="second question", category_id=category_id)
        response = self.client.get('/api/questions/')
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual(
            '[{' +
            '"url":"http://testserver/api/questions/1/","pk":1,"name":"first question",' +
            '"answer":"","sequence":1,"rows":1,"category":"http://testserver/api/categories/1/"' +
            '},{' +
            '"url":"http://testserver/api/questions/2/","pk":2,"name":"second question",' +
            '"answer":"","sequence":1,"rows":1,"category":"http://testserver/api/categories/1/"' +
            '}]', response.data)


class TestQuestionCreate(APITestCase):

    def createRequest(self):
        return self.client.post('/api/questions/', {
            "name": "question text",
            "category": get_category_url(),
            "answer": "question answer"
        })

    def test_returns_created_instance(self):
        response = self.createRequest()
        self.assertEquals(201, response.status_code)
        self.assertJSONEqual(
            '{' +
            '"url":"http://testserver/api/questions/1/",' +
            '"pk":1,' +
            '"name":"question text",' +
            '"answer":"question answer",' +
            '"sequence":1,' +
            '"rows":1,' +
            '"category":"http://testserver/api/categories/1/"' +
            '}', response.data)

    def test_returns_validation_rules(self):
        response = self.client.post('/api/questions/')
        self.assertEquals(400, response.status_code)
        self.assertJSONEqual(
            '{' +
            '"name":["This field is required."],"answer":["This field is required."],' +
            '"category":["This field is required."]' +
            '}', response.data)

    def test_creates_new_instance(self):
        self.assertEqual(0, Question.objects.count())
        self.createRequest()
        self.assertEqual(1, Question.objects.count())
        self.assertEqual('question text', Question.objects.first().name)


class TestQuestionUpdate(APITestCase):

    def test_returns_updated_instance(self):
        self.skipTest("Not Yet Implemented")

    def test_returns_validation_rules(self):
        self.skipTest("Not Yet Implemented")

    def test_returns_error_when_non_existent(self):
        self.skipTest("Not Yet Implemented")

    def test_updates_instance(self):
        self.skipTest("Not Yet Implemented")


class TestQuestionDelete(APITestCase):

    def test_returns_deleted_status(self):
        self.skipTest("Not Yet Implemented")

    def test_returns_no_content(self):
        self.skipTest("Not Yet Implemented")

    def test_deletes_instance(self):
        self.skipTest("Not Yet Implemented")

    def test_returns_error_when_non_existent(self):
        self.skipTest("Not Yet Implemented")

from api.models import Category
from rest_framework.test import APITestCase


class TestCategoryList (APITestCase):

    def test_returns_empty(self):
        response = self.client.get('/api/categories/')
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual('[]', response.data)

    def test_returns_instance(self):
        Category.objects.create(name="first category")
        response = self.client.get('/api/categories/')
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual(
            '[{' +
            '"url":"http://testserver/api/categories/1/","pk":1,"name":"first category",' +
            '"description":null,"questions":[]' +
            '}]', response.data)

    def test_returns_many_instances(self):
        Category.objects.create(name="first category")
        Category.objects.create(name="second category")
        response = self.client.get('/api/categories/')
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual(
            '[{' +
            '"url":"http://testserver/api/categories/1/","pk":1,"name":"first category",' +
            '"description":null,"questions":[]' +
            '},{' +
            '"url":"http://testserver/api/categories/2/","pk":2,"name":"second category",' +
            '"description":null,"questions":[]' +
            '}]', response.data)


class TestCategoryCreate(APITestCase):

    def test_returns_new_instance(self):
        response = self.client.post('/api/categories/', {"name": "name"})
        self.assertEquals(201, response.status_code)
        self.assertJSONEqual(
            '{' +
            '"url":"http://testserver/api/categories/1/","pk":1,"name":"name","description":null,"questions":[]' +
            '}', response.data)

    def test_returns_validation_rules(self):
        response = self.client.post('/api/categories/')
        self.assertEquals(400, response.status_code)
        self.assertJSONEqual('{"name":["This field is required."]}', response.data)

    def test_creates_new_instance(self):
        response = self.client.post('/api/categories/', {"name": "category name"})
        self.assertEquals(201, response.status_code)
        self.assertEquals(1, Category.objects.all().count())
        self.assertEquals("category name", Category.objects.first().name)


class TestCategoryUpdate (APITestCase):
    def test_returns_updated_instance(self):
        Category.objects.create(name="original name")
        response = self.client.put('/api/categories/1/', {"name": "updated name"})
        self.assertEquals(200, response.status_code)
        self.assertJSONEqual(
            '{' +
            '"url":"http://testserver/api/categories/1/","pk":1,"name":"updated name",' +
            '"description":null,"questions":[]' +
            '}', response.data)

    def test_returns_validation_rules(self):
        Category.objects.create(name="original name")
        response = self.client.put('/api/categories/1/', {"name": ""})
        self.assertEquals(400, response.status_code)
        self.assertJSONEqual('{"name":["This field may not be blank."]}', response.data)

    def test_updates_instance(self):
        Category.objects.create(name="original name")
        self.assertEquals("original name", Category.objects.first().name)
        self.client.put('/api/categories/1/', {'name': "changed name"})
        self.assertEquals("changed name", Category.objects.first().name)

    def test_error_when_non_existent(self):
        response = self.client.put('/api/categories/1/')
        self.assertEquals(404, response.status_code)


class TestCategoryDelete (APITestCase):
    def test_returns_deleted_status(self):
        deletable = Category.objects.create(name="delete")
        response = self.client.delete('/api/categories/' + str(deletable.id) + '/')
        self.assertEquals(204, response.status_code)
        self.assertEquals(None, response.data)

    def test_deletes_instance(self):
        Category.objects.create(name="delete")
        self.assertEquals(1, Category.objects.all().count())
        response = self.client.delete('/api/categories/1/')
        self.assertEquals(204, response.status_code)
        self.assertEquals(0, Category.objects.all().count())

    def test_deletes_singular_instance(self):
        deletable = Category.objects.create(name="delete")
        non_deletable = Category.objects.create(name="stay")
        self.assertEquals(2, Category.objects.all().count())
        response = self.client.delete('/api/categories/' + str(deletable.id) + '/')
        self.assertEquals(204, response.status_code)
        self.assertEquals(1, Category.objects.all().count())
        self.assertEquals(non_deletable.name, Category.objects.first().name)

    def test_error_when_non_existent(self):
        response = self.client.delete('/api/categories/1/')
        self.assertEquals(404, response.status_code)

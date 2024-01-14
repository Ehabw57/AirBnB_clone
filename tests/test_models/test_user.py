#!/usr/bin/python3
"""some doc moents goes  here"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """some docs goes here"""
    def setUp(self):
        """some doc goes here"""
        self.b1 = User()
        self.b2 = User()

    def tearDown(self):
        """some doc goeshere"""
        del self.b1
        del self.b2

    def test_attributes(self):
        """some doki doki here"""
        self.assertTrue(User.email is "")
        self.assertTrue(User.password is "")
        self.assertTrue(User.first_name is "")
        self.assertTrue(User.last_name is "")

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertTrue(
                issubclass(State, BaseModel)
                and State is not BaseModel
                )

    def test_uid(self):
        """some doc here"""
        self.assertTrue(isinstance(self.b1.id, str), "Uid should be a string")
        self.assertFalse(self.b1.id == self.b2.id, "Uid should'nt be the same")

    def test_time(self):
        """seom mother fu docs"""
        self.assertNotEqual(self.b1.created_at, self.b2.created_at,
                            "instance can't have same created time")
        self.assertNotEqual(self.b1.updated_at, self.b2.updated_at,
                            "instances can't have the same updated time")

    def test_str_method(self):
        """some doc string goes here"""
        expected = f"[{self.b1.__class__.__name__}] ({self.b1.id}) {self.b1.__dict__}"
        self.assertEqual(str(self.b1), expected,
                         "The output should be the same")

    def test_save_method(self):
        """some mf doc goes here"""
        self.assertFalse(self.b1.updated_at > self.b2.updated_at,
                         "first instance can't be newer than sex instance")
        self.b1.save()
        self.assertTrue(self.b1.updated_at > self.b2.updated_at,
                        "Save should updated the time")

    def test_dict_method(self):
        """soem doc string goes here"""
        dict = self.b1.to_dict()
        self.assertEqual(dict['__class__'], self.b1.__class__.__name__,
                         "Both items shoud be the values")
        self.assertEqual(dict['created_at'], self.b1.created_at.isoformat(),
                         "Both should be the same value")
        self.assertEqual(dict['updated_at'], self.b1.updated_at.isoformat(),
                         "Both should be the same value")

    def test_init(self):
        """soem docs goes here"""
        json_dict = self.b1.to_dict()
        self.b0 = User(**json_dict)

        for key in json_dict.keys():
            if key not in ['updated_at', 'created_at', '__class__']:
                self.assertEqual(json_dict[key], self.b0.__dict__[key],
                                 f"[{key}] this what we are testing now")

        self.assertEqual(type(self.b0.updated_at), type(self.b1.updated_at),
                         "Updated+created must be instances of datetime class")
        self.assertEqual(type(self.b0.created_at), type(self.b1.created_at),
                         "Updated+created must be instances of datetime class")
        self.assertFalse('__class__' in self.b0.__dict__)


if __name__ == "___main__":
    unittest.main()

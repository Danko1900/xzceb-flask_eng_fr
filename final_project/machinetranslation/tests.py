import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''Tests for english_to_french method.'''
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hi, my name is Dan!'),'Salut, mon nom est Dan !')
        self.assertNotEqual(english_to_french('Goodbye'),'Goodbye')
        self.assertEqual(english_to_french(''),'Text must be provided.')
        self.assertEqual(english_to_french(None),'Text must be provided.')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    '''Tests for french_to_english method.'''
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Salut, mon nom est Dan !'),'Hi, my name is Dan!')
        self.assertNotEqual(french_to_english('Au Revoir'),'Au Revoir')
        self.assertEqual(french_to_english(''),'Text must be provided.')
        self.assertEqual(french_to_english(None),'Text must be provided.')
        self.assertEqual(french_to_english('Bonjour'),'Hello')  

if __name__ == '__main__':
    unittest.main()     

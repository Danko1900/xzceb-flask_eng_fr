import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hi, my name is Dan!'),'Salut, mon nom est Dan !')
        self.assertEqual(english_to_french('I don\'t speak French.'),'Je ne parle pas français.')
        self.assertEqual(english_to_french(''),'Text must be provided.')
        self.assertEqual(english_to_french(None),'Text must be provided.')
        self.assertEqual(english_to_french('Hello'),'Bonjour')


    def test_french_to_english(self):
        self.assertEqual(french_to_english('Salut, mon nom est Dan !'),'Hi, my name is Dan!')
        self.assertEqual(french_to_english('Je ne parle pas français.'),'I don\'t speak French.')
        self.assertEqual(french_to_english(''),'Text must be provided.')
        self.assertEqual(french_to_english(None),'Text must be provided.')
        self.assertEqual(french_to_english('Bonjour'),'Hello')  


if __name__ == '__main__':
    unittest.main()       
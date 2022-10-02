'''Translator Module for Python Project for AI & Application Development - Coursera'''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Takes in english text and returns french translation'''
    try:
        french_text = language_translator.translate(
            english_text,
            model_id='en-fr').get_result()

    except ValueError:
        return "Text must be provided."

    except ApiException:
        return "Text must be provided."

    else:
        return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''Takes in french text and returns english translation'''
    try:
        english_text = language_translator.translate(
            french_text,
            model_id='fr-en').get_result()

    except ValueError:
        return "Text must be provided."

    except ApiException:
        return "Text must be provided."

    else:
        return english_text['translations'][0]['translation']

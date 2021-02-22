from vocabulary_creator import VocabularyCreator
import unittest
from unittest.mock import patch

class TestVocabularyCreator(unittest.TestCase):
    def setUp(self):
            "dataset": [
                {
                    "mail": {
                    "Subject": " term paper",
                    "From": "kaminski@paris.com",
                    "Date": "2001-04-30",
                    "Body":"dr . kaminski \nattached please find a copy of our term paper . advise\nif you experience problems opening the attachment .\nbest regards \nken jett\n- combo 2 [ 1 ] . v 2 . do\n",
                    "Spam": "false",
                    "File": "enronds//enron2/ham/5579.2001-04-30.kaminski.ham.txt"
                    }
                },
                {
                    "mail": {
                    "Subject": " fwd : this is is porn money - -",
                    "From": "GP@paris.com",
                    "Date": "2005-02-02",
                    "Body":"make a $ 1000 a day\nthe adult industry can bring you riches\nbeyond your wildest dreams make a $ 1000 a day with little or no investment .\nwe can show you how ! ! ! ! ! !\nmake a\nfortune become a adult webmaster part or full time\nif you would prefer not to receive these messages\ncheck here your email will be\nremoved within 48 hrs\n",
                    "Spam": "true",
                    "File": "enronds//enron1/spam/3660.2005-02-02.GP.spam.txt"
                    }
                }
            ]
        }  # données pour mocker "return_value" du "load_dict"
        self.clean_subject_spam = ['fwd', 'porn', 'money']  # données pour mocker "return_value" du "clean_text"
        self.clean_body_spam = ['make', 'day', 'adult', 'industri', 'bring', 'rich', 'beyond', 'wildest', 'dream', 'make', 'day', 'littl', 'invest', 'show', 'make', 'fortun', 'becom', 'adult', 'webmast', 'part', 'full', 'time', 'would', 'prefer', 'receiv', 'messag', 'check', 'email', 'remov', 'within', 'hr']  # données pour mocker "return_value" du "clean_text"
        self.clean_subject_ham = ['term', 'paper']  # données pour mocker "return_value" du "clean_text"
        self.clean_body_ham = ['kaminski', 'attach', 'pleas', 'find', 'copi', 'term', 'paper', 'advis', 'experi', 'problem', 'open', 'attach', 'best', 'regard', 'ken', 'jett', 'combo']  # données pour mocker "return_value" du "clean_text"
        self.vocab_expected = {

            "spam_sub":{
                'fwd':1/3,
                'porn':1/3,
                'money':1/3
            },

            "ham_sub":{
                'term':1/2, 
                'paper':1/2
            },

            "spam_body":{
                'make':2/31,
                'day':2/31,
                'adult':2/31,
                'industri':1/31,
                'bring':1/31,
                'rich':1/31,
                'beyond':1/31,
                'wildest':1/31,
                'dream':1/31,
                'littl':1/31,
                'invest':1/31,
                'show':1/31,
                'make':1/31,
                'fortun':1/31,
                'becom':1/31,
                'webmast':1/31,
                'part':1/31,
                'full':1/31,
                'time':1/31,
                'would':1/31,
                'prefer':1/31,
                'receiv':1/31,
                'messag':1/31,
                'check':1/31,
                'email':1/31,
                'remov':1/31,
                'within':1/31,
                'hr':1/31
            },

            "ham_body":{
                'kaminski':1/17, 
                'attach':2/17,
                'pleas':1/17,
                'find':1/17,
                'copi':1/17,
                'term':1/17,
                'paper':1/17,
                'advis':1/17,
                'experi':1/17,
                'problem':1/17,
                'open':1/17,
                'best':1/17,
                'regard':1/17,
                'ken':1/17,
                'jett':1/17,
                'combo':1/17'
            }

        }  # vocabulaire avec les valuers de la probabilité calculées correctement

    def tearDown(self):
        pass

    @patch("vocabulary_creator.VocabularyCreator.load_dict")
    @patch("vocabulary_creator.VocabularyCreator.clean_text")
    @patch("vocabulary_creator.VocabularyCreator.write_data_to_vocab_file")
    def test_create_vocab_spam_Returns_vocabulary_with_correct_values(
        self, mock_write_data_to_vocab_file, mock_clean_text, mock_load_dict
    ):
        """Description: Tester qu'un vocabulaire avec les probabilités calculées
        correctement va être retourné. Il faut mocker les fonctions "load dict"
         (utiliser self.mails comme un return value simulé),"clean text"
         (cette fonction va être appelé quelques fois, pour chaque appel on
         va simuler la return_value different, pour cela il faut utiliser
         side_effect (vois l'exemple dans l'énonce)) et
         "write_data_to_vocab_file" qui va simuler "return True" au lieu
         d'écrire au fichier "vocabulary.json".
         if faut utiliser self.assertEqual(appele_a_create_vocab(), self.vocab_expected)
        """


#if __name__ == "__main__":

  #  unittest.main()

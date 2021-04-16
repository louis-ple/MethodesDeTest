import json

from email_analyzer import EmailAnalyzer

import unittest
from unittest.mock import patch


class TestEmailAnalyzer(unittest.TestCase):
    def setUp(self):

        self.subject_spam = " fwd : this is is porn money - -"
        self.body_spam = "make a $ 1000 a day\nthe adult industry can bring you riches\nbeyond your wildest dreams make a $ 1000 a day with little or no investment .\nwe can show you how ! ! ! ! ! !\nmake a\nfortune become a adult webmaster part or full time\nif you would prefer not to receive these messages\ncheck here your email will be\nremoved within 48 hrs\n"
        self.clean_subject_spam = ['fwd', 'porn', 'money']  # données pour mocker "return_value" du "clean_text"
        self.clean_body_spam = ['make', 'day', 'adult', 'industri', 'bring', 'rich', 'beyond', 'wildest', 'dream', 'make', 'day', 'littl', 'invest', 'show', 'make', 'fortun', 'becom', 'adult', 'webmast', 'part', 'full', 'time', 'would', 'prefer', 'receiv', 'messag', 'check', 'email', 'remov', 'within', 'hr']  # données pour mocker "return_value" du "clean_text"

        self.subject_ham = " term paper"
        self.body_ham = "dr . kaminski \nattached please find a copy of our term paper . advise\nif you experience problems opening the attachment .\nbest regards \nken jett\n- combo 2 [ 1 ] . v 2 . do\n"
        self.clean_subject_ham = ['term', 'paper']  # données pour mocker "return_value" du "clean_text"
        self.clean_body_ham = ['kaminski', 'attach', 'pleas', 'find', 'copi', 'term', 'paper', 'advis', 'experi', 'problem', 'open', 'attach', 'best', 'regard', 'ken', 'jett', 'combo']  # données pour mocker "return_value" du "clean_text"

        self.spam_ham_body_prob_true = (
            0.5,
            0.5,
        )  # données pour mocker "return_value" du "spam_ham_body_prob"
        self.subject_spam_ham_prob_true = (
            0.5,
            0.5,
        )  # données pour mocker "return_value" du "subject_spam_ham_prob"
        self.spam_ham_body_prob_false = (
            0.5,
            0.5,
        )  # données pour mocker "return_value" du "spam_ham_body_prob"
        self.subject_spam_ham_prob_false = (
            0.5,
            0.5,
        )  # données pour mocker "return_value" du "subject_spam_ham_prob"
        self.vocab = (
            {

            "p_sub_spam":{
                'fwd':1/3,
                'porn':1/3,
                'money':1/3
            },

            "p_sub_ham":{
                'term':1/2, 
                'paper':1/2
            },

            "p_body_spam":{
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

            "p_body_ham":{
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
                'combo':1/17
            }

        }
        )  # vocabulaire avec les valeurs de la probabilité pour mocker "return_value" du "load_dict"
        self.spam_ham_body_prob_expected = (5.5538715156327925e-46, 2.9255737483310772e-39)  # valeurs de la probabilité attendus
        self.subject_spam_ham_prob_expected = (2.6990706997084545e-05, 8.294321188683086e-05)  # valeurs de la probabilité attendus

    def tearDown(self):
        pass

    @patch("email_analyzer.EmailAnalyzer.clean_text")
    @patch("email_analyzer.EmailAnalyzer.spam_ham_body_prob")
    @patch("email_analyzer.EmailAnalyzer.spam_ham_subject_prob")
    def test_is_spam_Returns_True_if_spam_prob_is_higher(
        self, mock_subject_spam_ham_prob, mock_spam_ham_body_prob, mock_clean_text
    ):

        mock_subject_spam_ham_prob.return_value=self.subject_spam_ham_prob_true
        mock_spam_ham_body_prob.return_value=self.spam_ham_body_prob_true
        ea=EmailAnalyzer()
        self.assertFalse(ea.is_spam(self.subject_spam, self.body_spam))


        """
        Il faut mocker les fonctions "spam_ham_body_prob" et "subject_spam_ham_prob".
        La sortie de la fonction doit être True si probabilité spam > probabilité ham
        (ces probabilites devron etre calcule selon l'enonce dans le TP1 )
        """

    @patch("email_analyzer.EmailAnalyzer.clean_text")
    @patch("email_analyzer.EmailAnalyzer.spam_ham_body_prob")
    @patch("email_analyzer.EmailAnalyzer.spam_ham_subject_prob")
    def test_is_spam_Returns_False_if_spam_prob_is_lower(
        self, mock_subject_spam_ham_prob, mock_spam_ham_body_prob, mock_clean_text
    ):

        mock_subject_spam_ham_prob.return_value=self.subject_spam_ham_prob_false
        mock_spam_ham_body_prob.return_value=self.spam_ham_body_prob_false
        ea=EmailAnalyzer()
        self.assertFalse(ea.is_spam(self.subject_ham, self.body_ham))



        """
        Il faut mocker les fonctions "spam_ham_body_prob" et "subject_spam_ham_prob".
        La sortie de la fonction doit être False si probabilité spam  probabilité ham
        (ces probabilites devron etre calcule selon l'enonce dans le TP1 )
        """

    @patch("email_analyzer.EmailAnalyzer.load_dict")
    def test_spam_ham_body_prob_Returns_expected_probability(self, mock_load_dict):


        mock_load_dict.return_value=self.vocab
        ea=EmailAnalyzer()
        expected=self.spam_ham_body_prob_expected
        self.assertEqual(ea.spam_ham_body_prob(self.clean_body_spam),expected)

        """
        Il faut mocker la fonction "load_dict"
        Il faut vérifier que probabilité est calculée correctement donné le "body" à l'entrée
        (ces probabilites devron etre calcule selon l'enonce dans le TP1 )
        """

    @patch("email_analyzer.EmailAnalyzer.load_dict")
    def test_subject_spam_ham_prob_Returns_expected_probability(self, mock_load_dict):

        mock_load_dict.return_value=self.vocab
        ea=EmailAnalyzer()
        expected=self.subject_spam_ham_prob_expected
        self.assertEqual(ea.spam_ham_body_prob(self.clean_subject_spam),expected)


        """
        Il faut mocker la fonction "load_dict"
        il faut vérifier que probabilité est calculée correctement donné le "sujet" a l'entrée
        (ces probabilites devron etre calcule selon l'enonce dans le TP1 )
        """


#if __name__ == "__main__":

    #unittest.main()

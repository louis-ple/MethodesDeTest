import json
from vocabulary_creator import VocabularyCreator
from renege import RENEGE
from email_analyzer import EmailAnalyzer
import random

def evaluate(test,vocab):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    total = 0
    analyzer = EmailAnalyzer(vocab)
    with open(test) as email_file:
        new_emails = json.load(email_file)

    i = 0
    email_count = len(new_emails["dataset"])

    print("Evaluating emails ")
    for e_mail in new_emails["dataset"]:
        i += 1
        print("\rEmail " + str(i) + "/" + str(email_count), end="")

        new_email = e_mail["mail"]
        subject = new_email["Subject"]
        body = new_email["Body"]
        spam = new_email["Spam"]

        if ((analyzer.is_spam(subject, body))) and (spam == "true"):
            tp += 1
        if (not (analyzer.is_spam(subject, body))) and (spam == "false"):
            tn += 1
        if ((analyzer.is_spam(subject, body))) and (spam == "false"):
            fp += 1
        if (not (analyzer.is_spam(subject, body))) and (spam == "true"):
            fn += 1
        total += 1

    #print("Accuracy: ", round((tp + tn) / (tp + tn + fp + fn), 2))

    return round((tp + tn) / (tp + tn + fp + fn), 2)
    #return (tp + tn) / (tp + tn + fp + fn)

def test_change_emails_order_train():
    print("Test #1: Changement de l’ordre des e-mails dans train")

    initial_accuracy=evaluate("train_set.json", "vocabulary.json")

    with open("train_set.json", "r") as file:
        emails=json.load(file)

    random.shuffle(emails["dataset"])

    with open("train700_mails.json", "w") as file2:
        json.dump(emails,file2)

    accuracy=evaluate("train700_mails.json", "vocabulary.json")

    print("")
    print("Initial accuracy: ", initial_accuracy)
    print("Accuracy: ", accuracy)

    if (accuracy / initial_accuracy) > 1.03 or (accuracy / initial_accuracy) < 0.97:
        print("Difference > 3%, test failed.")
    else:
        print("Difference < 3%, test passed.")

def test_change_emails_order_test():
    print("Test #2: Changement de l’ordre des e-mails dans test")

    initial_accuracy=evaluate("test_set.json", "vocabulary.json")

    with open("test_set.json", "r") as file:
        emails=json.load(file)

    random.shuffle(emails["dataset"])

    with open("test300_mails.json", "w") as file2:
        json.dump(emails,file2)

    accuracy=evaluate("test300_mails.json", "vocabulary.json")

    print("")
    print("Initial accuracy: ", initial_accuracy)
    print("Accuracy: ", accuracy)

    if (accuracy / initial_accuracy) > 1.03 or (accuracy / initial_accuracy) < 0.97:
        print("Difference > 3%, test failed.")
    else:
        print("Difference < 3%, test passed.")

def test_change_words_order_train():
    print("Test #3: Changement de l’ordre des mots dans train")

    initial_accuracy=evaluate("train_set.json", "vocabulary.json")

    with open("train_set.json", "r") as file:
        emails=json.load(file)

    for email in emails["dataset"]:

        subject=email["mail"]["Subject"]
        split_subject=subject.split(" ")
        random.shuffle(split_subject)
        join_subject = " ".join(split_subject)
        email["mail"]["Subject"] = join_subject

        body=email["mail"]["Body"]
        split_body=body.split(' ')
        random.shuffle(split_body)
        join_body=" ".join(split_body)
        email["mail"]["Body"] = join_body

    with open("train700_words.json", "w") as file2:
        json.dump(emails,file2)

    accuracy=evaluate("train700_words.json", "vocabulary.json")

    print("")
    print("Initial accuracy: ", initial_accuracy)
    print("Accuracy: ", accuracy)

    if (accuracy / initial_accuracy) > 1.03 or (accuracy / initial_accuracy) < 0.97:
        print("Difference > 3%, test failed.")
    else:
        print("Difference < 3%, test passed.")

def test_change_words_order_test():
    print("Test #4: Changement de l’ordre des mots dans test")

    initial_accuracy=evaluate("test_set.json", "vocabulary.json")

    with open("test_set.json", "r") as file:
        emails=json.load(file)

    for email in emails["dataset"]:

        subject=email["mail"]["Subject"]
        split_subject=subject.split(" ")
        random.shuffle(split_subject)
        join_subject = " ".join(split_subject)
        email["mail"]["Subject"] = join_subject

        body=email["mail"]["Body"]
        split_body=body.split(' ')
        random.shuffle(split_body)
        join_body=" ".join(split_body)
        email["mail"]["Body"] = join_body

    with open("test300_words.json", "w") as file2:
        json.dump(emails,file2)

    accuracy=evaluate("test300_words.json", "vocabulary.json")

    print("")
    print("Initial accuracy: ", initial_accuracy)
    print("Accuracy: ", accuracy)

    if (accuracy / initial_accuracy) > 1.03 or (accuracy / initial_accuracy) < 0.97:
        print("Difference > 3%, test failed.")
    else:
        print("Difference < 3%, test passed.")

def test_add_emails_train():
    print("Test #5: Ajout des mêmes e-mails dans train")

    initial_accuracy=evaluate("train_set.json", "vocabulary.json")

    with open("train_set.json", "r") as file:
        emails=json.load(file)

    for a,b in emails.items():
        emails[a].extend(b)

    with open("train700x2.json", "w") as file2:
        json.dump(emails,file2)

    accuracy=evaluate("train700x2.json", "vocabulary.json")

    print("")
    print("Initial accuracy: ", initial_accuracy)
    print("Accuracy: ", accuracy)

    if (accuracy / initial_accuracy) > 1.03 or (accuracy / initial_accuracy) < 0.97:
        print("Difference > 3%, test failed.")
    else:
        print("Difference < 3%, test passed.")


def test_add_emails_test():
    print("Test #6: Ajout des mêmes e-mails dans test")

    initial_accuracy=evaluate("test_set.json", "vocabulary.json")

    with open("test_set.json", "r") as file:
        emails=json.load(file)

    for a,b in emails.items():
        emails[a].extend(b)

    with open("test300x2.json", "w") as file2:
        json.dump(emails,file2)

    accuracy=evaluate("test300x2.json", "vocabulary.json")

    print("")
    print("Initial accuracy: ", initial_accuracy)
    print("Accuracy: ", accuracy)

    if (accuracy / initial_accuracy) > 1.03 or (accuracy / initial_accuracy) < 0.97:
        print("Difference > 3%, test failed.")
    else:
        print("Difference < 3%, test passed.")



def test_add_noise_train():
    print("Test #7: Ajout du bruit dans train")

def test_add_noise_test():
    print("Test #8: Ajout du bruit dans test")

test_change_emails_order_train()
test_change_emails_order_test()
test_change_words_order_train()
test_change_words_order_test()
test_add_emails_train()
test_add_emails_test()
test_add_noise_train()
test_add_noise_test()




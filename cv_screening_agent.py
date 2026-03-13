import re

import nltk

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


class CVScreeningAgent:

    def __init__(self, key_skills):

        self.key_skills = key_skills

        nltk.download('punkt')


    def analyze_cv(self, cv_text):

        # Tokenize the CV text

        tokens = nltk.word_tokenize(cv_text)

        return tokens


    def process_cv(self, cv_text):

        # Simple processing: remove special characters and lower case the text

        processed_text = re.sub('\W+', ' ', cv_text).lower()

        return processed_text


    def score_cv(self, processed_cv):

        # Calculate score based on keyword matches

        score = sum(1 for skill in self.key_skills if skill in processed_cv)

        return score


    def score_multiple_cvs(self, cvs):

        scores = {}

        for cv in cvs:

            processed_cv = self.process_cv(cv)

            score = self.score_cv(processed_cv)

            scores[cv] = score

        return scores


if __name__ == '__main__':

    key_skills = ['Python', 'Data Analysis', 'Machine Learning', 'NLP']

    agent = CVScreeningAgent(key_skills)

    sample_cv = "John Doe\nPython Developer with experience in Data Analysis and Machine Learning."

    print(agent.score_cv(agent.process_cv(sample_cv)))

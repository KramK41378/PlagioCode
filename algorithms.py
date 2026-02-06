from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compare_strings(lst_for_check, lst_to_check):
    cnt = 0
    for elem in lst_for_check:
        if elem in lst_to_check:
            cnt += 1
    return cnt / len(lst_for_check) * 100


def compare_without_spaces(lst_for_check, lst_to_check):
    cnt = 0
    lst1 = [elem.replace(' ', '') for elem in lst_for_check]
    lst2 = [elem.replace(' ', '') for elem in lst_to_check]
    for elem in lst1:
        if elem in lst2:
            cnt += 1
    return cnt / len(lst1) * 100


def strings_to_tfidf(strings_list):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(strings_list)
    return X.toarray()


def calculate_similarity(vectors1, vectors2):
    similarity_matrix = cosine_similarity(vectors1, vectors2)
    return similarity_matrix


def aggregate_similarity(similarity_matrix, method='optimal'):
    if method == 'mean':
        return np.mean(similarity_matrix) * 100
    elif method == 'optimal':
        max_per_row = np.max(similarity_matrix, axis=1)
        return np.mean(max_per_row) * 100

def compare_binary(lst1, lst2):
    list1 = lst1
    list2 = lst2
    all_strings = list1 + list2
    tfidf_matrix = strings_to_tfidf(all_strings)
    vectors1 = tfidf_matrix[:len(list1)]
    vectors2 = tfidf_matrix[len(list1):]
    similarity_matrix = calculate_similarity(vectors1, vectors2)
    percent = aggregate_similarity(similarity_matrix, method='optimal')
    return percent


def compare_simple_alg(code1, code2):
    min_len = min(len(code1), len(code2))
    exact_matches = 0

    for i in range(min_len):
        if code1[i].strip() == code2[i].strip():
            exact_matches += 1

    structural_matches = 0
    for i in range(min_len):
        line1, line2 = code1[i].strip(), code2[i].strip()

        if line1 != line2:
            keywords1 = set(word for word in line1.split() if word in ['def', 'if', 'else', 'for', 'while', 'return'])
            keywords2 = set(word for word in line2.split() if word in ['def', 'if', 'else', 'for', 'while', 'return'])

            if keywords1 == keywords2:
                structural_matches += 0.5

    total_matches = exact_matches + structural_matches
    max_lines = max(len(code1), len(code2))

    if max_lines == 0:
        return 0.0

    similarity = (total_matches / max_lines) * 100
    return round(similarity, 2)


if __name__ == "__main__":
    list1 = ["строrf", "ф", "строка 3"]
    list2 = ["строка 1", "другая строка", "строка 3"]
    print(f"{compare_simple_alg(list1, list2):.2f}%")

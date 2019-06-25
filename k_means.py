NITROGENOUS_BASES = "actg"
CODON_SIZE = 3
WORD_VECTOR_SIZE = 300


def drop_enough_to_make_divisible_by(sequences, divisible_by):
    excedents = len(sequences) % divisible_by
    return sequences[excedents:]


def make_matrix_from_list(sequence, number_of_columns):
    return_value = [sequence[i:i+number_of_columns]
                    for i in range(0, len(sequence) - 1, number_of_columns)]
    return return_value


def load_sequences(path):
    file = open(path, "r")
    contents = file.read()
    contents = contents.replace(">fragment of c.crescentus genome", "")
    contents = contents.replace("\n", "")
    sequences = [contents[i:i + CODON_SIZE]
                 for i in range(0, len(contents) - 1, CODON_SIZE)]
    return sequences


def make_count_dictionary(abecedary, word_size):
    return_value = {}
    abecedary_length = len(abecedary)
    number_of_words = abecedary_length ** word_size
    for i in range(0, number_of_words):
        word = ""
        for p in range(word_size - 1, -1, -1):
            index = int(i / abecedary_length ** p % abecedary_length)
            word = word + abecedary[index]
        return_value[word] = 0
    return return_value


def count_word_ocurrences_in_word_vector(word_vector, count_dictionary):
    for word in word_vector:
        count_dictionary[word] = count_dictionary[word] + 1


def count_word_ocurrences_in_matrix(word_matrix):
    counts = []
    for word_vector in word_matrix:
        count_dictionary = make_count_dictionary(NITROGENOUS_BASES, CODON_SIZE)
        count_word_ocurrences_in_word_vector(word_vector, count_dictionary)
        counts.append(count_dictionary)
    return counts

# TODO: Complete K-Means by preceding it with PCA: https://en.wikipedia.org/wiki/Principal_component_analysis#Details


def k_means():
    pass


sequences = load_sequences("ccrescentus.fa")
sequences = drop_enough_to_make_divisible_by(sequences, WORD_VECTOR_SIZE)
sequence_matrix = make_matrix_from_list(sequences, WORD_VECTOR_SIZE)
counts = count_word_ocurrences_in_matrix(sequence_matrix)
print(len(counts[0]))

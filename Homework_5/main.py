import pandas as pd
from numpy import log as ln

def calculate_probabilities(data):
    probabilities = {'democrat': 0, 'republican': 0}
    for i in range(1,17):
        probabilities['democrat_col'+str(i)+'_y'] = 0
        probabilities['democrat_col'+str(i)+'_n'] = 0
        probabilities['democrat_col'+str(i)+'_?'] = 0
        probabilities['republican_col'+str(i)+'_y'] = 0
        probabilities['republican_col'+str(i)+'_n'] = 0
        probabilities['republican_col'+str(i)+'_?'] = 0

    #class probabilities
    data_class_column_list = list(data['class'])
    data_class_column_len = len(data_class_column_list)
    democrats_count = data_class_column_list.count('democrat')
    republicans_count = data_class_column_list.count('republican')
    probabilities['democrat'] = democrats_count / data_class_column_len
    probabilities['republican'] = republicans_count / data_class_column_len

    for i in range(1, 17):
        data_col_x_column_list = list(data['col' + str(i)])
        c = 0
        for j in data_col_x_column_list:
            probabilities[data_class_column_list[c]+'_col'+str(i)+'_'+str(j)] += 1
            c += 1

    #escape from 0 probability
    for i in range(1,17):
        probabilities['democrat_col'+str(i)+'_y'] += 1
        probabilities['democrat_col'+str(i)+'_n'] += 1
        probabilities['democrat_col'+str(i)+'_?'] += 1
        probabilities['republican_col'+str(i)+'_y'] += 1
        probabilities['republican_col'+str(i)+'_n'] += 1
        probabilities['republican_col'+str(i)+'_?'] += 1

        #create actual probabilities
        probabilities['democrat_col'+str(i)+'_y'] /= democrats_count
        probabilities['democrat_col'+str(i)+'_n'] /= democrats_count
        probabilities['democrat_col'+str(i)+'_?'] /= democrats_count
        probabilities['republican_col'+str(i)+'_y'] /= republicans_count
        probabilities['republican_col'+str(i)+'_n'] /= republicans_count
        probabilities['republican_col'+str(i)+'_?'] /= republicans_count
    
    return probabilities
    
def shuffle_data(data):
    return data.sample(frac=1)

#use one loop for both probabilities
def calculate_democrat_and_republican_probability(probabilities, row_features):
    democrat_probability = 0
    republican_probability = 0
    for h in range(1,17):
        democrat_probability +=  ln(probabilities['democrat_col'+str(h)+'_'+row_features[h-1]])
        republican_probability += ln(probabilities['republican_col'+str(h)+'_'+row_features[h-1]])
    return democrat_probability, republican_probability

def select_probable_class(democrat_probability, republican_probability):
    return 'democrat' if democrat_probability > republican_probability else 'republican'

def update_accuracy_depending_on_probable_class(accuracies, probable_class, row_class, i):
    prev_accuracy_value = accuracies[i]
    new_accuracy_value = (prev_accuracy_value[0], prev_accuracy_value[1] + 1)
    if probable_class == row_class:
            new_accuracy_value = (prev_accuracy_value[0] + 1, prev_accuracy_value[1] + 1)
    accuracies[i] = new_accuracy_value
    return accuracies

def ten_fold_cross_validation(data, data_len):
    elements_per_set = int(data_len / 10)
    accuracies = [(0, 0)] * 10
    for i in range(9):
        set_for_test = data.iloc[i*elements_per_set:(i+1)*elements_per_set]
        set_for_learning_first_part = data.iloc[0:i*elements_per_set]
        set_for_learning_second_part = data.iloc[(i+1)*elements_per_set:]
        set_for_learning = set_for_learning_first_part.append(set_for_learning_second_part)
        probabilities = calculate_probabilities(set_for_learning)
        for j in range(elements_per_set):
            row_as_list = list(set_for_test.iloc[j])
            row_class = row_as_list[0]
            row_features = row_as_list[1:]
            democrat_probability, republican_probability = calculate_democrat_and_republican_probability(probabilities, row_features)
            probable_class = select_probable_class(democrat_probability, republican_probability)
            accuracies = update_accuracy_depending_on_probable_class(accuracies, probable_class, row_class, i)

    set_for_test = data.iloc[9*elements_per_set:]
    set_for_learning = data.iloc[:9*elements_per_set]
    probabilities = calculate_probabilities(set_for_learning)
    for j in range(len(list(set_for_test['class']))):
            row_as_list = list(set_for_test.iloc[j])
            row_class = row_as_list[0]
            row_features = row_as_list[1:]
            democrat_probability, republican_probability = calculate_democrat_and_republican_probability(probabilities, row_features)
            probable_class = select_probable_class(democrat_probability, republican_probability)
            accuracies = update_accuracy_depending_on_probable_class(accuracies, probable_class, row_class, 9)
    return accuracies

def print_output(accuracies):
    for accuracy in accuracies:
        accuracy_in_percents = round((accuracy[0] / accuracy[1] * 100))
        print('Accuracy: ' + str(accuracy[0]) + '/' + str(accuracy[1]) + '---->' + str(accuracy_in_percents) + '%')

def read_data_from_file(filename):
    columns = ['class', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12', 'col13', 'col14', 'col15', 'col16']
    data = pd.read_csv(filename, names=columns)
    return data

        
def main():
    filename = "data.csv"
    data = read_data_from_file(filename)
    data = shuffle_data(data)
    data_len = len(list(data['class']))
    accuracies = ten_fold_cross_validation(data, data_len)
    print_output(accuracies)


if __name__ == '__main__':
    main()

import pandas as pd

def calculate_probabilities(data):
    cols = list(data.columns)
    print(cols)
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
    print(probabilities['democrat'])
    print(probabilities['republican'])
    print(len(data_class_column_list))
    print(democrats_count)
    print(republicans_count)

    for i in range(1, 17):
        data_col_x_column_list = list(data['col' + str(i)])
        c = 0
        # classes = []
        for j in data_col_x_column_list:
            probabilities[data_class_column_list[c]+'_col'+str(i)+'_'+str(j)] += 1
            # classes.append(data_class_column_list[c])
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
    
    # assert classes == data_class_column_list
    return probabilities
    

def read_data_from_file(filename):
    columns = ['class', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12', 'col13', 'col14', 'col15', 'col16']
    data = pd.read_csv(filename, names=columns)
    #print(data)
    #print(list(data['republican']).count('democrat'))
    prob1= calculate_probabilities(data)
    data2 = data.sample(frac=1)
    print(data2)
    # prob2= calculate_probabilities(data2)

    # assert prob1 == prob2
    # # assert data == data2
    for col in columns:
        print(list(data[col]).count('?'))        

    
def main():
    filename = "data.csv"
    read_data_from_file(filename)


if __name__ == '__main__':
    main()


# probabilities = {'democrat': 0,
    #                  'republican': 0,
    #                  'democrat_col1_y': 0,
    #                  'democrat_col1_n': 0,
    #                  'democrat_col1_?': 0,
    #                  'republican_col1_y': 0,
    #                  'republican_col1_n': 0,
    #                  'republican_col1_?': 0,
    #                  'democrat_col2_y': 0,
    #                  'democrat_col2_n': 0,
    #                  'democrat_col2_?': 0,
    #                  'republican_col2_y': 0,
    #                  'republican_col2_n': 0,
    #                  'republican_col2_?': 0,
    #                  'democrat_col3_y': 0,
    #                  'democrat_col3_n': 0,
    #                  'democrat_col3_?': 0,
    #                  'republican_col3_y': 0,
    #                  'republican_col3_n': 0,
    #                  'republican_col3_?': 0,
    #                  'democrat_col4_y': 0,
    #                  'democrat_col4_n': 0,
    #                  'democrat_col4_?': 0,
    #                  'republican_col4_y': 0,
    #                  'republican_col4_n': 0,
    #                  'republican_col4_?': 0,
    #                  'democrat_col5_y': 0,
    #                  'democrat_col5_n': 0,
    #                  'democrat_col5_?': 0,
    #                  'republican_col5_y': 0,
    #                  'republican_col5_n': 0,
    #                  'republican_col5_?': 0,
    #                  'democrat_col6_y': 0,
    #                  'democrat_col6_n': 0,
    #                  'democrat_col6_?': 0,
    #                  'republican_col6_y': 0,
    #                  'republican_col6_n': 0,
    #                  'republican_col6_?': 0,
    #                  'democrat_col7_y': 0,
    #                  'democrat_col7_n': 0,
    #                  'democrat_col7_?': 0,
    #                  'republican_col7_y': 0,
    #                  'republican_col7_n': 0,
    #                  'republican_col7_?': 0,
    #                  'democrat_col8_y': 0,
    #                  'democrat_col8_n': 0,
    #                  'democrat_col8_?': 0,
    #                  'republican_col8_y': 0,
    #                  'republican_col8_n': 0,
    #                  'republican_col8_?': 0,
    #                  'democrat_col9_y': 0,
    #                  'democrat_col9_n': 0,
    #                  'democrat_col9_?': 0,
    #                  'republican_col9_y': 0,
    #                  'republican_col9_n': 0,
    #                  'republican_col9_?': 0,
    #                  'democrat_col10_y': 0,
    #                  'democrat_col10_n': 0,
    #                  'democrat_col10_?': 0,
    #                  'republican_col10_y': 0,
    #                  'republican_col10_n': 0,
    #                  'republican_col10_?': 0,
    
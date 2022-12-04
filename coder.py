import sys


def definecoding(letters, probability, dict_letters):
    dict_segment = dict_letters
    l = 0
    
    for i in range(0, 4):
        dict_segment[str(letters[i])][0] = float(l)
        dict_segment[str(letters[i])][1] = float(l) + float(probability[i])
        l = dict_segment[letters[i]][1] 
    
    return dict_segment


def coding(len_text, text, segment):
    left = 0.0
    right = 1.0
    
    for i in range(0, len_text - 1):
        symb = text[i]
        new_right = left + (right - left) * segment[symb][1]
        new_left = left + (right - left) * segment[symb][0]
        left = new_left
        right = new_right
    
    return (left + right) / 2


def main(letters, mas_probability, len_text, text, dict_letters):
    
    segment = definecoding(letters, mas_probability, dict_letters)
    res = coding(len_text, text, segment)
    
    return res
    
    

def get_data():
    data = []
    with open("file", "r+") as f:
        data.append(f.readline().split())
        data.append(f.readline().split())
    return data
if __name__ == '__main__':
    data = sys.argv[1:]
    
    text = data[0]
    len_text = len(text)
    
    let, res = get_data()
    
    dict_letters = {}
    # letters = "abcde"

    for v in let:
        dict_letters[v] = [0.0, 0.0]
        
    data_probability = res
    # mas_probability = data_probability.split()
    
    
    code = main(let, data_probability, len_text, text, dict_letters)
    
    print(code)
    print(len_text)
    

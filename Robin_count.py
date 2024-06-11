from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def mapper(line):
    for word in line.split():
        yield word, 1

def reducer(word, counts):
    return word, sum(counts)

def main(file_path):
    lines = read_input(file_path)
    mapped = []
    for line in lines:
        mapped.extend(list(mapper(line)))
    
    grouped = defaultdict(list)
    for word, count in mapped:
        grouped[word].append(count)
    
    reduced = []
    for word, counts in grouped.items():
        reduced.append(reducer(word, counts))
    
    for word, count in reduced:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main('input2.txt')

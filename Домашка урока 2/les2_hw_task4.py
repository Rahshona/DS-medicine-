words = input('Enter the words for the task with space:').split()
for i, v in enumerate(words, 1):
    print(f'{i}) {v:.10}')

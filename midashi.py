for x in open('README.md', encoding='utf-8'):
    if x.startswith('## '):
        print(x.strip()[3:] + ',', end=' ')

for x in open('README.md', encoding='utf-8'):
    if x.startswith('http'):
        print(x.strip())

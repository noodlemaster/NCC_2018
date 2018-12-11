from src.ciphers.temp.scytale import scytale
from src.tools.display import show_ioc

if __name__ == '__main__':
    # file = open('../../../questions/example/scytale.txt', 'r')
    file = open('../../../questions/2017/7b.txt', 'r')
    text = file.read()
    file.close()
    results = scytale(text, lower=3, upper=8, onlyfactor=False)
    for r in results:
        show_ioc(r, 25)

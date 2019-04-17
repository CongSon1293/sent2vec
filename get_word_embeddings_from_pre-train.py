from pyfasttext import FastText

ft = FastText('model.bin')
print ft.get_numpy_vector(u'you')

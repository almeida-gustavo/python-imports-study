def excl_display(text):
    print('!!!', text, '!!!')
    
def lined_display(text):
    print(''.join(['-' for _ in text]))
    print(text)
    print(''.join(['-' for _ in text]))
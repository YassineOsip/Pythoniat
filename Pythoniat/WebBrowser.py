import webbrowser

url = 'http://www.google.com'
webbrowser.open_new_tab(url)
query = input("Search  : ")
webbrowser.open_new_tab('http://ww.google.com/?q=%s' %query)


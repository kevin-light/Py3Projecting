temp = '流水'
temp_unicode = temp.decode('utf-8')
print(temp_unicode)
temp_gbk = temp_unicode.encode('gbk')
print(temp_gbk)
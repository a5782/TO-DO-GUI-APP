contents = ["fist_content","second_content","third_content"]
filenames = ["first.txt","second.txt","third.txt"]
#method1
'''
for i in range(len(filename)):
    file = open(filename[i],"w")
    file.writelines(contents[i])
    file.close()
'''
#method2
for content,filename in zip(contents,filenames):
         file = open(f"C:/Users/Aravind/PycharmProjects/PythonProject5/.venv/Lib/site-packages/files/{filename}","w")
         file.writelines(content)
         file.close()
a = "long string" \
    "still present" \
    "adaf"
print(a)
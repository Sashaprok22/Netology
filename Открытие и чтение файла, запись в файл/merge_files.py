files = [
    "files/1.txt",
    "files/2.txt",
    "files/3.txt",
]

files_lines = []

for file_path in files:
    with open(file_path) as file:
        files_lines.append((file_path, file.readlines()))

files_lines.sort(key=lambda a: len(a[1]))

with open("result.txt", "w") as result:
    for file_name, content in files_lines:
        result.writelines([file_name + "\n", str(len(content)) + "\n", "".join(content) + "\n"])
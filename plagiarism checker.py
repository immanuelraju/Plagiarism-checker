from difflib import SequenceMatcher
with open("file.txt") as file1, open("file2.txt") as file2:
    file1_data=file1.read()
    file2_data=file2.read()
    similarity_ratio=SequenceMatcher(None,file1_data,file2_data).ratio()
    print(similarity_ratio)

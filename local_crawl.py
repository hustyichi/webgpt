import json


def read_json_file(file_name: str):
    with open(file_name, "r") as f:
        json_data = json.load(f)
        docs = json_data[0]["docs"]
        return docs


def clean_doc(doc: dict):
    markdown_doc = doc["markdown"]
    line_data = markdown_doc.split("\n")

    flag = False
    flag_text = "由 GitBook 提供支持"
    end_flag_text = "上一页"
    end_flag_text2 = "下一页"
    clean_data = []
    for line in line_data:
        if line.find(flag_text) != -1:
            flag = True
            continue

        if line.find(end_flag_text) != -1 or line.find(end_flag_text2) != -1:
            break

        if flag:
            clean_data.append(line)

    return "\n".join(clean_data)


docs = read_json_file("documents.json")
clean_contents = []
for idx, doc in enumerate(docs):
    clean_content = clean_doc(doc)
    clean_contents.append(clean_content)

with open(f"data/page_full.md", "w") as f:
    f.write("\n\n\n".join(clean_contents))

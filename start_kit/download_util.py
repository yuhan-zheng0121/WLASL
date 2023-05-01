import json

def count_gloss(f):
    file = open(f)
    content = json.load(file)
    gloss = {}
    for entry in content:
        gloss[entry['gloss']] = len(entry['instances'])

    with open("summary.json", "w") as outfile:
        json.dump(gloss, outfile)

    sorted_gloss = sorted(gloss.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_gloss)

    with open("summary_sorted.json", "w") as outfile:
        json.dump(converted_dict, outfile)
    file.close()

def select_top_k(f, k):
    file = open(f)
    content = json.load(file)

    content.sort(key=lambda x: len(x['instances']), reverse=True)
    top_k = content[:k]

    out_file = "top_" + str(k) + "_words.json"
    with open(out_file, "w") as outfile:
        json.dump(top_k, outfile)

    file.close()

if __name__ == '__main__':
    file = "WLASL_v0.3.json"
    k = 40
    # count_gloss(file)
    # print("count_gloss DONE")
    select_top_k(file, k)
    print("select_top_k DONE")

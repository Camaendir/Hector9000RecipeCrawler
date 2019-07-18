import json

# sort.py

def main():
    with open("ingredients_clean.txt", "r") as f:
        items = json.loads(f.read())["items"]
        Faulty = []
        Correct = []
        correct_count = 0
        faulty_count = 0
        for item in items:
            print("Checking Drink Nr. %d" % (correct_count + faulty_count + 1))
            if item["faulty"]:
                faulty_count = faulty_count + 1
                Faulty.append(item)
            else:
                correct_count = correct_count + 1
                Correct.append(item)
        with open("ingredients_sorted_faulty.txt", "w+") as fa:
            fa.write(json.dumps(Faulty, indent=4, sort_keys=True))
        with open("ingredients_sorted_correct.txt", "w+") as cr:
            cr.write(json.dumps(Correct, indent=4, sort_keys=True))
        print("Found %d faulty Drinks" % faulty_count)
        print("Found %d correct Drinks" % correct_count)


if __name__ == "__main__":
    main()
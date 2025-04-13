import json

input_path = "captions.jsonl"
output_path = "cleaned_output.jsonl"

with open(input_path, 'r', encoding='utf-8') as infile, \
     open(output_path, 'w', encoding='utf-8') as outfile:

    for line in infile:
        try:
            obj = json.loads(line)
            cleaned_obj = {
                "image/key": obj.get("image/key"),
                "en": obj.get("en"),
                "es": obj.get("es")
            }
            json.dump(cleaned_obj, outfile, ensure_ascii=False)
            outfile.write('\n')
        except json.JSONDecodeError as e:
            print(f"Skipping line due to JSON error: {e}")

print(f"✅ Cleaned JSONL saved to {output_path}")


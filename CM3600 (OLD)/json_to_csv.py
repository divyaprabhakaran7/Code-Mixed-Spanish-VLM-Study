import json
import csv

input_path = "captions.jsonl"
output_path = "captions_output.csv"

# Open the output CSV file
with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(["image/key", "en_caption_1", "en_caption_2", "es_caption_1", "es_caption_2"])

    with open(input_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            try:
                obj = json.loads(line)
                key = obj.get("image/key", "")
                en_captions = obj.get("en", {}).get("caption", ["", ""])
                es_captions = obj.get("es", {}).get("caption", ["", ""])

                # Pad with empty strings if fewer than 2 captions
                en_captions += [""] * (2 - len(en_captions))
                es_captions += [""] * (2 - len(es_captions))

                writer.writerow([key, en_captions[0], en_captions[1], es_captions[0], es_captions[1]])

            except json.JSONDecodeError as e:
                print(f"Skipping line due to JSON error: {e}")

print(f"✅ CSV file saved to {output_path}")


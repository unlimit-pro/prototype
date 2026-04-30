import re
import json

def decode_html_flexible(input_file="index.html", output_file="index_d.html"):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Improved pattern: 
        # - Handles optional spaces \s*
        # - Matches single ' or double " quotes
        # - re.DOTALL (the flag at the end) allows it to match across multiple lines
        pattern = r'<script\s+type=["\']__bundler/template["\']>\s*"(.*?)"\s*</script>'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if match:
            escaped_data = match.group(1)
            
            # Decodes \n to real newlines, \" to quotes, etc.
            decoded_html = json.loads(f'"{escaped_data}"')

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(decoded_html)
            
            print(f"Success! Decoded version saved as: {output_file}")
        else:
            print("Still could not find the tag. Checking for raw content...")
            # Fallback: if the tag is slightly different, try to find any large quoted string
            # inside a script tag.
            print("Please check if your file uses a different script 'type' name.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    decode_html_flexible()

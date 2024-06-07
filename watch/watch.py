import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)', s):
        if match.group(0) == s:
            return None
        else:
            video_id = match.group(1)
            youtu_be_url = f"https://youtu.be/{video_id}"
            return youtu_be_url
    else:
        return None

if __name__ == "__main__":
    main()

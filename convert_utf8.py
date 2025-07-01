import os
import chardet

directory = "/Users/junhyung/Downloads/202505_주소DB_전체분"  # 변환할 파일들이 있는 디렉토리 경로
output_directory = "/Users/junhyung/Downloads/202505_주소DB_전체분-utf-8"

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)

        with open(filepath, "rb") as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            encoding = result["encoding"]

        print(f"{filename} 의 인코딩: {encoding}")

        try:
            with open(filepath, "r", encoding=encoding) as f:
                content = f.read()

            with open(
                os.path.join(output_directory, filename), "w", encoding="utf-8"
            ) as f:
                f.write(content)
        except Exception as e:
            print(f"오류 발생: {filename}, {e}")

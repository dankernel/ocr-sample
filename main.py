from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

words_file = "unique_korean_words.txt"


def draw_image(text):

    text = text.replace("/", "")

    # 1) 캔버스(이미지) 생성
    width, height = len(text) * 50, 200
    background_color = (255, 255, 255)  # 흰색 배경
    image = Image.new("RGB", (width, height), color=background_color)

    # 2) 드로잉 객체 생성
    draw = ImageDraw.Draw(image)

    # 3) 폰트 로드 (폰트 파일 경로와 크기 지정)
    #    예: 'NanumGothic.ttf' 를 프로젝트 폴더에 넣었다고 가정
    font_path = "HY견고딕.TTF"
    font_size = 48
    font = ImageFont.truetype(font_path, font_size)

    # 4) 텍스트와 위치 지정
    text_color = (0, 0, 0)  # 검정색
    # 텍스트 크기를 계산해서 중앙에 배치할 수도 있습니다.
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # 5) 이미지에 텍스트 그리기
    draw.text((x, y), text, font=font, fill=text_color)

    # 6) 파일로 저장
    output_path = f"output/{text}.png"
    image.save(output_path)


def main():

    with open(words_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in tqdm(lines):
        word = line[:-1]
        if not word:
            continue
        draw_image(word)


if __name__ == "__main__":
    main()

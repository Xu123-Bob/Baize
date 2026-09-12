from PIL import Image, ImageEnhance

BRAILLE_MAP = [
    [0x01, 0x08],
    [0x02, 0x10],
    [0x04, 0x20],
    [0x40, 0x80]
]

def generate_braille_logo(image_path, output_path, width=60, threshold=100):
    img = Image.open(image_path)

    # 处理透明背景 → 黑色背景
    if img.mode in ('RGBA', 'LA'):
        img = img.convert('RGBA')
        bg = Image.new('RGB', img.size, (0, 0, 0))
        bg.paste(img, mask=img.split()[-1])
        img = bg
    else:
        img = img.convert('RGB')

    # 增强对比度
    img = ImageEnhance.Contrast(img).enhance(1.8)

    # 目标字符行数（每个 Braille 字符占 4 行像素，宽高比约 2:1）
    char_rows = max(1, int(width * img.height / img.width * 0.5))
    # 实际像素高度，必须为 4 的倍数
    pixel_height = char_rows * 4

    # 缩放图片
    img = img.resize((width, pixel_height), Image.Resampling.LANCZOS)

    # 获取像素数据
    gray = img.convert('L')
    pixels_gray = list(gray.getdata())
    pixels_rgb = list(img.getdata())
    print(f"调试：宽度={width}, 字符行数={char_rows}, 像素高={pixel_height}, 像素总数={len(pixels_gray)}")

    output_lines = []
    for row in range(char_rows):
        y_base = row * 4
        line = ""
        for x in range(width):
            block = []
            for dy in range(4):
                for dx in range(2):
                    idx = (y_base + dy) * width + (x + dx)
                    # 安全边界检查（理论上不会越界，但留一手）
                    if idx >= len(pixels_gray):
                        block.append(0)
                    else:
                        block.append(pixels_gray[idx])

            if max(block) > threshold:
                braille_code = 0
                for dy in range(4):
                    for dx in range(2):
                        if block[dy * 2 + dx] > threshold:
                            braille_code |= BRAILLE_MAP[dy][dx]
                # 取块左上角像素颜色
                color_idx = y_base * width + x
                if color_idx >= len(pixels_rgb):
                    r, g, b = 255, 215, 0  # 备用金色
                else:
                    r, g, b = pixels_rgb[color_idx][:3]
                line += f"\033[38;2;{r};{g};{b}m{chr(0x2800 + braille_code)}"
            else:
                line += " "
        output_lines.append(line + "\033[0m")

    art = '\n'.join(output_lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(art)
    print(f"✓ 已生成 {output_path}，宽度 {width}，行数 {char_rows}")

if __name__ == "__main__":
    generate_braille_logo(
        r"D:\资料文件_实际\Claude Code自制软件\白泽agent\LOGO和启动交互界面\logo.png",
        "logo.txt",
        width=80
    )
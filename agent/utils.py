import shutil
import wcwidth

# utils.py 顶部添加
PRINT_DETAILS = True   # 默认打印，CLI 模式下会设为 False


def printed_length(s):
    length = 0
    for char in s:
        width = wcwidth.wcwidth(char)
        if width > 0:  # Exclude zero-width characters
            length += width
    return length

def lined_print(info):
    terminal_width = shutil.get_terminal_size().columns
    info_len = printed_length(info)
    # 计算左右宽度
    side_len = (terminal_width - info_len - 4) // 2  # 留出 ◀ 和 ▶ 的位置
    left = '═' * side_len
    right = '═' * side_len
    # 拼合：◀══════ 信息 ══════▶
    line = f"◀{left} {info} {right}▶"
    # 对齐补齐
    if printed_length(line) < terminal_width:
        line += '═'
    print("\n\n")
    print(f"\033[90m{line}\033[0m")
    
def framed_print(title, content, style="default"):
    """Print content in a styled frame, wrapping long lines instead of truncating"""
    # ========== 新增：若全局关闭，则直接返回 ==========
    if not PRINT_DETAILS:
        return
    lines = content.split('\n')
    frame_width = shutil.get_terminal_size().columns

    # Define ANSI color codes
    colors = {
        "default": {"frame": "\033[90m", "title": "\033[1m", "reset": "\033[0m"},
        "info": {"frame": "\033[94m", "title": "\033[1;94m", "reset": "\033[0m"},
        "warning": {"frame": "\033[93m", "title": "\033[1;93m", "reset": "\033[0m"},
        "error": {"frame": "\033[91m", "title": "\033[1;91m", "reset": "\033[0m"},
        "success": {"frame": "\033[92m", "title": "\033[1;92m", "reset": "\033[0m"}
    }

    color = colors.get(style, colors["default"])

    # Draw top border with title
    top_border_with_title = f"┌───── {title} "
    top_border_with_title += "─" * (frame_width - printed_length(top_border_with_title) - 1)
    top_border_with_title += "┐"

    # Print frame
    print(f"{color['frame']}{''.join(top_border_with_title)}{color['reset']}")

    # Print content lines with wrapping
    display_width = frame_width - 4  # 2 spaces on each side

    for line in lines:
        if line.strip() == "":
            # Empty line - just print spaces
            print(f"{color['frame']}│ {' ' * display_width} │{color['reset']}")
            continue

        # Wrap long lines
        current_pos = 0
        while current_pos < len(line):
            wrapped_line = ""
            current_width = 0
            start_pos = current_pos

            # Build wrapped line character by character
            while current_pos < len(line):
                char = line[current_pos]
                char_width = wcwidth.wcwidth(char)

                if current_width + char_width <= display_width:
                    wrapped_line += char
                    current_width += char_width
                    current_pos += 1
                else:
                    break

            # If we didn't add any characters (shouldn't happen), advance by 1
            if current_pos == start_pos:
                wrapped_line = line[current_pos]
                current_pos += 1

            # Pad with spaces to fill the line
            while current_width < display_width:
                wrapped_line += " "
                current_width += 1

            print(f"{color['frame']}│ {wrapped_line} │{color['reset']}")

    # Print bottom border
    print(f"{color['frame']}└" + "─" * (frame_width - 2) + f"┘{color['reset']}")
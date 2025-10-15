import time


ESC = "\x1b"
CSI = f"{ESC}["
RESET=f'{CSI}0m'


def Loading():
    time.sleep(0.2)

def show_progress(num_task, width):
    for task in range(num_task):
        for filled in range(0, width):
            bar=f"{'#'*filled}{'-' * (width - filled-1)}"
            print(f"{CSI}1G{task}/{num_task}{bar}",
                end="",
                flush=True)
            time.sleep(0.1)

if __name__=="__main__":
    show_progress(1,30)
    print(f'{CSI}3mlalala')


def draw_line(offset, length, colour=213):
    line=f'{" "* offset}{CSI}48;5;(colour)m{" "* length}{RESET}'

def draw_romb(height=15):
    center = height // 2
    step = 1
    length = 1
    offset = center
    while True:
        for colour in range(16,232):
            for line in range(height):
                

    for line in range(height):
        draw_line(offset, length)
        if line < center:
            offset -= step
            length += step * 2
        else:
            offset +=step
            length -= step*2

if __name__=="__main__":
    draw_romb()
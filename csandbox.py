import sys

from copcode import (Function, new_frame, frames, run)


def init():
    assert len(sys.argv) == 2 and sys.argv[1].endswith(".py")
    source = open(sys.argv[1]).read()
    co = compile(source, sys.argv[1], 'exec')
    fun = Function(sys.argv[1], co)
    frame = new_frame(fun)
    return frame


def main():
    frame = init()
    frames.append(frame)
    run(frame)
    frames.pop()


if __name__ == '__main__':
    main()

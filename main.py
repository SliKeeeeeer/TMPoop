import sys

from container import Container


def main():
    if len(sys.argv) != 3:
        print('Incorrect command line input')
        sys.exit(1)

    try:
        input_file = open(sys.argv[1], "r")
    except OSError:
        print('Opening file error')
        sys.exit(1)

    print('Start')

    cont = Container()

    cont.read_from(input_file)
    print('Filled container')

    try:
        output_file = open(sys.argv[2], "w")
    except OSError:
        print('Opening file error')
        sys.exit(1)
    finally:
        input_file.close()

    cont.sort()
    cont.write_to(output_file)
    # cont.write_to_procedure(output_file)

    cont.clear()

    print('Empty container')
    cont.write_to(output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()

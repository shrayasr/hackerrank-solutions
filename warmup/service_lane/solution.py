def get_inputs():

    first_line = raw_input()
    first_line_splits = first_line.strip().split()

    len_freeway = first_line_splits[0]
    T = int(first_line_splits[1])

    second_line = raw_input()
    width_array = [ int(width) for width in second_line.strip().split() ]

    entries_exits = []
    for i in xrange(0,T):
        entry_exit_line = raw_input()
        entries_exits.append([ int(entry_exit) for entry_exit in entry_exit_line.strip().split() ])

    return width_array, entries_exits

def main():

    width_array, entries_exits = get_inputs()

    for entry_exit in entries_exits:

        entry = int(entry_exit[0])
        exit = int(entry_exit[1])

        segments_to_traverse = width_array[entry:exit+1]
        print min(segments_to_traverse)

if __name__ == "__main__":
    main()

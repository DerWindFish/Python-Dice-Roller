def parse_input(input_string):
    # Return 'input_string as the die selection

    if input_string.strip() in {'d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'}:
        return int(input_string)
    else:
        print('Please pick one of the following option: [d4, d6, d8, d10, d12, d20, d100]')
        raise SystemExit(1)
# Get user input for which die they would like to roll
which_die_input = input('Which die would you like to roll? [d4, d6, d8, d10, d12, d20, d100]')
which_die = parse_input(which_die_input)
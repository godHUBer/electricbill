"""A simple CSV-based electricity billing project."""

import csv
from pathlib import Path

BILL_FILE = Path(__file__).with_name('bills.csv')
HEADINGS = ['Bill ID', 'Customer', 'Previous Reading', 'Current Reading',
            'Units', 'Amount (Rs.)']


def calculate_bill(units):
    """Apply sample rates to each block of units, plus a fixed charge."""
    if units <= 100:
        return 50 + units * 4
    if units <= 200:
        return 50 + 100 * 4 + (units - 100) * 6
    return 50 + 100 * 4 + 100 * 6 + (units - 200) * 8


def load_bills():
    with BILL_FILE.open(newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def show_bill(bill):
    print('\n--- Electricity Bill ---')
    for heading in HEADINGS:
        print(heading + ': ' + bill[heading])


def add_bill():
    name = input('Customer name: ').strip()
    if not name:
        print('Customer name cannot be empty.')
        return

    readings = read_readings()
    if readings is None:
        return

    previous, current = readings
    bills = load_bills()
    bill_id = max([int(bill['Bill ID']) for bill in bills], default=0) + 1
    bill = make_bill(bill_id, name, previous, current)
    with BILL_FILE.open('a', newline='', encoding='utf-8') as file:
        csv.DictWriter(file, fieldnames=HEADINGS).writerow(bill)
    print('Bill saved.')
    show_bill(bill)


def list_bills():
    bills = load_bills()
    if not bills:
        print('No bills saved yet.')
        return

    print_table(bills)


def find_bill():
    bills = load_bills()
    index = select_bill(bills)
    if index is not None:
        show_bill(bills[index])


def print_table(bills):
    """Print a compact table for a list of bill dictionaries."""
    if not bills:
        print('No matching bills.')
        return

    row_format = '{:<8} {:<24} {:>8} {:>14}'
    print()
    print(row_format.format('Bill ID', 'Customer', 'Units', 'Amount (Rs.)'))
    print('-' * 57)
    for bill in bills:
        print(row_format.format(bill['Bill ID'], bill['Customer'][:24],
                                bill['Units'], bill['Amount (Rs.)']))


def search_customer():
    """Find bills even if the user enters only part of a name."""
    name = input('Enter all or part of a customer name: ').strip().lower()
    if not name:
        print('Enter at least one letter or character.')
        return

    matches = []
    for bill in load_bills():
        if name in bill['Customer'].lower():
            matches.append(bill)
    print_table(matches)


def read_readings():
    """Read and validate a pair of meter readings."""
    try:
        previous = int(input('Previous meter reading: '))
        current = int(input('Current meter reading: '))
    except ValueError:
        print('Please enter whole-number meter readings.')
        return None

    if previous < 0 or current < previous:
        print('Readings must be non-negative and current cannot be below previous.')
        return None

    return previous, current


def make_bill(bill_id, name, previous, current):
    """Build a bill dictionary using the CSV column names."""
    units = current - previous
    return {
        'Bill ID': str(bill_id),
        'Customer': name,
        'Previous Reading': str(previous),
        'Current Reading': str(current),
        'Units': str(units),
        'Amount (Rs.)': f'{calculate_bill(units):.2f}',
    }


def save_bills(bills):
    """Rewrite the CSV after a confirmed change."""
    with BILL_FILE.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADINGS)
        writer.writeheader()
        writer.writerows(bills)


def select_bill(bills):
    """Return the position of a bill with the requested ID."""
    bill_id = input('Enter bill ID: ').strip()
    for index in range(len(bills)):
        if bills[index]['Bill ID'] == bill_id:
            return index

    print('Bill not found.')
    return None


def correct_bill():
    """Correct a saved bill without changing its ID."""
    bills = load_bills()
    index = select_bill(bills)
    if index is None:
        return

    old_bill = bills[index]
    show_bill(old_bill)
    name = input('Customer name (Enter to keep it): ').strip()
    if not name:
        name = old_bill['Customer']

    readings = read_readings()
    if readings is None:
        return

    previous, current = readings
    corrected = make_bill(old_bill['Bill ID'], name, previous, current)
    show_bill(corrected)
    answer = input('Save this correction? (y/n): ').strip().lower()
    if answer != 'y':
        print('No changes saved.')
        return

    bills[index] = corrected
    save_bills(bills)
    print('Bill updated.')


def show_summary():
    """Calculate totals and find the bill with the highest usage."""
    bills = load_bills()
    if not bills:
        print('No bills saved yet.')
        return

    total_units = 0
    total_amount = 0
    highest = bills[0]
    for bill in bills:
        units = int(bill['Units'])
        total_units += units
        total_amount += float(bill['Amount (Rs.)'])
        if units > int(highest['Units']):
            highest = bill

    print('\n--- Billing Summary ---')
    print('Bills saved:', len(bills))
    print('Total units:', total_units)
    print(f'Total billed: Rs. {total_amount:.2f}')
    print(f'Average bill: Rs. {total_amount / len(bills):.2f}')
    print(f"Highest usage: {highest['Units']} units (bill {highest['Bill ID']})")


def estimate_bill():
    """Try the rates without saving a customer record."""
    try:
        units = int(input('Enter expected units: '))
    except ValueError:
        print('Enter a whole number.')
        return

    if units < 0:
        print('Units cannot be negative.')
        return

    first = min(units, 100)
    second = min(max(units - 100, 0), 100)
    third = max(units - 200, 0)
    print('\n--- Estimated Bill (not saved) ---')
    print(f'First block: {first} x Rs. 4 = Rs. {first * 4}')
    print(f'Second block: {second} x Rs. 6 = Rs. {second * 6}')
    print(f'Third block: {third} x Rs. 8 = Rs. {third * 8}')
    print('Fixed charge: Rs. 50')
    print(f'Total: Rs. {calculate_bill(units):.2f}')


def filter_by_usage():
    """List bills whose usage meets a minimum number of units."""
    try:
        minimum = int(input('Minimum units to show: '))
    except ValueError:
        print('Enter a whole number.')
        return

    if minimum < 0:
        print('Minimum units cannot be negative.')
        return

    matches = []
    for bill in load_bills():
        if int(bill['Units']) >= minimum:
            matches.append(bill)
    print_table(matches)


def more_options():
    while True:
        print('\n--- More Billing Tools ---')
        print('1. Search by customer name')
        print('2. Correct a saved bill')
        print('3. Show billing summary')
        print('4. Estimate a bill')
        print('5. Filter bills by usage')
        print('6. Back to main menu')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            search_customer()
        elif choice == '2':
            correct_bill()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            estimate_bill()
        elif choice == '5':
            filter_by_usage()
        elif choice == '6':
            return
        else:
            print('Choose a number from 1 to 6.')


def main():
    if not BILL_FILE.exists() or BILL_FILE.stat().st_size == 0:
        save_bills([])

    while True:
        print('\n=== Electricity Bill System ===')
        print('1. Add bill\n2. List bills\n3. Find bill by ID\n4. Exit\n5. More billing tools')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            add_bill()
        elif choice == '2':
            list_bills()
        elif choice == '3':
            find_bill()
        elif choice == '4':
            print('Goodbye!')
            break
        elif choice == '5':
            more_options()
        else:
            print('Choose a number from 1 to 5.')


if __name__ == '__main__':
    main()

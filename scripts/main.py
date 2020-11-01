import os
import re
import argparse


def range_extract(lst):
    # Yield 2-tuple ranges or 1-tuple single elements from list of increasing ints
    lenlst = len(lst)
    i = 0
    while i < lenlst:
        low = lst[i]
        while i < lenlst - 1 and lst[i] + 1 == lst[i + 1]:
            i += 1
        hi = lst[i]
        if hi - low >= 2:
            yield (low, hi)
        elif hi - low == 1:
            yield (low,)
            yield (hi,)
        else:
            yield (low,)
        i += 1


def printr(ranges):
    print(",".join((("%i-%i" % r) if len(r) == 2 else "%i" % r) for r in ranges))


def find_missing(lst, start, end):
    if start:
        list_start = start
    else:
        list_start = lst[0]

    if end:
        list_end = end
    else:
        list_end = lst[-1]

    return sorted(set(range(list_start, list_end + 1)).difference(lst))


def main(args):
    working_dir = args.dir

    extensions = ["cb7", "cba", "cbr", "cbt", "cbz"]

    if args.filetype:
        if args.filetype.startswith("."):
            extensions.append(args.filetype[1:])
        else:
            extensions.append(args.filetype)

    files = []
    files_matched = []

    for f in os.listdir(working_dir):
        if os.path.isfile(os.path.join(working_dir, f)) and (
                f.lower().endswith(tuple(extensions))
        ):
            files.append(f)

    if not files:
        print("No comic files found in " + os.path.abspath(working_dir))
        exit(1)

    re_issue_number_pound = re.compile(r"^.+#(\d+)")
    # re_issue_number_first_digit = re.compile(r"^(?:[^\d]+)(?:\s+|#)(\d+)")
    # re_issue_number_second_digit = re.compile(r"(?:\d+)[^\d]+(\d+)(?:\s|\b)")

    if args.digit_group:
        re_issue_number_nth_digit = re.compile(
            r"(?:(?:\d+)[^\d]+){" + str(args.digit_group - 1) + r"}(\d+)(?:\s|\b)"
        )
        re_method = re_issue_number_nth_digit
    else:
        re_method = re_issue_number_pound

    for issue in files:
        try:
            issue_number: str = re.search(re_method, issue).group(1)
            files_matched.append(int(issue_number))
        except AttributeError:
            continue

    if not files_matched:
        print("No matching comic files in " + os.path.abspath(working_dir))
        exit(1)

    files_matched.sort()

    print("\nHave list:")
    printr(range_extract(files_matched))

    print("\nMiss List:")
    printr(range_extract(find_missing(files_matched, args.start, args.end)))


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dir", type=str, nargs="?", default=os.getcwd(), help="Input folder"
    )
    parser.add_argument("--start", "-s", type=int, help="Starting number")
    parser.add_argument("--end", "-e", type=int, help="Ending number")
    parser.add_argument(
        "--digit-group",
        "-d",
        type=int,
        nargs="?",
        const=1,
        help="Nth digit group in file name that contains issue number",
    )
    parser.add_argument("--filetype", "-f", type=str, help="Custom file extension to check for")

    args_namespace = parser.parse_args()
    main(args_namespace)


if __name__ == "__main__":
    cli()

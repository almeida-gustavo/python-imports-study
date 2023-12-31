import argparse
import importlib.metadata
import sys


def default_output(output: str) -> None:
    print(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputer', default='default')
    args = parser.parse_args()

    eps = importlib.metadata.entry_points(group="this_name_can_be_what_i_want")
    # both produces the same result
    # eps = importlib.metadata.entry_points()["this_name_can_be_what_i_want"]
    print(eps)
    outputers = {
        entrypoint.name: entrypoint
        for entrypoint in eps
    }

    try:
        outputer = outputers[args.outputer].load()
    except KeyError:
        print(f'outputer {args.outputer} is not available!', file=sys.stderr)
        outputers_s = ', '.join(sorted(outputers))
        print(f'available outputers: {outputers_s}', file=sys.stderr)
        return 1

    outputer('hello world')

    return 0


# if __name__ == '__main__':
#     exit(main())
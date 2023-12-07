import argparse

_UNSET = object()


class CliArg:
    def __init__(self,
                 flags=_UNSET,
                 help=_UNSET,
                 action=_UNSET,
                 default=_UNSET,
                 nargs=_UNSET,
                 type=_UNSET,
                 choices=_UNSET,
                 required=_UNSET,
                 metavar=_UNSET,
                 dest=_UNSET):

        self.flags = flags
        self.kwargs = {}
        for k, v in locals().items():
            if v is _UNSET:
                continue
            if k in ("self", "flags"):
                continue

            self.kwargs[k] = v

    def add_to_parser(self, parser: argparse.ArgumentParser):
        """Add this argument to an ArgumentParser."""
        parser.add_argument(*self.flags, **self.kwargs)


ACTION_NAME_ID = CliArg(("-a", "--action",),
                        help="The action type to perform",
                        choices=("anonymization", "p-anonymization"))

CONFIG_FILE = CliArg(("-f", "--config-file",), help="File that contains configuration about datasource")


if __name__ == '__main__':
    t_parser = argparse.ArgumentParser()
    args = t_parser.parse_args()

    print(args)
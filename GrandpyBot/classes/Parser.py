import re


class Parser:
    def parse(self, entry):
        """
        Parse the user input in parameter
        :param entry:
        :return:
        """
        result = None
        entry = entry.lower()
        parser = re.compile(
            "(.+\s)*(où se trouve [a-zA-Z ]+ *\?)$"
        )
        found = parser.match(entry)
        if found:
            if len(found.groups()) == 1:
                result = found.groups()[0]
            else:
                result = found.groups()[1]

        return result
from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements=None):
        self.text = text
        self.offset = offset
        self.elements = elements or []

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.Dig = elements[3]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.Year = elements[0]
        self.Month = elements[2]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.Day = elements[1]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[1-9]')
    REGEX_2 = re.compile('^[0-2]')
    REGEX_3 = re.compile('^[1-9]')
    REGEX_4 = re.compile('^[1-2]')
    REGEX_5 = re.compile('^[0-9]')
    REGEX_6 = re.compile('^[0-1]')
    REGEX_7 = re.compile('^[0-9]')

    def _read_transaction(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['transaction'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        address0 = self._read_Date()
        self._cache['transaction'][index0] = (address0, self._offset)
        return address0

    def _read_Year(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Year'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Dig()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Dig()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_Dig()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_Dig()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode1(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Year'][index0] = (address0, self._offset)
        return address0

    def _read_Month(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Month'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '0':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'0\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 is not None and Grammar.REGEX_1.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[1-9]')
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address3 = FAILURE
            chunk2 = None
            if self._offset < self._input_size:
                chunk2 = self._input[self._offset:self._offset + 1]
            if chunk2 == '1':
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'1\'')
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                chunk3 = None
                if self._offset < self._input_size:
                    chunk3 = self._input[self._offset:self._offset + 1]
                if chunk3 is not None and Grammar.REGEX_2.search(chunk3):
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-2]')
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['Month'][index0] = (address0, self._offset)
        return address0

    def _read_Day(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Day'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '0':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'0\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 is not None and Grammar.REGEX_3.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[1-9]')
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address3 = FAILURE
            chunk2 = None
            if self._offset < self._input_size:
                chunk2 = self._input[self._offset:self._offset + 1]
            if chunk2 is not None and Grammar.REGEX_4.search(chunk2):
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[1-2]')
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                chunk3 = None
                if self._offset < self._input_size:
                    chunk3 = self._input[self._offset:self._offset + 1]
                if chunk3 is not None and Grammar.REGEX_5.search(chunk3):
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9]')
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index4, elements2 = self._offset, []
                address5 = FAILURE
                chunk4 = None
                if self._offset < self._input_size:
                    chunk4 = self._input[self._offset:self._offset + 1]
                if chunk4 == '3':
                    address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address5 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'3\'')
                if address5 is not FAILURE:
                    elements2.append(address5)
                    address6 = FAILURE
                    chunk5 = None
                    if self._offset < self._input_size:
                        chunk5 = self._input[self._offset:self._offset + 1]
                    if chunk5 is not None and Grammar.REGEX_6.search(chunk5):
                        address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address6 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[0-1]')
                    if address6 is not FAILURE:
                        elements2.append(address6)
                    else:
                        elements2 = None
                        self._offset = index4
                else:
                    elements2 = None
                    self._offset = index4
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = TreeNode(self._input[index4:self._offset], index4, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['Day'][index0] = (address0, self._offset)
        return address0

    def _read_Date(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Date'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Year()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == '-':
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'-\'')
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_Month()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    index2 = self._offset
                    index3, elements1 = self._offset, []
                    address5 = FAILURE
                    chunk1 = None
                    if self._offset < self._input_size:
                        chunk1 = self._input[self._offset:self._offset + 1]
                    if chunk1 == '-':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'-\'')
                    if address5 is not FAILURE:
                        elements1.append(address5)
                        address6 = FAILURE
                        address6 = self._read_Day()
                        if address6 is not FAILURE:
                            elements1.append(address6)
                        else:
                            elements1 = None
                            self._offset = index3
                    else:
                        elements1 = None
                        self._offset = index3
                    if elements1 is None:
                        address4 = FAILURE
                    else:
                        address4 = TreeNode3(self._input[index3:self._offset], index3, elements1)
                        self._offset = self._offset
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[index2:index2], index2)
                        self._offset = index2
                    if address4 is not FAILURE:
                        elements0.append(address4)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode2(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Date'][index0] = (address0, self._offset)
        return address0

    def _read_Dig(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Dig'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_7.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[0-9]')
        self._cache['Dig'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_transaction()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()

def addEval(text: str, doEval = True) -> str:
    return f"eval({text})" if doEval else text

class StringManipulators:
    def string_to_decimal(self, text: str) -> list[int]:
        return list(map(ord, text))

    def decimal_to_chrs(self, array: list, evaluate = True) -> str:
        '''
        Wraps each element of array in `chr()` and concatenates them.
        `evaluate` : Wrap in `eval()` (default True)

        Example: `[101, 102]` -> `eval(chr(101)+chr(102))`
        '''
        return addEval(f'chr({")+chr(".join(map(str, array))})', evaluate)

    def string_to_chrs(self, text: str, evaluate = True) -> str:
        '''
        Converts strings to their decimal equivalent, wrapped in `chr()` and concatenated.
        `evaluate` : Wrap in `eval()` (default True)

        Example: `Hello` -> `eval(chr(72)+chr(101)+chr(108)+chr(108)+chr(111))`
        '''
        return addEval(self.decimal_to_chrs(list(map(ord, text)), evaluate=False), evaluate)

class NumberManipulators:
    def int_addition(self, num: int, evaluate = True) -> str:
        '''
        Self explanatory look at the example
        `evaluate` : Wrap in `eval()` (default True)

        Example: `10` -> `eval(1+1+1+1+1+1+1+1+1+1)`
        '''
        return addEval("+".join(["1"] * num), evaluate)


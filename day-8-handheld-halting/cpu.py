class InfiniteLoopError(Exception):
    pass

class CPU:

    def __init__(self, instructions=None, debug=False, detect_loop=False):
        self.instructions = instructions if instructions is not None else []
        self.debug = debug
        self.detect_loop = detect_loop
        
        self.pc = 0         # program counter
        self.ir = None      # instruction register
        self.acc = 0        # accumulator

        self.op = None
        self.arg = None
        
        # Total number of instructions executed
        self.loops = 0

        # All PC values previously visited, used to detect loops
        self.history = set()

    def step(self):
        self._fetch()
        self._decode()
        self._execute()
        self.loops += 1

    def run(self):
        if self.debug:
            print('state\tpc\tir\tacc\top\targ\tloops')
            print('-----\t-----\t-----\t-----\t-----\t-----\t-----')
            self._print_debug('START')

        try:
            while True:
                self.step()
        except InfiniteLoopError:
            if self.debug:
                self._print_debug('LOOP')
        except IndexError:
            return self._exit()

    def report_state(self):
        return {
            'pc': self.pc,
            'ir': self.ir,
            'acc': self.acc,
            'op': self.op,
            'arg': self.arg,
            'loops': self.loops,
        }

    def _print_debug(self, state):
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(state, self.pc, self.ir, self.acc, self.op, self.arg, self.loops))

    def _exit(self):
        if self.debug:
            self._print_debug('EXIT')
        return 0
    
    def _fetch(self):
        self.ir = self.pc
        self.pc += 1

        if self.debug:
            self._print_debug('FETCH')

        return self.ir

    def _decode(self):
        instruction = self.instructions[self.ir]
        self.op, self.arg = instruction.split()
        self.arg = int(self.arg)

        if self.debug:
            self._print_debug('DECODE')

        return self.op, self.arg

    def _execute(self, ignore_loop=False):
        if self.detect_loop and not ignore_loop:
            if self.ir in self.history:
                raise InfiniteLoopError
            self.history.add(self.ir)

        if self.op == 'acc':
            self.acc += self.arg
        elif self.op == 'jmp':
            self.pc += self.arg - 1

        if self.debug:
            self._print_debug('EXECUTE')